import socket
from time import sleep


class vitrek4700:
    delay = 1  # in seconds
    meternums = 10

    # session = None  # empty session

    def __init__(self, ip='192.168.1.200', port=10733):
        """
            :type set_port: integer - current port number
            :type set_ip: string - ipnumber
        """
        self.ip = ip
        self.port = port
        self.connect()

    def __del__(self):
        self.disconnect()
        # print('Current device deleted')

    def connect(self):
        try:
            self.session = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.session.connect((self.ip, self.port))
            return 'connection seccessful'
        except:
            return 'connection error'

    def disconnect(self):
        try:
            self.interfacerst()
            self.session.close()
            return 'disconnect seccessful'
        except:
            return 'disconnect fail'

    def send(self, msg=''):
        try:
            msg += '\r\n'
            self.session.send(msg.encode('ascii'))
        except:
            return 'send message error'

    def recive(self, buffer=1024):
        try:
            return (self.session.recv(buffer).decode('ascii')).rstrip()
        except:
            return 0

    def gethiprobe(self):
        self.send('HIPROBE?')
        return self.recive()

    def getloprobe(self):
        self.send('LOPROBE?')
        return self.recive()

    def getmodes(self):
        """MODE: prec, fast or ripple; Digits count; Band range; Average"""

        def mode():
            self.send('MODE?')
            return self.recive()

        def digits():
            self.send('DIGITS?')
            return self.recive()

        def band():
            self.send('BAND?')
            return self.recive()

        def average():
            self.send('AVERAGE?')
            return self.recive()

        curmode = mode()
        # curmode = curmode.rstrip()
        if (curmode == 'PRECISE'):
            return {'mode': curmode, 'digits': digits(), 'band': band(), 'average': average()}
        elif curmode == 'RIPPLE':
            return {'mode': curmode, 'digits': None, 'band': None, 'average': average()}
        else:
            return {'mode': curmode, 'digits': None, 'band': None, 'average': None}

    def setmode(self, modes):
        pass

    def clsrscreen(self):
        """useless. Will not use it"""
        self.send('*CLS')

    def interfacerst(self):
        """turn off local control label without connection drop"""
        self.send('*RST')

    def dczero(self):
        self.send('DCZERO')

    def getacv(self):
        self.send('ACV?')
        return float(self.recive())

    def getdcv(self):
        self.send('DCV?')
        return float(self.recive())

    def getfreq(self):
        self.send('FREQ?')
        return float(self.recive())

    def getpeakpeak(self):
        self.send('PKPK?')
        return float(self.recive())

    def getcrfacktor(self):
        self.send('CF?')
        return float(self.recive())

    def getmeasures(self):
        """The function returns 5 parameters: 1 - DCV; 2 - ACV; 3 - Frequency; 4 - PKPK; 5 - CF"""
        return [self.getdcv(),
                self.getacv(),
                self.getfreq(),
                self.getpeakpeak(),
                self.getcrfacktor()
                ]

    def getidn(self):
        self.send('*IDN?')
        return self.recive()


if __name__ == '__main__':
    pass
