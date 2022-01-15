# import lib
import urllib.request as urllib2
import requests
import time
from datetime import datetime
import pyautogui
from pynput.keyboard import Key, Listener
import os


# Đọc file

def test_file():
    target_url = "https://docs.google.com/document/d/1whMCj918c5RhLQqa8SlKen4NWB2LgV7DsbxcjRppGZ8/edit?usp=sharing"

    data = urllib2.urlopen(target_url)
    for line in data:
        print(line.decode("utf-8"))

    r = requests.get(target_url, allow_redirects=True)
    print(r.headers.get('content-type'))

    open('C.txt', 'wb').write(r.content)


# Đọc file txt đơn giản lưu khung thời gian vào từ điển:
def readFile(fileName):
    with open(fileName) as input:
        timeframe = input.readline()
    input.close()
    token = timeframe.split()
    dict = {}
    dict['F'] = 0; dict['T'] = 0
    dict['D'] = 0; dict['I'] = 0
    dict['S'] = 0
    for i in token:
        if i[0] == 'T' or i[0] == 'F':
            dict[i[0]] = str(i[1:])
        else:
            dict[i[0]] = int(i[1:])
    return dict

# Password
Cpass = "children"
Ppass = "parent"

def getPassword():
    pw = input("Enter your password: ")
    return pw

def isChildren(cp, pw):
    return cp==pw

def isParent(pp, pw):
    return pp==pw

def time_to_minute(t):
    return t[0]*60+t[1]

def getCurrentTime():
    t = datetime.now()
    current_time = t.strftime("%H:%M")
    #tt = t.timetuple()
    #return [tt.tm_hour, tt.min]
    return current_time



def isTimeChildren(cur_t, t):
    for i in cur_t:
        if(t>=i[0] and t<=i[1]):
            return i[1]-t
    return -1

def C_run():
    pw = getPassword()
    if(isParent(Ppass, pw)):
        print("Parent's password!! Waiting 60 minutes.")
        time.sleep(6)
        print("Get password again")

def notify(from_to, t):
    s="0"
    d="0"
    if(len(from_to)>2):
        for i in from_to:
            if(i[0]=='S'):
                s=i[1:]
            if(i[0]=='D'):
                d=i[1:]
    return int(s), int(d)

# Chup man hình
def take_screen_shot(file_name):
  image = pyautogui.screenshot()
  image.save(file_name)
  take_screen_shot("test.jpg")

def take_in_1m():
    while True:
        time.sleep(60)
        file_name = str(datetime.date(datetime.now())) + " " + getCurrentTime() + ".jpg"
        take_screen_shot(file_name)

# Key record
a = []

def writefile(a):
    f = open("key.txt", "a")
    for key in a:
        k = str(key).replace("'", "")
        f.write(k + " ")
    f.write("\n")
    a.clear()


def on_press(key):
    a.append(key)
    if len(a) > 50:
        writefile(a)

def on_release(key):
    # stop record keyboard
    # if key == Key.esc:
    #    writefile(a)
    #    return False
    pass

def record_key():
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

# Shutdown he thong
def shut():
    os.system("shutdown /s /t 1")

# Main program
if __name__ == '__main__':
    pass
    # getCurrentTime()
    # C_run()
    # record_key()

