import numpy as np
import serial
import serial.tools.list_ports
import sys
import base64
from bitstring import Bits
import time
import pandas as pd

def read_hex(hexstring):
    #hexstring=''.join(reversed(hexstring))
    if len(hexstring) == 999:
       print('error')
    else:
        bx1, bx2 = hexstring[2:4],hexstring[4:6]
        bx =bx2+bx1
        by1,by2 = hexstring[6:8],hexstring[8:10]
        by= by2+by1
        bz1,bz2 = hexstring[10:12],hexstring[12:14]
        bz = bz2+bz1
        Bx = (Bits(hex=bx).int)*0.13
        By = (Bits(hex=by).int)*0.13
        Bz = (Bits(hex=bz).int)*0.13
        B = np.array([Bx,By,Bz])
        return B

def readSensor(serial): 
    try:
        # request data   21 
        serial.flushInput()
        string = "5A E8 5A DF 5A CB" #Long range - Fast mode - Start periodic readout
        
        cmd_bytes = bytearray.fromhex(string)
        
        ser.write(cmd_bytes)
        
        msg_b = serial.read(8)
        encoded = str(base64.b16encode(msg_b))
        encoded = encoded.replace("b'","")
        encoded = encoded.replace("'","")
        B = read_hex(encoded)
        #print(B)
        return B

    except KeyboardInterrupt:
        print("User interrupt encountered. Exiting...")
        time.sleep(3)
        serial.flushInput()
        serial.flushOutput()
        serial.close()
        sys.exit()
    except:
        # for all other kinds of error, but not specifying which one
        print("Device disconnected")
        time.sleep(3)
        serial.flushInput()
        serial.flushOutput()
        serial.close()
        sys.exit()


def getXMCserialConnection(): 
    # returns serial port object
    # opens the serial port to communicate with the XMC
    global ser
    ports = list(serial.tools.list_ports.comports())
    if (len(ports) != 0):
        for p in ports:
            if ((p.pid == 261) & (p.vid == 4966)): # pid and vid from xmc
                #print("XMC found on port: " + p.device)
                try:
                    ser = serial.Serial(p.device, 115200)
                    #print('Serial Connection Done')
                    return ser
                except Exception:
                    print('Please unplug then plug back the device')
                    print('Serial Connection Done')
    print('ERROR(getSerialConnection) - Cannot Find a device.')
    sys.exit()
    
    
def trainData():
    
    
    
    label = ['0000','0001','0010','0011','0100','0101','0110','0111','1000','1001','1010','1011','1100','1101','1110','1111']
    label2= ['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15']
    df = pd.DataFrame(columns=['label','Bx','By','Bz'])
    ser = getXMCserialConnection()
    for i in range(len(label)):
        print('Storing sequence %s' %(label[i]))
        inpt = input('Press to store value')
        
        for j in range(40):
            B = readSensor(ser)
            new_row = {'label':label2[i], 'Bx':B[0], 'By':B[1], 'Bz':B[2]}
            time.sleep(.5)      
            df = df.append(new_row, ignore_index=True)
    timestr = time.strftime("%Y%m%d-%H%M%S")
    df.to_csv("data/Switch_Data_{}.xlsx".format(timestr))            


    return df      



def testData():
    label = ['0000','0001','0010','0011','0100','0101','0110','0111','1000','1001','1010','1011','1100','1101','1110','1111']
    label2= ['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15']  
    ser = getXMCserialConnection()
    time.sleep(.1)
    B = readSensor(ser)
    
    outpt = np.array([B[0],B[1],B[2]]).reshape((1,-1))
    ser.flushInput()
    ser.flushOutput()
    ser.close()
    return outpt
    
    
    
    
    
