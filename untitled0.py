import cv2
face = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
nose = cv2.CascadeClassifier('haarcascade_mcs_nose.xml')
font=cv2.FONT_HERSHEY_COMPLEX
video_capture = cv2.VideoCapture(0)
while True:
    ret, frame = video_capture.read()
    faces = face.detectMultiScale(frame)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        cv2.rectangle(frame, (x,y-40),(x+w, y), (50,50,255),-2)
        Nose = nose.detectMultiScale( frame)
        if Nose ==() :
            cv2.putText(frame, " mask",(x,y-10), font, 0.75, (255,255,255),1)
            print(Nose)
        else :
            cv2.putText(frame, "no mask",(x,y-10), font, 0.75, (255,255,255),1)
            print(faces)
    cv2.imshow('Video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video_capture.release()
cv2.destroyAllWindows()