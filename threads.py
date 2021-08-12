from threading import Thread
import time
def car(number, speed):
    race = 0
    while race <= 100:

        race += speed
        time.sleep(0.5)
        print('\nCar {}: {}'.format(number, race))



t_car1 = Thread(target=car, args=[1, 10])
t_car2 = Thread(target=car, args=[2, 9])

t_car1.start()
t_car2.start()