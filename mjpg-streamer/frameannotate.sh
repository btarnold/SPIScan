#!/bin/bash
echo
cd /home/brian/DspaceSPI/SPIScan/mjpg-streamer/captures
convert /home/brian/DspaceSPI/SPIScan/mjpg-streamer/captures/capture.jpg -background White -pointsize 42 label:'Date'  -gravity Center -append /home/brian/DspaceSPI/SPIScan/mjpg-streamer/captures/anno_label.jpg
