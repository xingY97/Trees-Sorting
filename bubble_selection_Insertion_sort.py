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
    TODO: Memory usage: ??? Why and under what conditions?"""
    #minus one because there is not an item after the comparison of last item
    items_length = len(items) - 1
    #use sorted function to break the loop when the list is being sorted
    sorted = False
    #as long as is_sorted is False, while loop continues to run until its true 
    while not sorted:
        sorted = True
        for i in range(0,items_length):
            if items[i] > items[i+1]:
                sorted = False
                items[i], items[i+1] = items[i+1], items[i]
                #use i to go through the items, check is current items is greater than or less than next item
                #if True, stop the loop, if false, swap the two items
                #if all items are sorted, is sorted function will return, if condition would not activate
                # so the is_sorted will stay True
    return items


def selection_sort(items):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Find minimum item in unsorted items
    # TODO: Swap it with first unsorted item


def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Take first unsorted item
    # TODO: Insert it in sorted order in front of items


if __name__ == "__main__":
    
    # print(is_sorted([1,3,5,10,20]))#expecting True
    # print(is_sorted([3,5,10,20,1]))#expecting False

    #print(bubble_sort([1,4,5,2])) #expecting 1,2,4,5
