#!/bin/bash
echo
cd /home/brian/DspaceSPI/SPIScan/mjpg-streamer
./mjpg_streamer -i "./input_uvc.so -d /dev/video1 -r 1920x1080 -f 1 -y" -o "./output_file.so -f ./captures -s 1 -d 10000" 
#./mjpg_streamer -i "./input_uvc.so -d /dev/video1 -r 1920x1080 -f 1 -y" -o "./output_http.so -p 8090 -w ./www" 

