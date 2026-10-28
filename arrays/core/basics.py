# in python an array(list) is a dynamic collection of  object references, it can grow and shrink automatically as we add or remove elements.


arr = [5, 10, 15, 20]
# an index is a position of the element, in python indicies start from 0, so 0th index contains value of 5
# 0->5, 1->10, 2->15, 3->20


# print the first element
# print(arr[0])


# loooping over a list
print("single elements in the fruits list: ")
fruits = ['apple', 'banana']
for fruit in fruits:
    print (fruit, ' ')


# lets print individual characters of fruit's elements
print("individual characters of fruits's elements(strings): ")
# for i in range.....is useful for modifying orginal array elements, or when we want to skip ceratin positions
for i in range(len(fruits)):
    for j in range(len(fruits[i])):
        print(fruits[i][j], ' ' , end="")

    print('')


# iterable unpacking
fruits[0],fruits[1] = fruits[1], fruits[0]
# for in ... syntax is useful for when reading elements
for fruit in fruits:
    print(fruit)


for index, fruit in enumerate(fruits):
    print(f'index: {index} fruit: {fruit}')


# array methods that are useful
nums: list[int] = [4,2,1,-7,15]

# removes and returns the specific element, by default it removes the last element
popped = nums.pop()
print(f'popped: {popped} list: {nums}')
# removing from front makes remaining elements shift to left which can take O(n) time.


# sorted vs sort
nums.sort() # modifies the original array in place, key is additonal and useful parameter for working with lists
print(f'sorted array: {nums}')

sorted_arr = sorted(nums, key=int) # returns a new array
print(f'sorted array using sorted {sorted_arr}')

sorted_arr.insert(0, 0)
print(f'nums after inserting 0 at 0 index: {sorted_arr}')

# add to the end
sorted_arr.append(50)
print(f'appening 50 to the sorted array list: {sorted_arr}')