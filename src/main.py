from microbit import *

#====================================
# Life support modules
#====================================

# O2 level



# CO2 level



# Pressure level

#====================================
# Power system modules
#====================================

# Battery percentage
def battery_percentage():
    battery = 100

    if battery < 25:
        display.show(Image.SAD)
    elif battery < 10:
        display.show(Image.ASLEEP)
    else:
        display.show(Image.HAPPY)
        
    microbit.sleep(5000)
    



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
    while True:
        battery_percentage()

        if microbit.button_a.is_pressed():
            pass # Placeholder for co2 level function call
        if microbit.button_b.is_pressed():
            pass # Placeholder for o2 function call

on_forever()
