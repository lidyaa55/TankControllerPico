# Raspberry Pi Pico + LCD

MicroPython setup, wiring, drivers, and test scripts

## 1. Install MicroPython on Raspberry Pi Pico

1. Download the MicroPython UF2 for Pico:  
   [https://micropython.org/download/rp2-pico](https://micropython.org/download/rp2-pico)
2. Hold **BOOTSEL** while plugging in the Pico.
3. Drag the `.uf2` file onto the Pico drive.
4. Pico reboots into MicroPython.

---

## 2. Using Raspberry Pi Pico in VS Code (MicroPython)

### Steps

1. Connect Pico via USB
2. Open VS Code
3. Press **Ctrl + Shift + P**
4. Select **Pico: Configure Project**
5. Choose the correct COM port
6. Open REPL
7. Upload your `.py` files to the Pico
8. Run scripts directly from VS Code or REPL

---

## 3. Wiring (Pico → LCD + Touch)

### Pin Mapping Table

| **Pico Pin**  | **LCD Pin** | **Signal**                |
| ------------- | ----------- | ------------------------- |
| GP5 (Pin 5)   | 5           | LCD_RS                    |
| GP6 (Pin 6)   | 12          | SDA (Touch)               |
| GP7 (Pin 7)   | 10          | SCL (Touch)               |
| GP12 (Pin 12) | 4           | LCD_RST                   |
| GP14 (Pin 14) | 7           | SCK (SPI)                 |
| GP15 (Pin 15) | 6           | MOSI (SPI)                |
| GP16 (Pin 16) | 9           | MISO (SPI)                |
| GND (Pin 18)  | 2           | GND                       |
| GP20 (Pin 20) | 3           | LCD_CS                    |
| GP31 (Pin 31) | 13          | CTS_INT (Touch Interrupt) |
| 3.3V (Pin 36) | 11          | +3.3V                     |
| 5V (Pin 39)   | 1           | +5V                       |

---

## 4. Drivers

### ILI9341 Display Driver

Save as: **`ili9341.py`**

**Source link:**  
 [https://github.com/rdagger/micropython-ili9341](https://github.com/rdagger/micropython-ili9341)

---

### FT6336U Touch Driver

Save as: **`uFT6336U.py`**

**Source link:**  
 [https://github.com/fantasticdonkey/uFT6336U](https://github.com/fantasticdonkey/uFT6336U)

---

## 5. Test Code

### **Test 1 — Shapes Demo (LCD + Touch Init)**

```python
from time import sleep
from ili9341 import Display, color565
from machine import Pin, SPI, I2C
import uFT6336U


def test():
    spi = SPI(1, baudrate=40000000, sck=Pin(14), mosi=Pin(15), miso=Pin(16))
    display = Display(spi, dc=Pin(5), cs=Pin(20), rst=Pin(12))

    i2c_bus = I2C(0, sda=Pin(6), scl=Pin(7), freq=400000)
    touch = uFT6336U.FT6336U(i2c_bus)

    display.clear(color565(64, 0, 255))
    sleep(1)
    display.clear()

    display.draw_hline(10, 319, 229, color565(255, 0, 255))
    sleep(1)

    display.draw_vline(10, 0, 319, color565(0, 255, 255))
    sleep(1)

    display.fill_hrect(23, 50, 30, 75, color565(255, 255, 255))
    sleep(1)

    display.draw_line(127, 0, 64, 127, color565(255, 255, 0))
    sleep(2)

    display.clear()

    coords = [[0, 63], [78, 80], [122, 92], [50, 50], [78, 15], [0, 63]]
    display.draw_lines(coords, color565(0, 255, 255))
    sleep(1)

    display.clear()
    display.fill_polygon(7, 120, 120, 100, color565(0, 255, 0))
    sleep(1)

    display.fill_rectangle(0, 0, 163, 163, color565(128, 128, 255))
    sleep(1)

    display.draw_rectangle(0, 64, 163, 163, color565(255, 0, 255))
    sleep(1)

    display.fill_circle(132, 132, 70, color565(0, 255, 0))
    sleep(1)

    display.draw_circle(132, 96, 70, color565(0, 0, 255))
    sleep(1)

    display.fill_ellipse(96, 96, 30, 16, color565(255, 0, 0))
    sleep(1)

    display.draw_ellipse(96, 256, 16, 30, color565(255, 255, 0))

    sleep(5)
    display.cleanup()


test()
```

---

### **Test 2 — Touch Polling**

```python
from machine import I2C, Pin
import time
import uFT6336U

i2c = I2C(0, scl=Pin(7), sda=Pin(6))
t = uFT6336U.FT6336U(i2c)

print("Touch test (polling)")
print("Touch the screen to see coordinates printed in REPL")

while True:
    np = t.get_points()
    if np > 0:
        print(t.get_p1_x(), t.get_p1_y())
    if np > 1:
        print(t.get_p2_x(), t.get_p2_y())
    time.sleep(0.1)
```

---
