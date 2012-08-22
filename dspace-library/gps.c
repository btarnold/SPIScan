//
//  (C) Paul Campbell paul@taniwha.com 2012
//
#define GPS_TTY "/dev/tty0"
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <termios.h>
#include <errno.h>
#include <fcntl.h>

static pthread_mutex_t gps_mutex = PTHREAD_MUTEX_INITIALIZER;
static bool gps_lock=0;      // gps is locked
static double vlat, vlong;

double gps_long(void)
{
	return vlong;
}

double gps_lat(void)
{
	return vlat;
}

int gps_locked(void) { return gps_lock?1:0; }

double
cvt_gps_to_frac(char *cp)
{
        char *cp2;
	double d;
        int deg;
        
	cp2 = cp;
	for (;;) {
		if (!*cp)
			return -1;
		if (*cp == '.')
			break;
		cp++;
	}
	if ((cp-cp2) < 2)
		return -1;
	d = atof(cp-2);
	cp[-2] = 0;
	deg = atoi(cp2);
	d = ((double)deg)+(d/60.0);

	return d;
}

int 
to_hex(char c)
{
  if (c >= '0' && c <= '9') {
       c -= '0';
  } else
  if (c >= 'a' && c <= 'f') {
       c -= 'a';
       c += 10;
  } else
  if (c >= 'A' && c <= 'F') {
       c -= 'A';
       c += 10;
  } else return -1;
  return c;
}

static void
process_gps(char *g)
{
    char *cp, *cp2;
    unsigned char sum;
    int i, vs, gps_off;
    double newlong, newlat;
    unsigned char north, east;     // GPS location
    char value[20]; 

    if (gps_off < sizeof(g)) {
      g[gps_off] = 0;
    } else {
      g[sizeof(g)-1]=0;
    }
    gps_off = strlen(g);
    if (gps_off && (g[gps_off-1] == '\n' || g[gps_off-1] == '\r')) {
	g[gps_off-1] = 0;
        gps_off --;
    }
    if (gps_off && (g[0] == '\n' || g[0] == '\r')) {
	g++;
        gps_off --;
    }
    if (gps_off <= 0)
	return;
    if (strncmp(&g[0], "$GPRMC", 6) != 0)  // for the moment we only handle this string, ignore the rest
      return;
    //$GPRMC,002520.00,A,4552.34996,S,17029.01283,E,0.129,,130712,,,A*66
    // 002520 time
    // A OK
    // 4552.34996,S  lat
    // 17029.01283,E long
    // 130712 date
    // *66 sum
    cp = &g[1];
    sum = 0;
    for (i = 0; ;i++) {    // validate GPS string checksum  $DDDDD*CC CC is sum of DD in hex
        if (i >= gps_off)
          goto fail;
        if (*cp == '*') {
	    int v;

            cp++;
            v = to_hex(*cp++);
            if (v < 0)
                goto fail;   
            if (v != ((sum>>4)&0xf))
              goto fail;
            v = to_hex(*cp);
            if (v < 0)
                goto fail;   
            if (v != (sum&0xf))
                goto fail;
            break;
        }
        sum ^= *cp++;
    }
    cp = &g[6];
    while (*cp != ',') {  // skip first ','
       if (*cp == '*') 
         goto fail;
       cp++;
    }
    cp++;
    while (*cp != ',') {// skip time
       if (*cp == '*') 
         goto fail;
       cp++;
    }
    cp++;
    if (*cp != 'A') {// locked?
      pthread_mutex_lock(&gps_mutex);
      gps_lock = 0;
      pthread_mutex_unlock(&gps_mutex);
      goto fail;
    }
    while (*cp != ',') {// skip lock
       if (*cp == '*') 
         goto fail;
       cp++;
    }
    cp++;
    cp2 = &value[0];
    while (*cp != ',') {// read lat
       if (*cp == '*') 
         goto fail;
       if ((*cp >= '0' && *cp <= '9') || *cp == '.') {
           *cp2++ = *cp;
       } else
           goto fail;
       cp++;
    }
    *cp2=0;
    newlat = cvt_gps_to_frac(&value[0]);
    if (vlat <0)
      goto fail;
    cp++;
    if (*cp == 'N') {
        north = 1;
    } else
    if (*cp == 'S') {
        north = 0;
    } else goto fail;
    while (*cp != ',') {// skip N/S
       if (*cp == '*') 
         goto fail;
       cp++;
    }
    cp++;
    cp2 = &value[0];
    while (*cp != ',') {// read long
       if (*cp == '*') 
         goto fail;
       if ((*cp >= '0' && *cp <= '9') || *cp == '.') {
           *cp2++ = *cp;
       } else
           goto fail;
       cp++;
    }
    *cp2=0;
    newlong = cvt_gps_to_frac(&value[0]);
    if (vlong < 0)
      goto fail;
    cp++;
    if (*cp == 'E') {
        east = 1;
    } else
    if (*cp == 'W') {
        east = 0;
    } else goto fail;
    pthread_mutex_lock(&gps_mutex);
    vlong = newlong;
    vlat = newlat;
    gps_lock = 1;
    pthread_mutex_unlock(&gps_mutex);
fail:
    return;
}

static void *
gps_thread(void *p)
{
	int fd;
	FILE *f=0;
	pthread_detach(pthread_self());
	fd = open(GPS_TTY, O_RDONLY); 
	if (fd >= 0) {
    		struct termios options;

    		tcgetattr(fd, &options);
    		cfmakeraw(&options);
    		cfsetspeed(&options, 19200);  	// Baud rate
    		options.c_cflag &= ~CSIZE;
    		options.c_cflag |= CS8;         // 8 bits
    		options.c_cflag &= ~PARENB;     // No parity
    		options.c_cflag &= ~CSTOPB;     // One stop bit
    		options.c_cc[VMIN] = 1;         // Minimum number of chars to read
    		options.c_cc[VTIME] = 0;        // Timeout in 1/10 second units
    		if ( tcsetattr(fd, TCSANOW, &options) < 0 )
			fprintf(stderr, "GPS setup failed - '%s'\n", GPS_TTY);
		f = fdopen(fd, "r");
	}
	if (!f) {
		fprintf(stderr, "Cannot open GPS - '%s'\n", GPS_TTY);
		return 0;
	}
	for (;;) {
		char s[256];
		char *cp = fgets(&s[0], sizeof(s), f);
		if (!cp) {
			fprintf(stderr, "GPS read fails from '%s'\n", GPS_TTY);
			return 0;
		}
		process_gps(&s[0]);
	}
	return 0;
}
void
gps_start(void)
{
	pthread_t tid;
	pthread_create(&tid, 0, gps_thread, 0);
}
