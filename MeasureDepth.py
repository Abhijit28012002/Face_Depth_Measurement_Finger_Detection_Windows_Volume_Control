import cv2
from cvzone.FaceMeshModule import FaceMeshDetector
from HandTracking import DetectNumber

cap=cv2.VideoCapture(0)
detector=FaceMeshDetector(maxFaces=1)

while True:
    status,img=cap.read()
    cv2.rectangle(img,(0,0),(300,100),(0,255,0),cv2.FILLED)

    ######################################################
    ############ count No. of Up Finger ##################
    ###### And Increase OR Decrease Windows Volume #######
    ######################################################

    img=DetectNumber(img)


    img,faces=detector.findFaceMesh(img,draw=False)
    
    if faces:
        face=faces[0]
        pointLeft=face[145]
        pointRight=face[374]
        
        w,_=detector.findDistance(pointLeft,pointRight)
        W=6.3

        # Finding Distance
        f=720
        d=(W*f)/w
        #print(d)
        cv2.putText(img,f'Depth: {int(d)}cm',(20,40),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),2)
        

    cv2.imshow("Output",img)
    if cv2.waitKey(100)==13:
        break
cv2.destroyAllWindows()
cap.release()