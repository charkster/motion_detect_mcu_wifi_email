# motion_detect_mcu_wifi_email
Micropython script for emailing notification of PIR motion detect.

Works great on $5 [Seeed Xiao ESP32C3](https://wiki.seeedstudio.com/XIAO_ESP32C3_Getting_Started/), and ok on $6 [Pico W](https://www.raspberrypi.com/documentation/microcontrollers/raspberry-pi-pico.html) (it's slower because wifi is an external module).

[umail.py](https://github.com/shawwwn/uMail/tree/master) needs to be saved to the MCU board (as it is imported).

The sender gmail account needs to be setup for [App Password Sign-in](https://support.google.com/accounts/answer/185833?hl=en)

I used the $2 [Adafruit Mini Basic PIR Sensor](https://www.adafruit.com/product/4667)

I rename the script "main.py" when I save it to the MCU (boot.py runs first, then main.py).

The PIR sensor has GND connections for pins 1,2 and 3.3V for pin 3. The detect signal (alarm) is pin 4 and is active-high.

**Sample email notification:**

![picture](https://github.com/charkster/motion_detect_mcu_wifi_email/blob/main/motion_notification_email.png)


![picture](https://github.com/charkster/motion_detect_mcu_wifi_email/blob/main/mcu_boards_motion_detect_wifi_email_sm.JPG)
