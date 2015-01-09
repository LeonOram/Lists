#Leon Oram
#09-01-2014
#Bubble Sort

def bubble_sort(list_):
    count2 = 1
    swaps = True
    while swaps:
        swaps = False
        for count in range(len(list_)-count2):
            if list_[count].lower() > list_[count+1].lower():
                temp = list_[count]
                list_[count] = list_[count+1]
                list_[count+1] = temp
                swaps = True
        count2=count2+1
        

list_=["z","b","F","A","a","b","H"]
bubble_sort(list_)
print(list_)
            
