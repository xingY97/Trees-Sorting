#!python


def merge(items1, items2):
    """Merge given lists of items, each assumed to already be in sorted order,
    and return a new list containing all items in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Find minimum item in both lists and append it to new list
    #since we assumed two lists are already sorted, if items1 is empty return items2, vice versa
    #and then create a empty new list to append items from items1 and 2
    if len(items1) == 0:
        return items2
    if len(items2) == 0:
        return items1
    new_list = []

    # through the lists from index 0
    i,j = 0,0
    #we have to Find minimum item in both lists and append it to new list
    #use a while loop so it repeats until one list is empty
    #if first item in list1 is smaller than first item in list 2, append first item in list 1 to the new list, else, append item from list 2 to the new list, and then check
    #the next element in the list until the list is empty, so we do i += 1
    while len(items1) > i and len(items2) > j:
        if items1[i] < items2[j]:
            new_list.append(items1[i])
            i += 1
        else:
            new_list.append(items2[j])
            j += 1
    # TODO: Append remaining items in non-empty list to new list
    #extend method adds all iterable element to the end of new list
    new_list.extend(items1[i:])
    new_list.extend(items2[j:])
    

def merge_sort(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check if list is so small it's already sorted (base case)
    # TODO: Split items list into approximately equal halves
    # TODO: Sort each half by recursively calling merge sort
    # TODO: Merge sorted halves into one list in sorted order


def partition(items, low, high):
    """Return index `p` after in-place partitioning given items in range
    `[low...high]` by choosing a pivot (TODO: document your method here) from
    that range, moving pivot into index `p`, items less than pivot into range
    `[low...p-1]`, and items greater than pivot into range `[p+1...high]`.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Choose a pivot any way and document your method in docstring above
    # TODO: Loop through all items in range [low...high]
    # TODO: Move items less than pivot into front of range [low...p-1]
    # TODO: Move items greater than pivot into back of range [p+1...high]
    # TODO: Move pivot item into final position [p] and return index p


def quick_sort(items, low=None, high=None):
    """Sort given items in place by partitioning items in range `[low...high]`
    around a pivot item and recursively sorting each remaining sublist range.
    TODO: Best case running time: ??? Why and under what conditions?
    TODO: Worst case running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check if high and low range bounds have default values (not given)
    # TODO: Check if list or range is so small it's already sorted (base case)
    # TODO: Partition items in-place around a pivot and get index of pivot
    # TODO: Sort each sublist range by recursively calling quick sort



if __name__ =="__main__":
    list1 = [1,3,5,7,9]
    list2 = [2,4,6,8,10]
    
    print(merge()