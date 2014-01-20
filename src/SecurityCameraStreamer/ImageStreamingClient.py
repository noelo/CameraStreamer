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


    def __init__(self,streamURL=None,snapshotURL=None):
        self.streamURL = None
        self.snapshotURL = None
        
        
    def configCamera(self):
        # Turn on outdoor mode
        x = requests.get('http://192.168.1.170/camera_control.cgi?param=3&value=2&user=admin&pwd=password')  
        if x.status_code != 200: raise Exception('Unable to turn on outdoor mode, status = ' + x.status_code)
        
        # Turn on infrared mode   
        x =  x = requests.get('http://192.168.1.170/set_misc.cgi?led_mode=2&user=admin&pwd=password')
        if x.status_code != 200: raise Exception('Unable to turn on infrared mode, status = ' + x.status_code)
        


    def retrieveImageStream(self):
        payloadResult = ''
        startHDR = None
        endHDR = None
        startHDRFound = False
        endHDRFound = False
        
        r = requests.get(self.streamURL, stream=True)
        for data in r.iter_content(1000):

            payloadResult += data
        
            if not startHDRFound:
                startHDR = payloadResult.find("\377\330")
            else:
                pass
                
            if startHDR != -1:
                startHDRFound = True
        
                if not endHDRFound:
                    endHDR = payloadResult.find("\377\331")
                else:
                    pass
                    
                if endHDR != -1:
                    endHDRFound = True
                    
                    imgPayload = payloadResult[startHDR:endHDR]
                         
        
#                     resImage = Image.open(StringIO(imgPayload))

                    
                    yield StringIO(imgPayload)
#                     f = open(str((imgCount%10)+1) + 'workfile.jpg', 'wb')
#                     f.write(imgPayload)
#                     f.close
                    
                    tmpPayloadResult = payloadResult[endHDR + 1:]
                    
                    payloadResult = tmpPayloadResult[:]
                    
                    startHDRFound = False
                    endHDRFound = False
                    startHDR = None
                    endHDR = None
                else:
                    pass
            else:
                pass
            
    def retrieveImageSnapshot(self):
        r = requests.get(self.snapshotURL, stream=False)
        
        if r.status_code == 200:
            res = StringIO(r.content)
#             res =  Image.open(StringIO(r.content))
#             f = open('workfile.jpg', 'wb')
#             f.write(r.content)
#             f.close
            return res
        else:
            raise Exception("NOK response from Camera ["+r.status_code+"]")
            
                
            
        


 
    

            
