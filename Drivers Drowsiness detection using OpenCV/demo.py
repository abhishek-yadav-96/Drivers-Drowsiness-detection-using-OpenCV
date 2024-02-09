from flask import Flask, render_template, request, jsonify
import cv2
import dlib

app = Flask(__name__)

# Load dlib's face detector and facial landmarks predictor
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')

# Load the drowsiness detection model or implement your own logic

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/detect_drowsiness', methods=['POST'])
def detect_drowsiness():
    # Get the image data from the frontend
    image_data = request.json['image']
    
    # Convert base64 image data to OpenCV format
    nparr = np.frombuffer(base64.b64decode(image_data), np.uint8)
    image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    
    # Convert the image to grayscale for dlib processing
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale image
    faces = detector(gray)

    for face in faces:
        # Perform facial landmarks detection
        landmarks = predictor(gray, face)

        # Implement your drowsiness detection logic using the facial landmarks
        
        # Dummy response for testing purposes
        response = {'drowsy': False}
        return jsonify(response)

if __name__ == '__main__':
    app.run(port=110000)
