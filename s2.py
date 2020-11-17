import os
import sys

source = sys.argv[1]
operation = sys.argv[2]
order = ""

if operation[:3] == "cut":
    start = operation[3:5]
    time = operation[5:]
    order = "ffmpeg -i {} -ss 00:00:{} -t 00:00:{} {}cut.mp4".format(source, start, time, source[:-4])

elif operation == "histogram":
    order = 'ffmpeg -i {} -vf "split=2[a][b],[b]histogram[hh],[a][hh]overlay" {}_histogram.mp4'.format(source,source[:-4])

elif operation[:6] == "resize":
    if operation[-3:] == "720":
        w = 1280
        h = 720
    elif operation[-3:]=="480":
        w = 640
        h = 480
    elif operation[-3:]=="240":
        w = 360
        h = 240
    elif operation [-3:]=="120":
        w = 160
        h = 120
    else:
        print("Size not valid for this operation")
    order = 'ffmpeg -i {} -vf scale={}:{} {}_{}x{}.mp4'.format(source, w, h, source[:-4],w,h)

elif operation == "mono":
    order = "ffmpeg -i {} -ac 1 {}_mono.mp4".format(source, source[:-4])

elif operation == "aac":
    order = "ffmpeg -i {} -c:v copy -c:a libfdk_aac -vbr 3 {}_aac.mp4".format(source, source[:-4])

else:
    print("Invalid requested operation")

os.system(order)
