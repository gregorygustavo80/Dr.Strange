# Hand Gesture Control using MediaPipe and Python

>This project allows controlling computer functions using hand gestures detected through the MediaPipe library in Python. It includes features such as screen capture, volume control, opening applications, and other simple actions using specific gestures recognized by the camera.

## Pré-requisitos
Make sure you have Python installed on your system.

The script will automatically install the following Python libraries:

+ OpenCV (cv2)
+ MediaPipe
+ PyAutoGUI
+ PyCaw
+ Comtypes
  
## Features

### Screen Capture

### Recognized Gestures: Closed Fist
>Action: Captures a specified area of the screen. Equivalent to Win + Shift + s command.

### Volume Control

>Extended index finger upwards.
Action: Increases the system volume.

### Mute

>V sign (index and middle fingers extended upwards).
Action: Mutes the system volume.

### WhatsApp Web Opening

>Hello sign in sign language (little finger raised).
Action: Opens WhatsApp Web in the default browser.

## Usage
Run the script Dr.Strange.py after installing the dependencies.
Ensure your camera is working correctly as the program will use it to detect hand gestures
````
python Dr.Strange.py 
````
## How It Works
The script uses the computer's camera to capture real-time video.
It utilizes the MediaPipe library to detect hands and recognize specific gestures based on hand landmarks' positions.
Depending on the recognized gesture, a corresponding action is performed (e.g., screen capture, volume adjustment, etc.).

## Contributions
Contributions are welcome! Feel free to fork the project, make improvements, and submit a pull request. If you encounter issues, please open an issue.


