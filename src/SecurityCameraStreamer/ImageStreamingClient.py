'''
Created on Sep 12, 2013

@author: noel.oconnor@gmail.com
'''

import requests
import Image
from StringIO import StringIO


class ImageStreamer(object):
    '''
    classdocs
    '''


    def __init__(self):
        self.imgCount = 0
        self.payloadResult = ''
        self.startHDR = None
        self.endHDR = None
        self.startHDRFound = False
        self.endHDRFound = False



    def retrieveImage(self):
        r = requests.get("http://192.168.1.170/videostream.cgi?rate=0&user=admin&pwd=yearight", stream=True)
        for data in r.iter_content(1000):
        #     print "loading data"
            self.payloadResult += data
        
            if not self.startHDRFound:
                startHDR = self.payloadResult.find("\377\330")
            else:
                pass
                
            if startHDR != -1:
                startHDRFound = True
        #         print "Start Header found @ %d" % startHDR
        
                if not self.endHDRFound:
                    endHDR = self.payloadResult.find("\377\331")
                else:
                    pass
                    
                if endHDR != -1:
                    endHDRFound = True
        #             print "End Header found @ %d out of %d" % (endHDR, len(payloadResult))
                    
                    imgPayload = self.payloadResult[startHDR:endHDR]
                         
        
                    resImage = Image.open(StringIO(imgPayload))
                    
                    yield resImage
        #             f = open(str((imgCount%10)+1) + 'workfile.jpg', 'wb')
        #             f.write(imgPayload)
        #             f.close
                    
                    tmpPayloadResult = self.payloadResult[endHDR + 1:]
        #             print "left with %d bytes in the buffer" % len(tmpPayloadResult)
                    
                    payloadResult = tmpPayloadResult[:]
                    
                    startHDRFound = False
                    endHDRFound = False
                    startHDR = None
                    endHDR = None
                else:
                    pass
            else:
                pass
                
            
        


 
    

            
