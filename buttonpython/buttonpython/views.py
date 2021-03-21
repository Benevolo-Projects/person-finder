from django.shortcuts import render
import requests
from subprocess import run, PIPE
import sys

import face_recognition


def home(request):
    return render(request, 'home.html')


def face_check_redirect(request):
    return render(request, 'finder.html')


def upload(request):
    return render(request, 'upload.html')


def face_ckeck(request):
    image = face_recognition.load_image_file("E://6th sem//SGP//Unknown//1.jpeg")
    face_locations = face_recognition.face_locations(image)
    if face_locations:
        # print(1)
        out = run([sys.executable, 'E://6th sem//SGP//ML//compare_faces.py'], shell=False, stdout=PIPE)
        print(out)
        return render(request, 'finder.html', {'data1': out.stdout})
    else:
        return render(request, 'finder.html', {'data1': 'Face not found'})
        # print(0)


'''
def external(request):
    # inp = request.POST.get('param')
    out = run([sys.executable, 'E://6th sem//SGP//ML//compare_faces.py'], shell=False, stdout=PIPE)
    print(out)

    return render(request, 'finder.html', {'data1': out.stdout})

'''
'''
import face_recognition

image = face_recognition.load_image_file("E://6th sem//SGP//Unknown_test_images//Krish_test.jpg")

face_locations = face_recognition.face_locations(image)


if face_locations:
    print(1)
else:
    print(0)
'''
