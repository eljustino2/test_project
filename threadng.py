import threading
import datetime
import time


def walk_dog(name):
    time.sleep(8)
    print(f'walk {name}')

def get_mail():
    time.sleep(4)
    print('get the mail')

def take_out_trash():
    time.sleep(2)
    print('take out the trash')


chore1=threading.Thread(target=walk_dog, args=('scooby',))
chore1.start()

chore2=threading.Thread(target=get_mail)
chore2.start()

chore3=threading.Thread(target=take_out_trash)
chore3.start()


chore1.join()
chore2.join()
chore3.join()


print('all chores are complete')