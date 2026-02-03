from microbit import *

#====================================
# Life support modules
#====================================

# O2 level

oxy_level_input = input.light_level()

# CO2 level



# Pressure level

#====================================
# Power system modules
#====================================

# Battery percentage

def battery_level():

    battery = 100

    if battery < 25:
        basic.show_string("Warning")

    elif battery < 10: 
        basic.show_string("Critical")

    else:
        basic.show_number(battery)

    basic.pause(5000)

    

    



# Solar input level



# Consumption level




#====================================
# Navigation modules
#====================================

# Heading



# Speed



# Altitude



# on_forever method

def on_forever():
    pass
basic.forever(on_forever)
