import cv2

# Load the Haar cascade file for face detection
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

status, image = cap.read()
cap.release()

if status:

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Loop over the detected faces
    for (x, y, w, h) in faces:
        # Crop the face
        face = image[y:y+h, x:x+w]
        
        # Place the cropped face back on the original image (in a specific position)
        image[0:face.shape[0], 0:face.shape[1]] = face  # Adjust the position as needed
        

    # Display the output image
    cv2.imshow('Image with Cropped Face', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
