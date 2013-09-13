'''
Created on Sep 12, 2013

@author: admin
'''

from SecurityCameraStreamer import ImageStreamingClient

if __name__ == '__main__':
    x= ImageStreamingClient.ImageStreamer()
    for z in x.retrieveImage():
        print "Im herererere "+str(z)
