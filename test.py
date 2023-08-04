import time
from rpi_ws281x import PixelStrip, Color

LED_COUNT = 300        # Number of LED pixels.
LED_PIN = 18          # GPIO pin connected to the pixels (18 uses PWM!).
# LED_PIN = 10        # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10          # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 100  # Set to 0 for darkest and 255 for brightest
LED_INVERT = False    # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

color = Color(0,0,25)
off = Color(0,0,0)
wait_ms=50

strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
strip.begin()

# Light Up Pixels
for i in range(strip.numPixels()):
    strip.setPixelColor(i, color)
    strip.show()

# for i in range(256):
#     strip.setBrightness(i)
#     strip.show()
#     time.sleep(wait_ms / 1000.0)

# for i in range(strip.numPixels()):
#     strip.setPixelColor(i, off)
#     strip.show()
#     #time.sleep(wait_ms / 1000.0)


# for i in range(20):
#     for i in range(strip.numPixels()):
#         strip.setPixelColor(i, color)
#         strip.show()
#         time.sleep(wait_ms / 1000.0)
#     for i in range(strip.numPixels()):
#         strip.setPixelColor(i, off)
#         strip.show()
#         time.sleep(wait_ms / 1000.0)