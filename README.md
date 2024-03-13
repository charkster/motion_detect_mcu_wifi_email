# motion_detect_mcu_wifi_email
Micropython script for emailing notification of PIR motion detect.

Works great on $5 [Seeed Xiao ESP32C3](https://wiki.seeedstudio.com/XIAO_ESP32C3_Getting_Started/), and ok on $6 [Pico W](https://www.raspberrypi.com/documentation/microcontrollers/raspberry-pi-pico.html)

[umail.py](https://github.com/shawwwn/uMail/tree/master) needs to be saved to the MCU board (as it is imported).

The sender gmail account needs to be setup for [App Password Sign-in](https://support.google.com/accounts/answer/185833?hl=en)

I used the $2 [Adafruit Mini Basic PIR Sensor](https://www.adafruit.com/product/4667)

I rename the script "main.py" when I save it to the MCU (boot.py runs first, then main.py).
