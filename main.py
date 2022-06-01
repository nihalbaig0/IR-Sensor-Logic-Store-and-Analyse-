import serial
from datetime import datetime

now = datetime.now()

current_time = now.strftime("%H_%M_%S")
print("Current Time =", current_time)

arduino_port = "COM6" #serial port of Arduino
baud = 9600 #arduino uno runs at 9600 baud
fileName= str(current_time) + ".csv"


def main():
    ser = serial.Serial(arduino_port, baud)
    print("Connected to Arduino port:" + arduino_port)
    file = open(fileName, "a")
    print("Created file")
    # display the data to the terminal
    while True:
        getData = ser.readline().decode('utf-8').rstrip()
        data = getData
        print(data)

        # add the data to the file
        file = open(fileName, "a")  # append the data to the file
        file.write(data + "\n")  # write data with a newline

        # close out the file
        file.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
