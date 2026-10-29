# hashing is done via dictionary. which stores elements in key-value pairs.
# a set is useful for unique/distinct values

chars = ["a", "b", "a", "c","d", "d", "d"]

freq = {}

# using indexing
for char in chars:
    if char not in freq:
        freq[char] = 0

    freq[char] += 1
print(freq)


freq = {}

for char in chars:
    freq[char] = freq.get(char, 0) + 1

print(freq)



# printing single elements
print(freq.get("a", 0))

print("e" in freq);

# get key and value using items() individually
for key, value in freq.items():
    print(f'key: {key} value: {value}')


# get all keys and values
print(freq.keys())
print(freq.values())


# pop - removes and retrieves a key
removed = freq.pop("a")
print(removed)

print(freq.pop("b", 0))

# update - adds or updates and entry
freq.update({"a": 3, "b": 10})
print(freq)