import csv
import sys

def find_max(index,my_list,dict):
    min = 0
    for i in range(1,len(my_list)):
        #finding total marks obtained by each student for finding top 3 students
        if(my_list[i][0] not in dict):
            dict[my_list[i][0]] = int(my_list[i][index])
        else:
            dict[my_list[i][0]] = dict[my_list[i][0]]+int(my_list[i][index])    

        if(int(my_list[i][index])>min):
            min = int(my_list[i][index])
            topper = my_list[i][0] 
    return topper

def find_topper_in_each_subject(my_list,dict):
    for i in range(1,7):
        topper = find_max(i,my_list,dict)
        print("Topper of %s class is %s"%(my_list[0][i],topper))
        
def top3Students(my_list,dict):
    first = 0
    second = 0
    third = 0
    firsttopper = ""
    secondtopper=""
    thirdtopper = ""
    for i in dict:
        if(dict[i]>first):
            third = second
            second = first
            first = dict[i]
            thirdtopper = secondtopper
            secondtopper = firsttopper
            firsttopper = i
        elif(dict[i]>second):
            third = second
            second = dict[i]
            thirdtopper = secondtopper
            secondtopper = i
        elif(dict[i]>third):
            third = dict[i]  
            thirdtopper = i      
    print("Best students in the class are (%s first rank, %s second rank, %s third rank)"%(firsttopper,secondtopper,thirdtopper))       

with open(sys.argv[1],'r') as f:
    file = csv.reader(f)
    my_list = list(file)

dict = {}
find_topper_in_each_subject(my_list,dict)   #Time Complexity => O(totalsubjects*totalstudents) 
top3Students(my_list,dict) #Time Complexity => O(TotalStudents) as I already calculated total marks
                         #for each subjects in subquestion 1 
                               


