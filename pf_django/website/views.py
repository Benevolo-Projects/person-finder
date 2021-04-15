from django.shortcuts import render, redirect
from .models import Uploader
import cv2
import os
from subprocess import run, PIPE
import face_recognition, sys
from .forms import UploadForm, FindForm
from django.contrib import messages


def home(request):
    return render(request, 'home.html', {})


def upload(request):
    if request.method == "POST":
        form = UploadForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            image = request.FILES['image_l']
            img = face_recognition.load_image_file(image)
            if face_recognition.face_locations(img): #form.is_valid() and
                form.save()
            else:
                messages.success(request, 'There is no face detected in you image So, Please try again...')
                return render(request, 'upload.html', {})
        else:
            fname_u = request.POST['fname_u']
            lname_u = request.POST['lname_u']
            email_u = request.POST['email_u']
            mobile_u = request.POST['mobile_u']
            messages.success(request, 'There was an error in your form or the is no face in your image!'
                                      ' So, Please try again...')
            return render(request, 'upload.html', {'fname_u': fname_u, 'lname_u': lname_u, 'email_u': email_u, 'mobile_u': mobile_u})
        messages.success(request, 'Thank you for adding, as soon as some one will match he/she will contact you.')
        #we can redirect to thank you page from here
        return redirect('home')
    else:
        return render(request, 'upload.html', {})


def find(request):

    """if request.method == "POST":
        form = UploadForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
        else:
            image = request.POST['image']
            messages.success(request, 'There was an error in your form! Please try again...')
            return render(request, 'upload.html', {'image': image})
        messages.success(request, 'Your photo is taken.')
        #we can redirect to thank you page from here
    else:
        return render(request, 'finder.html', {})"""
    return render(request, 'finder.html', {})


def comp(request):
    #upload
    if request.method == "POST":
        form = FindForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            fet_img = request.FILES['image']
            img = face_recognition.load_image_file(fet_img)
            if face_recognition.face_locations(img):  # form.is_valid() and
                form.save()
            else:
                messages.success(request, 'There is no face detected in you image So, Please try again...')
                return render(request, 'finder.html', {})
        else:
            messages.success(request, 'There was an error in your image! Please try again...')
            return render(request, 'finder.html', {})
        #we can redirect to thank you page from here
    else:
        return render(request, 'finder.html', {})

    #compare
    image = face_recognition.load_image_file('../images/db/Known/Unknown/0.jpg')
    face_locations = face_recognition.face_locations(image)
    if face_locations:
        out = run([sys.executable, '..//ML//compare_faces.py'], shell=False, stdout=PIPE)
        out = out.stdout.decode("utf-8")
        print(out)
        if out != 'No found in data.\r\n':
            messages.success(request, 'Match found.')
            return render(request, 'finder.html', {'data1': out})
        else:
            messages.info(request, 'Sorry!! no person found')
            return render(request, 'home.html', {})
    else:
        messages.success(request, 'There is no face in image or maybe image is blur! so please upload it again...')
        return render(request, 'finder.html', {})
    #return render(request, 'finder.html', {})



