import threading, time

print('start of program')


def takeANap(name):
    time.sleep(5);
    print('wake up! ' + name)


threadObj = threading.Thread(target=takeANap, args=['Aaron'])
threadObj.start()

print('End of program')
