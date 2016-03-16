import gps
import call from subprocess

#init gps module with command line: sudo gpsd /dev/ttyUSB0 -F /var/run/gpsd.sock

def init():
	call("gpsd /dev/ttyUSB0 -F /var/run/gpsd.sock", shell=True)

def get_longitude(): 

	# Listen on port 2947 (gpsd) of localhost
	session = gps.gps("localhost", "2947")
	session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)

	while True:  
    		try:
    			report = session.next()
			# Wait for a 'TPV' report and display the current time
			# To see all report data, uncomment the line below
			
			if report['class'] == 'TPV':
        			if hasattr(report, 'lon'):
           				return report.lon
    		except KeyError:
			pass
    		except KeyboardInterrupt:
			quit()
    		except StopIteration:
			session = None
			print "GPSD has terminated"

def get_latitude(): 
	# Listen on port 2947 (gpsd) of localhost
	session = gps.gps("localhost", "2947")
	session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)

	while True:  
    		try:
    			report = session.next()
			# Wait for a 'TPV' report and display the current time
			# To see all report data, uncomment the line below

			if report['class'] == 'TPV':
        			if hasattr(report, 'lat'):
           				return report.lat
    		except KeyError:
			pass
    		except KeyboardInterrupt:
			quit()
    		except StopIteration:
			session = None
			print "GPSD has terminated"

def get_time(): 
	# Listen on port 2947 (gpsd) of localhost
	session = gps.gps("localhost", "2947")
	session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)

	while True:  
    		try:
    			report = session.next()
			# Wait for a 'TPV' report and display the current time
			# To see all report data, uncomment the line below

			if report['class'] == 'TPV':
        			if hasattr(report, 'time'):
           				return report.time
    		except KeyError:
			pass
    		except KeyboardInterrupt:
			quit()
    		except StopIteration:
			session = None
			print "GPSD has terminated"




