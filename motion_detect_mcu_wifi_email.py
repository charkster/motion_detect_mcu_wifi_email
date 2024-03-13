import machine
import umail
import network
import time
import ntptime
import utime

def connect_to_wifi():
    # Your network credentials
    ssid = 'SSID_NAME'
    password = 'MY_SSID_PASSWORD'
    #Connect to Wi-Fi
    wlan = network.WLAN(network.STA_IF)
    time.sleep_ms(1000)
    wlan.active(True)
    time.sleep_ms(1000)
    wlan.connect(ssid, password)

    # Wait for connection to establish
    max_wait = 10
    while max_wait > 0:
        if wlan.status() == 1010:
                break
        max_wait -= 1
        print('waiting for connection...')
        time.sleep(1)
    
    # Manage connection errors
    if wlan.status() == 1010:
        print('connected')
        ntptime.settime() # this is GMT
        rtc = machine.RTC()
        utc_shift = -7 # Phoenix Arizona
        tm = utime.localtime(utime.mktime(utime.localtime()) + utc_shift*3600)
        tm = tm[0:3] + (0,) + tm[3:6] + (0,)
        rtc.datetime(tm)
    else:
        print(wlan.status())

def sendEmail():
    t = time.localtime()
    date = str("{:2d}/{:2d}/{:4d} {:2d}:{:02d}:{:02d}".format(t[1],t[2],t[0],t[3],t[4],t[5]))
    #initialize SMTP server and login
    smtp = umail.SMTP('smtp.gmail.com', 465, ssl=True)
    # Email details
    sender_email = 'azstanfordfamily@gmail.com'
    sender_name = 'pico email'
    sender_app_password = 'eueewczhxrmeuhph'
    recipient_email ='charkster@gmail.com'
    email_subject ='MCU Motion Detect'
    smtp.login(sender_email, sender_app_password)
    smtp.to(recipient_email)
    smtp.write("From:" + sender_name + "<"+ sender_email+">\n")
    smtp.write("Subject:" + email_subject + "\n")
    smtp.write("Motion detected\n")
    smtp.write(date)
    smtp.send()
    smtp.quit()
    wlan = network.WLAN(network.STA_IF) # redefine wlan for disconnect
    wlan.disconnect()

def motion_detect(self):
    motion_pin = machine.Pin(16, machine.Pin.IN, machine.Pin.PULL_DOWN) # redefine motion_pin for IRQ disable/re-enable
    motion_pin.irq(motion_detect, trigger=0) # disable IRQ
    connect_to_wifi()
    sendEmail()
    time.sleep(60) # I don't want too many motion detections
    motion_pin.irq(motion_detect, trigger=machine.Pin.IRQ_RISING) # enable IRQ


motion_pin = machine.Pin(16, machine.Pin.IN, machine.Pin.PULL_DOWN)
time.sleep(60) # allow sensor to settle
motion_pin.irq(motion_detect, trigger=machine.Pin.IRQ_RISING) # enable IRQ

while True:
    time.sleep(1)
