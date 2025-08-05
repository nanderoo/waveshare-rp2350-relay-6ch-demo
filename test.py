#
# Author: Neal Anders <neal.anders@gmail.com>
# Date: 2025-08-05
# License: Whatever?
#
# This script sends commands to a Waveshare RP2350-Relay-6CH board via serial port.
# Reference: https://www.waveshare.com/wiki/RP2350-Relay-6CH
#
# It requires the pyserial library to be installed. 
# You can install it using pip: pip install pyserial
# Usage: python script.py <COM_PORT> <COMMAND_NUMBER>
# Example: python script.py COM10 1
# Make sure to replace 'COM10' with your actual COM port.
#
# Note: Serial communication is via the RS-485 interface.

import serial
import sys

# These are specific to the Waveshare RP2350-Relay-6CH board
relay_commands = [
    bytes([0x06, 0x05, 0x00, 0x01, 0x55, 0x00, 0xA2, 0xED]),  # CH1
    bytes([0x06, 0x05, 0x00, 0x02, 0x55, 0x00, 0x52, 0xED]),  # CH2
    bytes([0x06, 0x05, 0x00, 0x03, 0x55, 0x00, 0x03, 0x2D]),  # CH3
    bytes([0x06, 0x05, 0x00, 0x04, 0x55, 0x00, 0xB2, 0xEC]),  # CH4
    bytes([0x06, 0x05, 0x00, 0x05, 0x55, 0x00, 0xE3, 0x2C]),  # CH5
    bytes([0x06, 0x05, 0x00, 0x06, 0x55, 0x00, 0x13, 0x2C]),  # CH6
    bytes([0x06, 0x05, 0x00, 0xFF, 0xFF, 0x00, 0xBD, 0xBD]),  # ALL ON
    bytes([0x06, 0x05, 0x00, 0xFF, 0x00, 0x00, 0xFC, 0x4D])   # ALL OFF
]

# Check if the command line arguments are provided
if len(sys.argv) > 2: # need a com port and relay number/command
    com = sys.argv[1]
    cmd = int(sys.argv[2])
    cmd_num = int(cmd) -1 # Convert to 1-based index from 0-based index)
else: 
    print("Usage: python script.py <COM_PORT> <COMMAND_NUMBER>")
    print("Example: python script.py COM10 1")
    sys.exit(1)

# Make sure the command number is valid
if cmd_num < 0 or cmd_num >= len(relay_commands):
    print(f"Invalid command number: {cmd_num + 1}. Must be between 1 and {len(relay_commands)}.")
    sys.exit(1) 

# open the serial port
try:
    conn = serial.Serial(com, 9600, timeout=1)
except serial.SerialException as e:
    print(f"Error opening serial port {com}: {e}")
    sys.exit(1) 

# Write the command to the relay
conn.write(relay_commands[cmd_num])  # Send command
