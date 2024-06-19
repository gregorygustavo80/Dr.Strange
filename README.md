# Hand Gesture Control using MediaPipe and Python

>This project allows controlling computer functions using hand gestures detected through the MediaPipe library in Python. It includes features such as screen capture, volume control, opening applications, and other simple actions using specific gestures recognized by the camera.

## Requeriments
Make sure you have Python installed on your system.

The script will automatically install the following Python libraries:

+ OpenCV (cv2)
+ MediaPipe
+ PyAutoGUI
+ PyCaw
+ Comtypes
  
## Features

### Screen Capture

### Recognized Gestures: closed hand
>Action: Captures a specified area of the screen. Equivalent to Win + Shift + s command.

![Captura de tela 2024-06-19 122040](https://github.com/gregorygustavo80/Dr.Strange/assets/168982426/093994b5-48a1-4fc2-9877-e92d0e84b42d)

### Volume Control

>Extended index finger upwards.
Action: Increases the system volume.

![Captura de tela 2024-06-19 121903](https://github.com/gregorygustavo80/Dr.Strange/assets/168982426/82ea73fe-01d3-46a8-afc0-93449472ba3a)


### Mute

>V sign (index and middle fingers extended upwards).
Action: Mutes the system volume.

![Captura de tela 2024-06-19 121945](https://github.com/gregorygustavo80/Dr.Strange/assets/168982426/f5cef964-39a2-459f-92ae-fba621127ef9)


### WhatsApp Web Opening

>Hello sign in sign language (little finger raised).
Action: Opens WhatsApp Web in the default browser.

![Captura de tela 2024-06-19 121817](https://github.com/gregorygustavo80/Dr.Strange/assets/168982426/4cfc84cd-37c4-451f-90b7-825e7cb1f66a)


## Usage
Run the script Dr.Strange.py after installing the dependencies.
Ensure your camera is working correctly as the program will use it to detect hand gestures
````
python Dr.Strange.py 
````
## Press x on the keyboard to exit

## How It Works
The script uses the computer's camera to capture real-time video.
It utilizes the MediaPipe library to detect hands and recognize specific gestures based on hand landmarks' positions.
Depending on the recognized gesture, a corresponding action is performed (e.g., screen capture, volume adjustment, etc.).

## Contributions
Contributions are welcome! Feel free to fork the project, make improvements, and submit a pull request. If you encounter issues, please open an issue.


