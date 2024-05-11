
#This example demostrates the use of events to coordinate threads: one thread signals an event while other threads wait for it.

from threading import Thread, Event
from time import sleep

def task(event: Event, id: int) -> None:
    print(f'\nThread {id} started. Waiting for the signal....')
    event.wait() #Tell thread to wait until thread is set
    print(f'\nReceived signal. The thread {id} was completed.')

def main() -> None:
    event = Event() #reate a new Event object:

    t1 = Thread(target=task, args=(event,1))
    t2 = Thread(target=task, args=(event,2))

    t1.start()
    t2.start()

    print('Blocking the main thread for 3 seconds...')
    sleep(10) 
    event.set() #Set the event



if __name__ == '__main__':
    main()