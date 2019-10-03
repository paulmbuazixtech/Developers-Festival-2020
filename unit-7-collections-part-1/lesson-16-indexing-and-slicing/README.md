<i>Notebook for this lesson can be found [here](https://github.com/rmotr-curriculum/base-python-curriculum/blob/master/unit-7-collections-part-1/lesson-16-indexing-and-slicing/Indexing%20and%20Slicing.ipynb).</i>

You can retrieve individual elements from a list by specifying the position they have in the list. Indexes start from the number 0\. So, the first element will have index 0, the second one will have index 1, the third one 3, etc... The last element of the list has index `len(list) - 1` (if the list has 8 elements, the last one is 7 (`8-1`))

In the example below, "rabbit" is the **first** element, but it's index is **0**. 

As a rule of thumb, you just subtract 1 from the way you would normally describe the order.

Index = order - 1

```python
pet_store = ['Rabbit', 'Puppy', 'Really angry cat', 'Parrot']
# Pos           0         1            2                3
# Order       first     second       third            fourth

# Rabbit is the first element and is index 0
# Puppy is the second element and is index 1
# Really angry cat is the third element and is index 2
# Parrot is the fourth element and is index 3
```

You can access an element in a list by using this format:

`list_name[index]`

There are also negative indexes, the last element of the list also has the index -1, the second to last -2, etc.

```python
names = ['Mary', 'Tom', 'Rose', 'Joe']
mary  == names[0]
tom   == names[1]
joe   == names[-1]
rose  == names[-2]
```

You can get sublists from a given list too. That'd be like a _fraction of a list_. A sublist specified by a range of indexes. For example, the **_elements between the second and the fifth position_**, the **_first three elements_**, etc.

To get a sublist you must specify two indexes separated by a colon sign. Example: `my_list[INDEX-1:INDEX-2]`.

**Important!** The resulting sublist will **NOT** include the element at the last position specified. See examples below

```python
names = ['Mary', 'Tom', 'Rose', 'Joe']
# First 3 names
print(names[0:3])
# ['Mary', 'Tom', 'Rose']

# Just the first name
print(names[0:1])
# ['Mary']

# Second and third
print(names[1:3])
# [Tom', 'Rose']

# From the second element up to the end of the list
print(names[1:4])
# ['Tom', 'Rose', 'Joe']

# The first index will be 0 by default, we can omit it:
print(names[:3])
# ['Mary', 'Tom', 'Rose']

# The last index will be the last element by default, we can also omit it
print(names[1:])
# ['Tom', 'Rose', 'Joe']
```

It's important to pay attention to how things are worded when dealing with index so you know if someone is asking for index or order. If you see words like "first" they are probably are referring to order and not index.

Great job. Now you can manually count and determine the index of something if you need it.
But what if you have a really big list or you've forgotten how to count?

Enter the `index` method. We can use it on the list and provide a search term to get the index of the first occurrence of it in a list. Note that it will error out if you are searching for something that is not in the list. For that reason, it's safer to first check if the search term is `in` your list before searching for the index of it.

The format for using this method is list_name.index('search_term').

```python
pet_store = ['Rabbit', 'Puppy', 'Battle cat', 'Parrot', 'Parrot']

# Let's get the index of parrot, without counting

# First check if it is in the list
if "Parrot" in pet_store:
    # Then get the index if it is present in the list!
    print(pet_store.index("Parrot")) # Prints 3 because it only gets first occurrence
else:
    print("These aren't the parrots you're looking for")
```

