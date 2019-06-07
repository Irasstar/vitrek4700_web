from Vitrek4700driver import vitrek4700


def connect():
    vitrek = vitrek4700('172.16.4.90')
    params = []
    for i in range(10):
        params.append(vitrek.getmeasures())
    print(params)


if __name__ == '__main__':
    connect()


