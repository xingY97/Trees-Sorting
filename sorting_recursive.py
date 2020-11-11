#!python

# def merge(items1, items2):
#     """Merge given lists of items, each assumed to already be in sorted order,
#     and return a new list containing all items in sorted order.
#     TODO: Running time: ??? Why and under what conditions?
#     TODO: Memory usage: ??? Why and under what conditions?"""
#     # TODO: Find minimum item in both lists and append it to new list
#     #since we assumed two lists are already sorted, if items1 is empty return items2, vice versa
#     #and then create a empty new list to append items from items1 and 2
#     if len(items1) == 0:
#         return items2
#     if len(items2) == 0:
#         return items1
#     result_list = []

#     # through the lists from index 0
#     i,j = 0,0
#     #we have to Find minimum item in both lists and append it to new list
#     #use a while loop so it repeats until one list is empty
#     #if first item in list1 is smaller than first item in list 2, append first item in list 1 to the new list, else, append item from list 2 to the new list, and then check
#     #the next element in the list until the list is empty, so we do i += 1
#     while len(items1) > i and len(items2) > j:
#         if items1[i] < items2[j]:
#             result_list.append(items1[i])
#             i += 1
#         else:
#             result_list.append(items2[j])
#             j += 1
#     # TODO: Append remaining items in non-empty list to new list
#     #extend method adds all iterable element to the end of new list
#     result_list.extend(items1[i:])
#     result_list.extend(items2[j:])

#     return result_list


def merge_sort(array):
    if len(array) <= 1:
        return array
    #find the middle, divind the array in half
    midPoint = int(len(array) / 2)
    #define left and right arrays, first half start from first element to midpoint, second half from midpoint to the end
    left = merge_sort(array[:midPoint])
    right = merge_sort(array[midPoint:])

    return merge(left,right)

def merge(left,right):

    #create a empty new result list to append items
    result = []
    left_pointer = right_pointer = 0

    #use a while loop to make sure there elements in both arrays
    while left_pointer < len(left) and right_pointer < len(right):
        #while there is element in the array, we need to check which index in the array is lower
        if left[left_pointer] < right[right_pointer]:
            #since the element in left array is smaller than right array, append it to the empty result array, and then move on to next element
            result.append(left[left_pointer])
            left_pointer += 1

        #else append elements from right array
        else :
            result.append(right[right_pointer])
            right_pointer += 1

    #extend method adds all iterable element to the end of new list
    result.extend(left[left_pointer:])
    result.extend(right[right_pointer:])

    return result

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



def main():
    array = [6,5,4,3,2,1]
    print(array)
    result = merge_sort(array)
    print(result)

if __name__ == "__main__":
    main()