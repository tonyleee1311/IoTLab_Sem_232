import serial.tools.list_ports
AIO_FEED_SENSOR =["cambien1", "cambien2", "cambien3"]
def getPort():
    ports = serial.tools.list_ports.comports()
    N = len(ports)
    commPort = "None"
    for i in range(0, N):
        port = ports[i]
        strPort = str(port)
        if "USB Serial Device" in strPort:
            splitPort = strPort.split(" ")
            commPort = (splitPort[0])
    #return commPort
    return "COM3"
if(getPort()!="None"):
    ser = serial.Serial( port=getPort(), baudrate=115200)
    print(ser)

