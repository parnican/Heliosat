import serial
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
	port =serial.Serial("/dev/ttyUSB1",baudrate=115200,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS,writeTimeout = 0,timeout = 10, rtscts=False,dsrdtr=False,xonxoff=False)
	data=bytes([0x0c,0x80,0x09,0x00,0xf0,0xce,0x61,0x9d,0x01,0x00,0x01,0x00,0x00,0x00]) 
	port.isOpen()	
	port.write(data) 
	return 'Hello World!'



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)