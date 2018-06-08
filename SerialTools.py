import serial
from serial.tools import list_ports
global board

def find_board():
    global board
    cpx = 24
    gemma = 32797
    ports = list(list_ports.comports())
    for p in ports:
        if (p.pid == gemma):
            gemma = str(p.device)
            print("Hey I found a Gemma M0 at ",gemma)
            board = gemma
        elif (p.pid == cpx):
            cpx = str(p.device)
            print("Hey I found a CircuitPython Express at ",cpx)
            board = cpx
    
    
def print_serial():
    global board
    PORT = board
    BAUD = 9600
    s = serial.Serial(PORT)
    s.baudrate = BAUD
    s.parity = serial.PARITY_NONE
    s.databits = serial.EIGHTBITS
    s.stopbits = serial.STOPBITS_ONE
    data = s.readline().decode("UTF-8").rstrip()
    print(data)
