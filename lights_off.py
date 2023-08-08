from config import *
from rpi_ws281x import PixelStrip, Color


def turn_on(strip, color):
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
    strip.show()

if __name__ == '__main__':
    strip = PixelStrip(MAX_LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    strip.begin()
    color = Color(0,0,0)
    turn_on(strip, color)