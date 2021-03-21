import face_recognition

image = face_recognition.load_image_file("E://6th sem//SGP//Unknown_test_images//Krish_test.jpg")

face_locations = face_recognition.face_locations(image)


if face_locations:
    print(1)
else:
    print(0)