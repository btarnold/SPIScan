from pyramid.response import Response
from pyramid.view import view_config
from random import randint
from .models import Event, DBSession
#from sqlalchemy.exc import DBAPIError
#from .models import (
#    DBSession,
#    MyModel,
#    )
#from pyramid.renderers import get_renderer
import datetime
import subprocess
import time
import pygame
import pygame.camera
#from random import randint

class myView(object):

    def __init__(self, request):
        self.request = request

    def __call__(self):
        return {}    

## no home route is defined, I presume that's why going to root produces 404

    @view_config(renderer="templates/spiscansurveyor.pt", route_name="home")
    def home_view(request):
        return {}

    @view_config(renderer="templates/spiscansurveyor.pt", name="spiscansurveyor.html")
    def index_view(request):
        return {}

    @view_config(renderer="templates/setup.pt", name="setup.html")
    def setup_view(request):
        return {}

    @view_config(renderer="templates/io.pt", name="io.html")
    def io_view(request):
        return {}

    @view_config(renderer="templates/files.pt", name="files.html")
    def files_view(request):
        return {}

    @view_config(renderer="templates/manual.pt", name="manual.html")
    def manual_view(request):
        return {}        
            
    @view_config(renderer="json", name="update")
    def update_view(self):
#    	open("/tmp/hit-update","a").write("update hit on %s\n" % datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S"))
	open("/tmp/hit-update","a").write("scan on %s\n" % datetime.datetime.utcnow())
        e = Event()
        e.spirecord=None
        e.spifileprefix="modtest"
        e.spidate=datetime.datetime.utcnow()
        e.type="spi"
        DBSession.add(e)
#        comtest=subprocess.Popen('', bufsize=0, executable=None, stdin=None, stdout=None, stderr=None, preexec_fn=None, close_fds=False, shell=False, cwd=None, env=None, universal_newlines=False, startupinfo=None, creationflags=0)
        return [
            randint(0,100),
            randint(0,100),
            randint(0,100),
            randint(0,100),
            888,
        ]
        
    @view_config(renderer="json", name="camcapture")
    def camcapture_view(self):
	cmdkill = "bash /home/brian/DspaceSPI/SPIScan/mjpg-streamer/killmjpg.sh"
	cmdlostart = "bash /home/brian/DspaceSPI/SPIScan/mjpg-streamer/lostart.sh"
	cmdhistart = "bash /home/brian/DspaceSPI/SPIScan/mjpg-streamer/histart.sh"
	cmdframegrab = "bash /home/brian/DspaceSPI/SPIScan/mjpg-streamer/framegrab.sh"
	subprocess.call(cmdkill, shell=True)
        time.sleep(0.5)
#	subprocess.call(cmdhistart, shell=True)
	pygame.camera.init()
	cam = pygame.camera.Camera("/dev/video1",(1920,1080))
	cam.start()
	img = cam.get_image()
	pygame.image.save(img,"/home/brian/DspaceSPI/SPIScan/mjpg-streamer/captures/capture.jpg")
	time.sleep(2)
	cam.stop()
#	subprocess.call(cmdkill, shell=True)
	time.sleep(1)
	subprocess.call(cmdlostart, shell=True)
#	open("/tmp/capture","a").write("frame grab on %s\n" % datetime.datetime.utcnow())
        ev = Event()
        ev.spirecord=None
        ev.spifileprefix="desktest"
        ev.spidate=datetime.datetime.utcnow()
        ev.type="cameraframe"
        DBSession.add(ev)
	return []
