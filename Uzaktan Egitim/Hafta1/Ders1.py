"""1 Nisan 2020 - Elif CELIK

Subjects
   1. Generate list with n items
   2. Search
   3. Sort
   4. Binary Search
   5. Mean, median, mode, weighted mean, geometric mean

"""


# Generate list with n items

import random
random.random()

s = random.randint(1,100) # random.randint(min,max)
print(s)

def get_n_random_numbers( n=10, min_ = -5, max_= 5 ):
    numbers= []
        for i in range(n):
            numbers.append(random.randint(min_, max_))
        return numbers


my_list = get_n_random_numbers()
sorted(my_list)


def my_frequency_with_dict( list ):
    frequency_dict={} # dict() = {}
    for item in list:
        if item in frequency_dict :
            frequency_dict[item] = frequency_dict[item] + 1
        else:
            frequency_dict[item] = 1
    return frequency_dict

my_frequency_with_dict(my_list)

def my_frequency_list_of_tuples(list_1):
    frequency_list = []
    for i in range(len(frequency_list)):
        s = False
        for j in range(len(frequency_list)):
            if list_1[i]==frequency_list[j][0]:
               frequency_list[j][1]= frequency_list[j][1] + 1
               s = True
        if s == False:
             frequency_list.append([list_1[i], 1])

    return frequency_list

my_list = [2, 3, 2, 5, 8, 2, 4, 3, 3, 2, 8, 5, 4, 4, 4, 4]
result_1 = my_frequency_with_dict(my_list)
result_2 = my_frequency_list_of_tuples(my_list)
print(result_1, result_2)

# Mode of a list with histogram

my_list_1 = get_n_random_numbers(10)
my_hist_d = my_frequency_with_dict(my_list_1)
print(my_hist_d)

my_hist_1 = my_frequency_list_of_tuples(my_list_1)
print(my_hist_1)

# to get mode, we have to search all keys on hist_dict
def my_mode_with_dict(my_hist_d):
    frequency_max = -1 # we define a max value -1 for comparision with the other frequency values
    mode = -1

    for key in my_hist_d.keys():
        #print(key, my_hist_d[key])
        if my_hist_d[key] > frequency_max:
            frequency_max = my_hist_d[key]
            mode = key
    return mode,frequency_max

my_mode_with_dict(my_hist_d)

my_list_100 = get_n_random_numbers(10, -4, 4)
my_hist_1 = my_frequency_with_dict(my_list_100)
my_mode_with_dict(my_hist_1)
print(my_list_100)


# Mode of a list with histogram ( a list of tuples )

my_list_1 = get_n_random_numbers(5,-2,2)
my_hist_d = my_frequency_with_dict(my_list_1)
print(my_hist_d)

my_hist_1 = my_frequency_list_of_tuples(my_list_1)
print(my_list_1)

# Linear search on a list
  def my_linear_search(my_list, item_search):
      found = (-1, -1)  # default eger listede yoksa
      n = len(my_list)
          for indis in range(n):
             if my_list[indis] == item_search:
              found = (my_list[indis], indis) # listede bulundu, return bulunan sayı, indisi tuple olarak return edilir
              # Break, uncomment for last found
           return found

my_linear_search(my_list, 3)

# Mean of list

def my_mean(my_list):
    s,t = 0,0
    for item in my_list:
        s = s+1
        t = t+item
    mean_ = t/s
    return mean_


# Sort the list

def bubble_sort(my_list):
    n = len(my_list)
    print(my_list)
    for i in range(n - 1, -1, -1):
        for j in range(0, 1):
            if not my_list[j] < my_list[j + 1]:
                # print("Swap islemi")
                temp = my_list[j]
                my_list[j] = my_list[j + 1]
                my_list[j + 1] = temp
    return my_list

# Binary Search on a sorted list

def my_binary_search(my_list, item_search):
    found = (-1, -1)
    low = 0
    high = len(my_list) - 1

    while low <= high :
        mid = (low + high) / 2

        if my_list[mid] == item_search:
            return my_list[mid], mid
        elif my_list[mid] > item_search:
            high = mid + 1
        else:
            low = mid + 1

    return found


# Median of a List

def my_median(my_list):
    my_list_2 = bubble_sort(my_list_1)
    print(my_list_2)

n = len(my_list_2)
if n%2 == 1:
    middle = int(n/2) +1
    median = my_list_2[middle]
    print(median)

else:
    middle_1 = my_list_2[int(n/2)]
    middle_2 = my_list_2[int(n/2)+1]
    median = (middle_1 + middle_2)/2
    print(median)

return median



