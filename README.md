# Drivers-Drowsiness-detection-using-OpenCV

The Driver Drowsiness Detection System is an advanced AI-based application designed to monitor drivers for signs of fatigue and prevent accidents caused by drowsiness. The system leverages computer vision techniques to analyze real-time video streams, detect facial landmarks, and assess driver alertness. By implementing machine learning and deep learning algorithms, it can identify key indicators of drowsiness such as eye closure, yawning, and head tilts. The system raises alarms when the driver shows signs of drowsiness to enhance road safety.

Technologies Used:
OpenCV: A powerful open-source computer vision library used to capture video streams and process images. OpenCV is utilized for real-time face detection and tracking.
dlib: A machine learning library used for facial landmark detection. It identifies critical facial points like the eyes, mouth, and nose, enabling accurate recognition of drowsiness indicators.
Flask: A lightweight web framework used to build the back-end of the application, allowing the system to run as a web service. Flask handles the integration of the detection module and the user interface.
Key Features:
Facial Landmark Detection: The system detects and tracks the driver’s face using dlib’s facial landmark detector, focusing on specific points such as the eyes, mouth, and head position.
Drowsiness Detection Algorithm: The system calculates the Eye Aspect Ratio (EAR) and Mouth Aspect Ratio (MAR) using the detected facial landmarks. If the EAR remains low (indicating closed eyes) or the MAR is high (indicating yawning) for a sustained period, the system triggers an alert.
Real-time Video Analysis: OpenCV captures live video from a camera and processes it in real-time to constantly monitor the driver's behavior.
Alerts: The system raises visual and/or auditory alarms when drowsiness indicators are detected to prompt the driver to stay alert or take a break.
Web Interface: The Flask-based web interface allows users to control and monitor the system remotely, making it easy to deploy in various environments.
Applications:
Transportation Industry: Enhances driver safety in commercial vehicles, reducing accidents caused by driver fatigue.
Automotive Integration: Can be integrated into vehicles as a safety feature for personal and commercial use.
Research: Useful for studying driver behavior and testing various algorithms in real-time environments.
