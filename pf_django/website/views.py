from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Uploader, Find
import cv2
import os
from subprocess import run, PIPE
import face_recognition, sys
from .forms import UploadForm, FindForm
from django.contrib import messages


def contactus(request):
    return render(request, 'contact_us.html', {})


def login(request):
    return render(request, './account/login.html', {})


@login_required(login_url='login')
def home(request):
    return render(request, 'home.html', {})


@login_required(login_url='login')
def upload(request):
    if request.method == "POST":
        form = UploadForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            image = request.FILES['image_l']
            img = face_recognition.load_image_file(image)
            if face_recognition.face_locations(img): #form.is_valid() and
                form.save()
            else:
                messages.success(request, 'There is no face detected in your image. So, Please try again with proper image...')
                return render(request, 'upload.html', {})
        else:
            fname_u = request.POST['fname_u']
            lname_u = request.POST['lname_u']
            email_u = request.POST['email_u']
            mobile_u = request.POST['mobile_u']
            messages.success(request, 'There was an error in your form or there is no face in your image!'
                                      ' So, Please try again...')
            return render(request, 'upload.html', {'fname_u': fname_u, 'lname_u': lname_u, 'email_u': email_u, 'mobile_u': mobile_u})
        messages.success(request, 'Thank you for adding! As soon as someone will Find him/her they will contact you.')
        #we can redirect to thank you page from here
        return redirect('home')
    else:
        return render(request, 'upload.html', {})


@login_required(login_url='login')
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
    return render(request, 'find.html', {})


@login_required(login_url='login')
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
                messages.success(request, 'There is no face detected in your image. So, Please try again with proper image...')
                return render(request, 'find.html', {})
        else:
            messages.success(request, 'There was an error in your image! Please try again...')
            return render(request, 'find.html', {})
        #we can redirect to thank you page from here
    else:
        return render(request, 'find.html', {})

    #compare
    image = face_recognition.load_image_file('../images/db/Known/Unknown/0.jpg')
    face_locations = face_recognition.face_locations(image)
    if face_locations:
        out = run([sys.executable, '..//ML//compare_faces.py'], shell=False, stdout=PIPE)
        t1 = out.stdout
        t2 = t1[:-2] #reomve \r\n from byte
        out = t2.decode("utf-8")
        print(out)
        if out != 'No found in data.':
            #messages.success(request, 'Match found.')
            #
            person = Uploader.objects.get(image_l__exact=out+'.jpg')
            person_ = Find.objects.last()
            #
            return render(request, 'Table.html', {'data': person_, 'data1': person})
        else:
            messages.info(request, 'Sorry!! No match found. But you can upload this person by clicking Upload Lost Person given Below.')
            return render(request, 'home.html', {})
    else:
        messages.success(request, 'There is no face in image or maybe image is blur! So please upload a clear image...')
        return render(request, 'find.html', {})
    #return render(request, 'finder.html', {})



