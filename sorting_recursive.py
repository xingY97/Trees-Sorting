#!python

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


def quick_sort(array):
    #base case, if the length of the array is 0 or 1, return the array, and assumed it is sorted.
    length = len(array)
    if length <= 1:
        return array
    #use pop method to remove the last element at the pivot then return it 
    else:
        pivot = array.pop()

    #create two empty list to append elements
    items_greater = []
    items_lower = []

    #compare every element to the pivot element, and append then to items_greater list if greater than pivot, append the element to items_lower if it is lower than the pivot
    for i in array:
        if i > pivot:
            items_greater.append(i)
        
        else:
            items_lower.append(i)

    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)


def main():
    array = [6,5,4,3,2,1]
    print(array)
    result = merge_sort(array)
    print(result)

    print(quick_sort([5,6,7,9,5,31,4,5,67,0]))

if __name__ == "__main__":
    main()