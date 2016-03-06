#this is a cherry py script for interacting between the webpage and the arduino through Firmata protocol.
import cherrypy
import spi_firmata
import os
import json

def strToFunction(str):
    if(str == 'lazers_toggle'):
        spi_firmata.lazers_toggle()
    elif(str == 'pump1_toggle'):
        spi_firmata.pump1_toggle()
    elif(str == 'pump2_toggle'):
        spi_firmata.pump2_toggle()
    elif(str.split()[0] == 'pwmLED'):
        spi_firmata.pwmLED(int(str.split()[1]))
    return json.dumps({'message':str, 'type':'success'})

class ArduinoWebService(object):
    exposed = True

    @cherrypy.tools.accept(media='text/plain')
    def POST(self, callString):
        return strToFunction(callString)


def CORS():
  cherrypy.response.headers["Access-Control-Allow-Origin"] = "*"


if __name__ == '__main__':
    conf = {
        '/': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.sessions.on': True,
            'tools.response_headers.on': True,
            'tools.response_headers.headers': [('Content-Type', 'text/plain')],
            'tools.CORS.on': True,
        }
    }
    cherrypy.config.update({'server.socket_host': '129.65.26.196',
                         'server.socket_port': 9999,
                        })
    cherrypy.tools.CORS = cherrypy.Tool('before_handler', CORS)
    os.system('chmod 777 /dev/ttyACM0')
    spi_firmata.init()
    spi_firmata.lazers_toggle(0)
    spi_firmata.pump1_toggle(0)
    spi_firmata.pump2_toggle(0)
    spi_firmata.pwmLED(0)
    cherrypy.quickstart(ArduinoWebService(), '/', conf)
