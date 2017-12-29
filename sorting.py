
#Name: Murtaza Khambaty

#Used to generate a sequence of random numbers
import random
#Used for reading and writing to and from the file
import pickle
#Used to calculate the time taken by the algorithm
import time
#Used for plotting the graph
import matplotlib.pyplot as plt

#Loaded a list 'ar' with 200,000 numbers(ranging from -100,000 to 100,000)
ar=random.sample(range(-100000,100000),100000)
global time_list_bubble_sort
time_list_bubble_sort=[]
global time_list_insertion_sort    #Declared some variables globally
time_list_insertion_sort=[]
global avg_time_bubble_sort
avg_time_bubble_sort=0.0
global avg_time_insertion_sort
avg_time_insertion_sort=0.0

def input(ar):      #A function caleled Input(), reads data from the file and calls the sorting functions
    avg_time_bubble_sort=[]
    avg_time_insertion_sort=[]
    input_list=[]


    ar=random.sample(range(1,300000),200000)       #Code to write 200,000 numbers into a list called ar. I wrote the data into the list just once.

    #Referred reading from file and writing to file from stackoverflow (https://stackoverflow.com/questions/35067957/how-to-read-pickle-file)
    with open("data.txt", 'wb') as fp:
        pickle.dump(ar,fp)

    with open("data.txt", 'rb') as fp:
        ar=pickle.load(fp)


    k=2000      #A random variable 'k' helps us to read k numbers from the file into the list(k is incremented by 2000 after every 10 iterations.
    for i in range (0,25):      #This iterates the loop 25 times. One time foreach dataset(2000, 4000,6000 ..... 50,000)

        time_list_bubble_sort=[]
        time_list_insertion_sort=[]
        sum_time_bubble_sort=0.0
        sum_time_insertion_sort=0.0

        for j in range(0,10):       #Iterates the loop 10 times for each dataset(2000*10, 4000*10 .... 50,000*10)
            ar1=random.sample(ar,k)     #Loads a random sample of data into the list 'ar1' depending upon the value of k. Eg. if k=2000, 2000 elements will be loaded into ar1)
            ar2=random.sample(ar,k)     #Loads a random sample of data into the list 'ar2' depending upon the value of k. Eg. if k=4000, 4000 elements will be loaded into ar2)

        #    ar1=sorted(ar1,reverse=True)   #Used an inbuilt python function to sort the elements in descending order into ar1
        #    ar2=sorted(ar2,reverse=True)   #Used an inbuilt python function to sort the elements in descending order into ar2

        #    ar1=sorted(ar1,reverse=False)  #Used an inbuilt python function to sort the elements in ascending order into ar1
        #    ar2=sorted(ar2,reverse=False)  #Used an inbuilt python function to sort the elements in ascending order into ar2

            start_time_bubble_sort=time.time()  #stores the current time into the variable.This is the start time of the algorithm
            bubble_sort(ar1)    #Calls the function bubble sort by passing ar1
            end_time_bubble_sort=time.time()    #Stores the current time into the variable. This is the end time of the algorithm
            total_time_bubble_sort=end_time_bubble_sort-start_time_bubble_sort  #Calculates the total time taken by bubble sort to execute.
            time_list_bubble_sort.append(total_time_bubble_sort)                #Appends the total time into a list
            sum_time_bubble_sort=sum_time_bubble_sort+time_list_bubble_sort[j]  #Calculates the sum of total time.



            start_time_insertion_sort=time.time()       #stores the current time into the variable.This is the start time of the algorithm
            insertion_sort(ar2)                         #Calls the function insertion sort by passing ar2
            end_time_insertion_sort=time.time()         #Stores the current time into the variable. This is the end time of the algorithm
            total_time_insertion_sort=end_time_insertion_sort-start_time_insertion_sort #Calculates the total time taken by bubble sort to execute.
            time_list_insertion_sort.append(total_time_insertion_sort)      #Appends the total time into a list
            sum_time_insertion_sort=sum_time_insertion_sort+time_list_insertion_sort[j]     #Calculates the sum of total time.




        avg_time_bubble_sort.append(sum_time_bubble_sort/10)        #Appends the avg time of 10 bubble sorts into a list.
        avg_time_insertion_sort.append(sum_time_insertion_sort/10)  #Appends the avg time of 10 bubble sorts into a list.
        print(avg_time_bubble_sort)
        print(avg_time_insertion_sort)


        k=k+2000        #Increments k by 2000

    for i in range(1,26):       #Creates the list of the number of elemtents in one dataset
        input_list.append(2000*i)

    plt.plot(input_list,avg_time_bubble_sort,'r--' ,input_list,avg_time_insertion_sort,'b--')   #Plots graph using input list on x axis, bubble/insertion sort time on y axis. Bubble sort graph is indicated by color red, and insertion sort by blue.
    plt.show()

def bubble_sort(ar):
    global time_list
    global avg_time
    n=len(ar)

    for i in range (0,n):          #Sorts n numbers using bubble sort and a temporary variable is used for swapping
        for j in range (0,n-1):
            if(ar[j]>ar[j+1]):

                temp = ar[j]
                ar[j]=ar[j+1]
                ar[j+1]=temp


def insertion_sort(ar):
    #Performs insertion sort
    n=len(ar)

    for j in range (1,n):
        key=ar[j]
        i=j-1
        while(i>=0 and ar[i]>key):
            ar[i+1]=ar[i]
            i=i-1

        ar[i+1] = key

#Calls the method input(), which inturn calls bubble sort and insertion sort
input(ar)
