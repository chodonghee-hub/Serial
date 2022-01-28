import serial
import serial.tools.list_ports as sp

list = sp.comports()
connected = []

## PC 연결된 COM Port 정보를 list에 넣어 확인한다.

for i in list:
    connected.append(i.device)
print("Connected COM ports : " + str(connected))

#ser = serial.Serial("COM1", 9600, timeoue = 1)
#if ser.readable() :
#   res = ser.readline()
#   print(res.decode()[:len(res)-1]

# baudrate 정보와 연결할 COM Port 이름을 입력한다.

select_comport = input("select : ")
ser = serial.Serial(select_comport, 9600, timeout = 1)

# 내가 연결할 Device의 명령어 delimiter가 Carrige return + Line Feed라고 하여 delimeter 설정

while True :
    print("insert op : " , end = '')
    op = input()
    delimiter = '\r\n'
    op = op + delimiter
    print(op)
    ser.write(op.encode())

    res = ser.readline()
    res_packet = res.decode()[:len(res)-1]
    print("result : {}".format(res_packet))
    print('\n')
    if op == 'q':
        ser.close()
