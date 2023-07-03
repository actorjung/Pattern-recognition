from django.shortcuts import render
from django.views.decorators import gzip
from django.http import StreamingHttpResponse
import cv2
import threading
import dlib
from PIL import Image
import numpy as np
from imutils import face_utils
from keras.models import load_model
import tensorflow as tf
from . import models
from .models import SongUrl
from django.db import connection
import random

def home(request):
    return render(request,'home.html')

def index(request):
    return render(request,'index.html')

def detect(request):
    return render(request,'detect.html')

def uploadFile(request):
    if request.method == "POST":
        # Fetching the form data
        fileTitle = request.POST["fileTitle"]
        uploadedFile = request.FILES["uploadedFile"]

        # Saving the information in the database
        document = models.Document(
            title = fileTitle,
            uploadedFile = uploadedFile
        )
        document.save()

    documents = models.Document.objects.all()

    return render(request, "upload.html", context = {
        "files": documents
    })

class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)
        (self.grabbed,self.frame) = self.video.read()
        threading.Thread(target=self.update, args=()).start()

    def __del__(self):
        self.video.release()

    def get_frame(self):
        image = self.frame
        _, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()

    def update(self):
        while True:
            (self.grabbed, self.frame) = self.video.read()


def gen(camera):
    while True:
        frame = camera.get_frame()
        yield(b'--frame\r\n'
              b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


@gzip.gzip_page
def detectme(request):
    try:
        cam = VideoCamera()
        if cv2.waitKey(1) == ord('q') :  # q
            cv2.imwrite("C:/user/woosung/capture/cap01" + ".png", cam)
        return StreamingHttpResponse(gen(cam),content_type="multipart/x-mixed-replace;boundary=frame")
    except:
        print("에러입니다...")
        pass

def result(request):
    detector = dlib.get_frontal_face_detector()
    emotion_model = load_model('model/model_keras2.h5')
    emotion_dict = {
        0: 'Angry',
        1: 'Happy',
        2: 'Neutral',
        3: 'Sad',
    }
    # Grab a single frame of video
    frame = cv2.imread('media/Uploaded Files/img.jpg')

    # Convert the image from BGR color (which OpenCV uses) to RGB color
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Find all the faces in the current frame of video
    face_locations = detector(rgb_frame)

    # Draw a box around the face
    for f in face_locations:
        cv2.rectangle(frame, (f.left(), f.top()), (f.right(), f.bottom()), (0, 0, 255), 2)

        crop = rgb_frame[f.top():f.bottom(), f.left():f.right()]
        crop_img = np.array(Image.fromarray(crop).resize([48, 48]))
        crop_img = crop_img.reshape((1, 48, 48, 3))
        emotion_preds = emotion_model.predict(crop_img)

        cv2.putText(frame, 'Emotion: {}({:.3f})'.format(emotion_dict[np.argmax(emotion_preds)], np.max(emotion_preds)),
                    (f.left(), f.top() - 40), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (36, 255, 12), 1)
    cv2.imwrite("static/img/result.jpg", frame)
    if np.argmax(emotion_preds) == 0:
        emotion = "angry"
    elif np.argmax(emotion_preds) == 1:
        emotion = "happy"
    elif np.argmax(emotion_preds) == 2:
        emotion = "netural"
    else :
        emotion = "sadup"

    a = SongUrl.objects.filter(tags=emotion).order_by('?')[:5]


    return render(request,'result.html',{ "emotion":emotion,'a': a })

def playlist(request):

    b = SongUrl.objects.filter(tags="saddown").order_by('?')[:5]

    return render(request,'playlist.html',{"b":b})
