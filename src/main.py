from microbit import *
import radio

radio.on()
radio.config(channel=7)

#====================================
# Life support modules
#====================================

# O2 level

ROOM_O2_READING = 600  # Example baseline value for room O2 level corresponding to ~21% of sensor range
MAX_O2_READING = 800  # Example maximum value for O2 level corresponding to top of sensor range

def read_o2_percentage():
    raw = pin0.read_analog()
    ratio = (raw - ROOM_O2_READING) / float(MAX_O2_READING - ROOM_O2_READING)
    o2 = 21 + ratio * 4

    if o2 < 0:
        o2 = 0
    elif o2 > 25:
        o2 = 25

    return o2

def update():
    o2_level = read_o2_percentage()
    
    if o2_level < 19.5:
        display.show(Image.L)
    else:
        display.clear()
    
    return o2_level

# CO2 level

MIN_PPM = 400
MAX_PPM = 5000

def read_co2_ppm():
    light = display.read_light_level()
    ratio = 1.0 - (light / 255.0)
    co2 = MIN_PPM + ratio * (MAX_PPM - MIN_PPM)
    return int(co2)

def update():
    o2_level = read_o2_percentage()
    co2_ppm = read_co2_ppm()

    if o2_level < 19.5 and co2_ppm > 1500:
        display.show("L")
    else:
        display.clear()

    return o2_level, co2_ppm


# Pressure level

#====================================
# Power system modules
#====================================

# Battery percentage



# Solar input level



# Consumption level




#====================================
# Navigation modules
#====================================

# Heading



# Speed



# Altitude



# on_forever method


