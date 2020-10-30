def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check that all adjacent items are in order, return early if so
    for i in range(len(items) - 1):
        current_item = items[i]
        next_item = items[i+1]

        #checking for ascending order, so the current item need to be less than next item
        #if next item is less than current item then it is not sorted. return false
        if next_item <= current_item:
            return False
        #return true if current item is less than next item
    return True
def bubble_sort(items):
    """
    TODO: Running time: ??? Why and under what conditions?
    #best case for bubble_sort is if the list is aleady sorted. no swapping needed 0(n)
    #worst case for bubble sort is when the smallest number is at the end
    TODO: Memory usage: ??? Why and under what conditions?"""

    #minus one because there is no item after the comparison of last item
    items_length = len(items) - 1
    #use sorted function to break the loop when the list is being sorted
    sorted = False
    # as long as is_sorted is False, while loop continues to run until its true 
    while not sorted:
        sorted = True
        for i in range(0,items_length):
            #use i to go through the items, check is current items is greater than the next item
            #if True, stop the loop, if false, swap the two items
            if items[i] > items[i+1]:
                sorted = False
                items[i], items[i+1] = items[i+1], items[i]
                #if all items are sorted,  sorted condion will return true, so if statement would not activate
                # so the sorted will stay True
    return items


def selection_sort(items):
    """Selection sort breaks the input list in two parts. the sorted part which initially is empty,
    the the unsorted part contains all elements, the algorithms selectc the minimin value of all the unsorted file and swaps
    it with the fitst unsorted value, and then increass the sorted part by one.

    TODO: Running time: ??? Why and under what conditions?
    #best and worst case for selection sort are the same, o(n*2), regardless if the list is sorted or not,
    #it will have to go throught the whole list to make sure
    TODO: Memory usage: ??? Why and under what conditions?"""
    0(1)
    items_length = range(0, len(items))
    #use i to go through every element in the items
    for i in items_length:
        #each time we do an iteration, the first item[i] is default min_value
        min_value = i
        #use j as the next item after min_value  
        #if j element is less than the min value
        for j in range(i+1, len(items_length)):
            if items[j] < items[min_value]:
                #replace the min_value with j value
                min_value = j
        #if we find an item thats less than the default value
        if min_value != i:
            #we need to switch the items
            items[min_value], items[i] = items[i], items[min_value]

    return items

def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    #sorting starts at index 1 since in insertion sort the first element is considered sorted
    items_length = range(1,len(items))
    for i in items_length:
        vaule_to_sort = items[i]
        #check if the vaule on the left is higher than the value we are trying to sort at i+1 position
        #i must be greater than 0 because python negative indexing
        #if element on the left is higher than the element i+1, we need to swap them
        while items[i-1] > vaule_to_sort and i > 0:
            items[i], items[i-1] = items[i-1], items[i]
            #and then comparison continue sort until the list is all sorted 
            i = i - 1
    return items




    

# print(is_sorted([1,3,5,10,20]))#expecting True
# print(is_sorted([3,5,10,20,1]))#expecting False

#print(bubble_sort([1,4,5,2])) #expecting 1,2,4,5

#print(selection_sort([7,8,9,5,4,3,3,0])) #expecting 0,3,3,4,5,7,8,9

#print(insertion_sort([2,3,44,5,6,7,7,9])) #expecting 2,3,5,6,7,7,9,44