"""uFT6336U demo (touch)."""

import time

import uFT6336U
from machine import I2C, Pin

i2c = I2C(0, scl=Pin(5), sda=Pin(4))

t = uFT6336U.FT6336U(i2c)

print("Touch test (polling)")
print("Touch the screen to see coordinates printed in REPL")

while True:
    np = t.get_points()
    if np > 0:
        print(t.get_p1_x(), t.get_p1_y(), end=" ")
    if np > 1:
        print(t.get_p2_x(), t.get_p2_y(), end=" ")
    if np > 0:
        print()
    time.sleep(0.1)
