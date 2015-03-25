# SCamPi
Security Camera (Raspberry) Pi

Start streaming a Logitech QuickCam UltraVision (http://support.logitech.com/en_us/product/quickcam-ultra-vision) and capture the stream as soon as the PIR detects motion. Save the captured files in the cloud.

## TODO Part I
* make init script stable (stop seems a bit flakey right now)
* add the save-chinks functionality
* hook up PIR motion detection to the chunked-stream-capture script
* save the files to a auto-synced destination that uploads files to the "cloud"
* check for connected device before trying to blink webcam LED
* make it installable
* add light sensor (i2c)
* add Solid State Relay to turn on the lights
* more...

## TODO Part II
* Create (android) app to:
- get alerts when motion is detected
- view live stream (with live audio)
- turn off/on alarm when app is connected/disconnected from local network
- turn on/off alarm through app
- talk back (hook up speaker to Raspberry Pi) - is it even possible?
