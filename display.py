from machine import Pin
import time

# Pin definitions
PIN_DISP_CS = 21
PIN_DISP_CLK = 22
PIN_DISP_LEFT_OUT = 5
PIN_DISP_RIGHT_OUT = 17

# GPIO setup
cs_pin = Pin(PIN_DISP_CS, Pin.OUT)
clk_pin = Pin(PIN_DISP_CLK, Pin.OUT)
left_out_pin = Pin(PIN_DISP_LEFT_OUT, Pin.OUT)
right_out_pin = Pin(PIN_DISP_RIGHT_OUT, Pin.OUT)

# Function to send data to the displays
def send_Displays(addr, aux_Disp_1, aux_Disp_2):
    cs_pin.value(0)  # Enable the displays

    for i in range(7, -1, -1):
        left_out_pin.value((addr >> i) & 1)
        right_out_pin.value((addr >> i) & 1)
        clk_pin.value(1)
        clk_pin.value(0)

    for i in range(7, -1, -1):
        left_out_pin.value((aux_Disp_2 >> i) & 1)
        right_out_pin.value((aux_Disp_1 >> i) & 1)
        clk_pin.value(1)
        clk_pin.value(0)

    cs_pin.value(1)  # Disable the displays

# Function to configure the displays
def configDisplay():
    # Setup the GPIO pins for the display
    cs_pin.value(1)
    clk_pin.value(0)

    # Send the initialization commands
    send_Displays(0x0C, 0x01, 0x01)  # Shutdown mode: turn on display
    send_Displays(0x0F, 0x00, 0x00)  # Disable display test mode
    send_Displays(0x0B, 0x07, 0x07)  # Set scan limit to 7 (all digits)
    send_Displays(0x09, 0x00, 0x00)  # Disable decode mode
    send_Displays(0x0A, 0x0F, 0x0F)  # Set intensity (brightness) to maximum

# Function to initialize the display
def initDisplay():
    configDisplay()

    # Start displaying animation (you should implement this function)
    Display_animation()

# Example animation function (simplified for demonstration purposes)
def Display_animation():
    for i in range(1, 9):
        send_Displays(i, 0xFF, 0xFF)  # Light up all LEDs for demonstration
        time.sleep(0.1)
    for i in range(1, 9):
        send_Displays(i, 0x00, 0x00)  # Turn off all LEDs for demonstration
        time.sleep(0.1)

# Main execution
initDisplay()
