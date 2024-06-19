Face Recognition System with Real-Time Database


This project implements a face recognition system using Python, OpenCV, face-recognition, dlib, and Firebase Realtime Database. The system detects faces in real-time through a webcam or video stream, recognizes known faces, and updates their attendance status in a Firebase database.

Features
Face Detection: Utilizes OpenCV and dlib for real-time face detection.
Face Recognition: Recognizes faces using the face-recognition library.
Firebase Integration: Stores recognized faces and attendance records in Firebase Realtime Database.
Real-Time Updates: Attendance status is updated in real-time in the Firebase database.
Requirements
Python 3.x
OpenCV
face-recognition
dlib
firebase-database
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/your-username/face-recognition-system.git
Install dependencies:

Copy code
pip install -r requirements.txt
Set up Firebase:

Create a Firebase project at Firebase Console.
Add a Realtime Database to your project.
Generate a service account key (JSON format) in Firebase settings and save it securely.
Rename the downloaded JSON file to firebase_key.json and place it in the project root directory.
Usage
Run the application:

css
Copy code
python main.py
The application will start capturing video from the default webcam.

Recognized faces will be annotated with names if they match the known faces stored in the Firebase database.

The attendance of recognized faces will be automatically updated in the Firebase Realtime Database.

Configuration
You can adjust settings such as face recognition model, confidence threshold, and Firebase database URL in config.py.
Contributing
Contributions are welcome! If you'd like to add new features, improve existing ones, or fix issues, feel free to send a pull request.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
Thanks to the developers of OpenCV, dlib, face-recognition, and Firebase for their powerful libraries and services.
Feel free to modify the sections and details as per your specific project structure and additional features. This README provides a solid foundation to help users understand your face recognition system and get started with it.


