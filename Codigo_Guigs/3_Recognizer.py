import cv2
import numpy as np
import os
import pandas as pd

def count_appearance(id):
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    user_dir = os.path.join(BASE_DIR, "users.csv")
    df = pd.read_csv(user_dir)
    df.iat[id-1,2] +=1
    df.to_csv(user_dir, index=False)

def count_smile(id):
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    user_dir = os.path.join(BASE_DIR, "users.csv")
    df = pd.read_csv(user_dir)
    df.iat[id-1,3] +=1
    df.to_csv(user_dir, index=False)

def Recognize():

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    cascade_dir = os.path.join(BASE_DIR, "cascades/haarcascade_frontalface_default.xml")
    smile_dir = os.path.join(BASE_DIR, "cascades/haarcascade_smile.xml")
    trainer_dir = os.path.join(BASE_DIR, "trainer/trainer.yml")


    recognizer = cv2.face.LBPHFaceRecognizer_create()

    recognizer.read(trainer_dir)
    faceCascade = cv2.CascadeClassifier(cascade_dir)
    smile_cascade = cv2.CascadeClassifier(smile_dir)

    font = cv2.FONT_HERSHEY_SIMPLEX
    # init id counter
    id_counter = 0

    # names related to ids: example ==> Marcelo: id=1,  etc
    user_dir=os.path.join(BASE_DIR, "users.csv")
    df = pd.read_csv(user_dir)
    names = df['Name'].tolist()
    # Initialize and start realtime video capture
    cam = cv2.VideoCapture(0)
    cam.set(3, 640)  # set video widht
    cam.set(4, 480)  # set video height
    # Define min window size to be recognized as a face
    minW = 0.2 * cam.get(3)
    minH = 0.2 * cam.get(4)

    flag_appearance=[0]*len(names)
    flag_smile=[0]*len(names)

    # Let's start the loop
    while True:
        ret, img = cam.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.2,
            minNeighbors=5,
            minSize=(int(minW), int(minH)),
        )
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            id_counter, confidence = recognizer.predict(gray[y:y + h, x:x + w])

            # Let's find the smiles
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = img[y:y + h, x:x + w]
            smiles = smile_cascade.detectMultiScale(roi_gray, 1.85, 20, minSize=(5,5))
            for (sx, sy, sw, sh) in smiles:
                cv2.rectangle(roi_color, (sx, sy), ((sx + sw), (sy + sh)), (0, 0, 255), 3)
                if flag_smile[id_counter-1]==0:
                    count_smile(id_counter)
                    flag_smile[id_counter-1]=1

            # If we find a match
            if confidence > 70:
                id = names[id_counter - 1]
                confidence = "  {0}%".format(round(confidence))
                if flag_appearance[id_counter-1]==0:
                    count_appearance(id_counter)
                    flag_appearance[id_counter-1]=1

            # If we cannot identify the person
            else:
                id = "unknown"
                confidence = "  {0}%".format(round(confidence))

            cv2.putText(img, str(id), (x + 5, y - 5), font, 1, (255, 255, 255), 2)
            cv2.putText(img, str(confidence), (x + 5, y + h - 5), font, 1, (255, 255, 0), 1)

        cv2.imshow('camera', img)
        k = cv2.waitKey(10) & 0xff  # Press 'ESC' for exiting video
        if k == 27:
            break
    # Do a bit of cleanup
    print("\n [INFO] Exiting Program and cleanup stuff")
    cam.release()
    cv2.destroyAllWindows()

