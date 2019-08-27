import pyautogui
import time
import random

command_format = "t{}\n"
commands = [command_format.format(c) for c in ["/sell sugarcane", "/bal"]]
interval = 1/10
sleep = 50
random_padding = 10

assert(random_padding < sleep), "Sleep time must be greater than random padding"

print("Sending {} command(s) every {} seconds (type delay = {}, padding = {})".format(len(commands), sleep, interval, random_padding))
print("Sleeping 5 seconds to tab in...")
time.sleep(5)
print("Starting loop")
while True:
    print("Sending command(s)")
    for com in commands:
        pyautogui.typewrite(com, interval=interval)
        time.sleep(0.5)
    t = sleep + random.randint(-1 * random_padding, random_padding)
    print("Sleeping {} seconds".format(t))
    time.sleep(t)
