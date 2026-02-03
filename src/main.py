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


