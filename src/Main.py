'''
Created on Sep 12, 2013

@author: admin
'''

from SecurityCameraStreamer import ImageStreamingClient
import time
import Image

if __name__ == '__main__':
    x= ImageStreamingClient.ImageStreamer()
    x.configCamera()
    x.streamURL = "http://192.168.1.170/videostream.cgi?rate=0&user=admin&pwd=password"
    x.snapshotURL = "http://192.168.1.170/snapshot.cgi?user=admin&pwd=password"
    imgCount = 0
    
    for z in x.retrieveImageStream():
        resImage = Image.open(z)
        print "Im herererere "+str(resImage) 
        time.sleep(5)
        
#     res = x.retrieveImageSnapshot()
#     resImage = Image.open(res)
#     resImage.show
