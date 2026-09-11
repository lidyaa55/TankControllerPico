# Raspberry Pi Pico + LCD

MicroPython setup, wiring, drivers, and test scripts

## 1. Install MicroPython on Raspberry Pi Pico

1. Download the MicroPython UF2 for Pico:  
   [https://micropython.org/download/rp2-pico](https://micropython.org/download/rp2-pico)
2. Hold **BOOTSEL** while plugging in the Pico.
3. Drag the `.uf2` file onto the Pico drive.
4. Pico reboots into MicroPython.

---

## 2. Using Raspberry Pi Pico in Visual Studio Code (MicroPython)

### Steps

1. Connect Pico via USB
2. Open Visual Studio Code
3. Press **Ctrl + Shift + P**
4. Select **Pico: Configure Project**
5. Choose the correct COM port
6. Open REPL
7. Upload your `.py` files to the Pico
8. Run scripts directly from Visual Studio Code or REPL

---

## 3. Wiring (Pico → LCD + Touch)

### Pin Mapping Table

| **Pico Pin** | **Pico Physical Pin** | **LCD Pin** | **Signal**                |
| ------------ | --------------------- | ----------- | ------------------------- |
| GP5          | 5                     | 5           | LCD_RS                    |
| GP6          | 6                     | 12          | SDA (Touch)               |
| GP7          | 7                     | 10          | SCL (Touch)               |
| GP12         | 12                    | 4           | LCD_RST                   |
| GP14         | 14                    | 7           | SCK (SPI)                 |
| GP15         | 15                    | 6           | MOSI (SPI)                |
| GP16         | 16                    | 9           | MISO (SPI)                |
| GND          | 18                    | 2           | GND                       |
| GP20         | 20                    | 3           | LCD_CS                    |
| GP31         | 31                    | 13          | CTS_INT (Touch Interrupt) |
| 3.3V         | 36                    | 11          | +3.3V                     |
| 5V           | 39                    | 1           | +5V                       |

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

1. Run **`demo_setup.bat`** from the `demos` folder to download the driver files.
2. Connect the Pico to Visual Studio Code and upload **`ili9341.py`** and **`uFT6336U.py`** to the Pico.
3. To test the LCD, open **`shapes_demo.py`**, upload it to the Pico, and run the current file. The display should show colored lines, rectangles, polygons, circles, and ellipses.
4. To test the touchscreen, open **`touch_demo.py`**, upload it to the Pico, and run the current file. Touch coordinates should appear in the Visual Studio Code REPL.

---
