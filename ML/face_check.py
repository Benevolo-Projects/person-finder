import face_recognition

image = face_recognition.load_image_file("../images/Unknown_test_images/1.jpeg")

face_locations = face_recognition.face_locations(image)


if face_locations:
    print(1)
else:
    print(0)