# ExHackathonPython

In this project, we took a usb Logitech Webcam Pro 9000 that was laying around still in the box

First we tested this usin a motion sensor and taking a picture - testgpiocam.py

Next we installed motion and used the web camera itself to detect motion and take a picture.
We added an Apache server and changed the defualt page to display the pics and allow streaming by updating the Motion.conf

The final step was to have the triggered event call simplemail.py via event trigger in motion.conf

simplemail.py sends an e-mail and updates an API that was written to log all triggered events
