import serial
import time
import struct


with serial.Serial('/dev/ttysWK0',115200,timeout=1) as ser: #針對傳輸阜及鮑率與serial設定
    ser.write(b'')
    print(ser.name)

    x = 0
    try:
        while True:
            ser.write(bytes(str(x),encoding='ASCII')) #僅str可以使用bytes 進行轉碼
            print(bytes(str(x),encoding='ASCII'))
            ser.write(b'\n')
            time.sleep(0.1)
            x += 1
    except KeyboardInterrupt:
        ser.close()
ser.close()