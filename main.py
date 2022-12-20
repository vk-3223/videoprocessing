import cv2

video = cv2.VideoCapture("HERE_YOUR_VIDEO")
success,frame = video.read()
height = frame.shape[0]
width = frame.shape[1]
output = cv2.VideoWriter('output.avi',cv2.VideoWriter_fourcc(*'DIVX'),30,(width,height))

face_classifier = cv2.CascadeClassifier(r"HERE_YOUR_cascade_classifier_file_path")

while success:
    face = face_classifier.detectMultiScale(frame,1.1,4)
    for x,y,w,h in face:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,255),4)
       
    output.write(frame)
    success,frame = video.read()
    if success is True:
        frame[y:y+h,x:x+w] = cv2.blur(frame[y:y+h,x:x+w],(50,50))
  
output.release()