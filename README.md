# drone
Drone wykrywający i lądujący na kodach ARUCO

kod testowany na modelu Iris quadcopter w programie gazebo 
instruckja do włączenia modelu znajduje się na stronie https://ardupilot.org/dev/docs/sitl-with-gazebo.html
aby uruchomić drona nalezy wykonać korki wskazane w powyższej instukcji ponadto:
1. uruchomić nowe okno konsoli
2.  - sudo modprobe v4l2loopback video_nr=2 card_label="GazeboCam" exclusive_caps=1
    - gz topic -t /world/iris_runway/model/iris_with_gimbal/model/gimbal/link/pitch_link/sensor/camera/image/enable_streaming -m gz.msgs.Boolean -p "data: 1"
    - gst-launch-1.0 udpsrc port=5600 caps="application/x-rtp, media=(string)video, clock-rate=(int)90000, encoding-name=(string)H264" ! rtph264depay ! avdec_h264 ! videoconvert ! v4l2sink device=/       dev/video2
      
// UMIEŚCIĆ WYMAGANE BIBLIOTEKI

nagranie lotu drona


https://github.com/user-attachments/assets/0757ae08-c6a5-46eb-82c0-79745d2697bf

