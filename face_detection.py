import cv2

vid=cv2.VideoCapture(0)
#Don't forget to use \\ when specifying the file path
face_cascade = cv2.CascadeClassifier('file_path.xml')

while(True):
    ret, frame = vid.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray,1.3,5)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    for(x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),3)

    cv2.imshow('Face Detetection Application',frame)
    
    
vid.release()
cv2.destroyAllWindows()