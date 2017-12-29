import random
import pickle
import time
import matplotlib.pyplot as plt

ar=random.sample(range(-100000,100000),100000)
global time_list_bubble_sort
time_list_bubble_sort=[]
global time_list_insertion_sort
time_list_insertion_sort=[]
global avg_time_bubble_sort
avg_time_bubble_sort=0.0
global avg_time_insertion_sort
avg_time_insertion_sort=0.0

def input(ar):
    '''
    file_name=["data_2000","data_4000","data_6000","data_8000","data_10000","data_12000","data_14000","data_16000","data_18000","data_20000","data_22000","data_24000","data_26000","data_28000","data_30000","data_32000","data_34000","data_36000","data_38000","data_40000","data_42000","data_44000","data_46000","data_48000","data_50000"]

    for i in range(2000,50000):
    ar=random.sample(-100000,100000,i)
    with open(filename,"wb")'''

    avg_time_bubble_sort=[]
    avg_time_insertion_sort=[]
    input_list=[]

    #I have referred this part of the code from stackoverflow
    with open("data.txt", 'wb') as fp:
        pickle.dump(ar,fp)

    with open("data.txt", 'rb') as fp:
        ar=pickle.load(fp)
    k=2000
    for i in range (0,3):

        time_list_bubble_sort=[]
        time_list_insertion_sort=[]
        sum_time_bubble_sort=0.0
        sum_time_insertion_sort=0.0

        for j in range(0,5):
            ar1=random.sample(ar,k)


            start_time_insertion_sort=time.time()

            insertion_sort(ar1)

            end_time_insertion_sort=time.time()
            total_time_insertion_sort=end_time_insertion_sort-start_time_insertion_sort
            time_list_insertion_sort.append(total_time_insertion_sort)

            sum_time_insertion_sort=sum_time_insertion_sort+time_list_insertion_sort[j]
            print(time_list_insertion_sort)


            start_time_bubble_sort=time.time()

            bubble_sort(ar1)

            end_time_bubble_sort=time.time()
            total_time_bubble_sort=end_time_bubble_sort-start_time_bubble_sort
            time_list_bubble_sort.append(total_time_bubble_sort)

            sum_time_bubble_sort=sum_time_bubble_sort+time_list_bubble_sort[j]
            print(time_list_bubble_sort)





        avg_time_bubble_sort.append(sum_time_bubble_sort/10)
        avg_time_insertion_sort.append(sum_time_insertion_sort/10)
        print(avg_time_bubble_sort)
        print(avg_time_insertion_sort)

        #   insertion_sort(ar1)
        k=k+2000

    for i in range(0,3):
        input_list.append(2000*i)

    plt.plot(input_list,avg_time_bubble_sort,'r--' ,input_list,avg_time_insertion_sort,'b--')

def bubble_sort(ar):
    global time_list
    global avg_time
    n=len(ar)
    #start_time=time.time()
    for i in range (0,n):
        for j in range (0,n-1):
            if(ar[j]>ar[j+1]):
                '''
                ar[j]=ar[j]+ar[j+1]
                ar[j+1]=ar[j]-ar[j+1]
                ar[j]=ar[j]-ar[j+1]
                '''
                temp = ar[j]
                ar[j]=ar[j+1]
                ar[j+1]=temp
    #end_time=time.time()

    #total_time=end_time-start_time

    #time_list.append(total_time)
'''
    for i in range (0,10):
        avg_time=avg_time+time_list[i]
        if(time_list[i]==9):
            print(avg_time)
            time_list=[]
            avg_time=0

'''
#    print(time_list)
def insertion_sort(ar):
    n=len(ar)
#    start_time=time.time()
    for j in range (1,n):
        key=ar[j]
        i=j-1
        while(i>=0 and ar[i]>key):
            ar[i+1]=ar[i]
            i=i-1

        ar[i+1] = key

 #   end_time=time.time()

  #  total_time=end_time-start_time
   # print(total_time)

input(ar)
