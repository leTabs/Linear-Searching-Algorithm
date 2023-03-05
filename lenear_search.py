# lenear search algorithm

def lenear_search(array, target):
    index = 0
    # the will indecate the position of the target if found.
    for item in array:
        # loop through the array
        if item == target:
            return (f'Target "{target}" found in:  {index}th position.')
            # if the item matches the target, then the target is returned with the it's index
        index += 1
        # increment the index after every unmatched loop

        if index == len(array):
            # if the target is not located in the array, only then we reach the point
            # that the index will be equal to the length of the array
            return (f'Target "{target}" is not located in the array.')
            # so inform the user accordingly

# testing...
ores = ['gold', 'coal', 'silver', 'bronse', 'diamond', 'emerald', 'rubby', 'iron']
print(lenear_search(ores, 'iron'))
