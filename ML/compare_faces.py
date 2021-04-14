import subprocess
import sys
import face_recognition
import cv2
import os
import numpy as np


def read_img(path):
    img = cv2.imread(path)
    (h, w) = img.shape[:2]
    width = 500
    ratio = width / float(w)
    height = int(h * ratio)
    return cv2.resize(img, (width, height))


Known_encodings = []
known_names = []
known_dir = '..//images//Known'
for file in os.listdir(known_dir):
    img = read_img(known_dir + '/' + file)
    img_enc = face_recognition.face_encodings(img)[0]
    Known_encodings.append(img_enc)
    known_names.append(file.split('.')[0])

flag = False
Unknown_dir = '..//images//Unknown'
for file in os.listdir(Unknown_dir):
    img = read_img(Unknown_dir + '/' + file)
    img_enc = face_recognition.face_encodings(img)[0]
    results = face_recognition.compare_faces(Known_encodings, img_enc, tolerance=0.47)

    for i in range(len(results)):
        if results[i]:
            print(known_names[i])
            flag = True

if not flag:
    print('No found in data.')
