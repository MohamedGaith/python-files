import time
import multiprocessing

def calc_square(numbers):
    for n in numbers:
        print('square ' + str(n*n))
        time.sleep(3)

def calc_cube(numbers):
    for n in numbers:
        print('cube ' + str(n*n*n))
        time.sleep(3)


if __name__ == "__main__":
    arr = [2,3,8]
    
    t = time.time()
    p1 = multiprocessing.Process(target=calc_square, args=(arr,))
    p2 = multiprocessing.Process(target=calc_cube, args=(arr,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
  
     
    print("done in : ",time.time()-t)

    print("The number of CPU currently working in system : ", multiprocessing.cpu_count()) 