import cv2
from cvzone.HandTrackingModule import HandDetector
from AccessAudio import Volume

def DetectNumber(image):
    handModel=HandDetector(maxHands=1)
    hand,image=handModel.findHands(image)
        ##############################
        ### If Hand Is Detected ######
        ############################## 
    if hand:
        FingerDetect=handModel.fingersUp(hand[0])
        if FingerDetect==[0,1,0,0,0]: number=1
        elif FingerDetect==[0,1,1,0,0]: number=2
        elif FingerDetect==[0,1,1,1,0]: number=3
        elif FingerDetect==[0,1,1,1,1]: number=4
        elif FingerDetect==[1,1,1,1,1]: number=5
        elif FingerDetect==[1,0,0,0,0]: number=6
        elif FingerDetect==[1,1,0,0,0]: number=7
        elif FingerDetect==[1,0,1,0,0]: number=8
        elif FingerDetect==[1,0,0,1,0]: number=9
        elif FingerDetect==[1,0,0,0,1]: number=10
        else: number=0
            
            ###########################################
            #######Increase or Decrease Volume#########
            ###########################################
        Volume(number)
        cv2.putText(image,f'DetectNumber:{number}',(20,80),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),2)
    
    return image
        
