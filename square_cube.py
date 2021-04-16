#!/usr/bin/env python

import multiprocessing

def print_cube(num):
    print("Cube: {}".format(num*num*num))
def print_square(num):
    print("Square: {}".format(num*num))

if __name__=="__main__":
    #create the processes
    p1=multiprocessing.Process(target=print_square, args=(10,))
    p2=multiprocessing.Process(target=print_cube,args=(10,))

    #start processes
    p1.start()
    p2.start()

    #wait until process 1 is finished
    p1.join()
    #wait until process 2 is finished
    p2.join()

    #when both processes finish
    print("Done!")