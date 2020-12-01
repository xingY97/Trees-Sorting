
def counting_sort(numbers):
    """Sort given numbers (integers) by counting occurrences of each number,
    then looping over counts and copying that many numbers into output list.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    #first if the length of numbers array contains only one element, return that element, no sorting required.
    if len(numbers) < 2:
        return 
    # TODO: Find range of given numbers (minimum and maximum integer values)
    #then find range of given numbers by subtracting maximun value to mininum value
    minNum = min(numbers)
    maxNum = max(numbers)
    range_num = maxNum - minNum + 1
    # TODO: Create list of counts with a slot for each number in input range
    #then create a empty count array to hold occurences of each value in the array
    countArray = [0] * range_num

    # use a for loop to go throught the array, if the number appears more than once increment its count by 1
    for item in numbers:
        countArray[item - minNum] += 1
    # TODO: Loop over counts and append that many numbers into output list
    # FIXME: Improve this to mutate input instead of creating new output list
    i , j = 0, 0
    while i < len(numbers):
        while countArray[j] < 1:
            j += 1
        numbers[i] = minNum + j
        countArray[j] -= 1
        i += 1


def bucket_sort(numbers, num_buckets=10):
    """Sort given numbers by distributing into buckets representing subranges,
    then sorting each bucket and concatenating all buckets in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Find range of given numbers (minimum and maximum values)
    # TODO: Create list of buckets to store numbers in subranges of input range
    # TODO: Loop over given numbers and place each item in appropriate bucket
    # TODO: Sort each bucket using any sorting algorithm (recursive or another)
    # TODO: Loop over buckets and append each bucket's numbers into output list
    # FIXME: Improve this to mutate input instead of creating new output list

if __name__ == "__main__":
    item = [2,5,6,7,8,9,1]
    counting_sort(item)
    print(item)