import cv2
import winsound
cam = cv2.VideoCapture(0)

while cam.isOpened():

    cv2.namedWindow("Video", cv2.WINDOW_NORMAL)
    cv2.setWindowProperty("Video", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    ret, frame1 = cam.read()
    ret, frame2 = cam.read()

    frame1 = cv2.putText(frame1, 'LIVE...', (5, 20),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255,255,255), 1)

    diff = cv2.absdiff(frame1,frame2)
    gray = cv2.cvtColor(diff,cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(gray,(5,5),0)
    _, thresh = cv2.threshold(blur,20,255,cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh,None,iterations=3)
    contours,_ = cv2.findContours(dilated,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for c in contours:
        if cv2.contourArea(c) <2000:
            continue
        area = cv2.contourArea(c) 
        winsound.PlaySound("alarm.wav",winsound.SND_ASYNC)
        winsound.Beep(500,100)
        x,y,w,h = cv2.boundingRect(c)
        cv2.rectangle(frame1,(x,y),(x+w, y+h) , (00, 200, 200),2 )
        cv2.putText(frame1,"Suspect"+str(area), (x, y), 
        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 255), 2) 



# For printing text

    # cv2.drawContours(frame1,contours,-1,(0,255,0),2)
    if cv2.waitKey(10) == ord("q"):
        break
    cv2.imshow("Video",frame1)