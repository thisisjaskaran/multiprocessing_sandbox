import multiprocessing

#empty list with global scope
result=[]

def square_list(mylist):
    global result
    for num in mylist:
        result.append(num*num)
    print("Result (in process p1) : {}".format(result))

if __name__=="__main__":
    mylist=[1,2,3,4]

    p1=multiprocessing.Process(target=square_list,args=(mylist,))

    p1.start()

    p1.join()

    print("Result (in main program) : {}".format(result))