<i>Access the Jupyter Notebook for this lesson [here](https://github.com/rmotr-curriculum/base-python-curriculum/blob/master/unit-7-collections-part-1/lesson-2-intro-to-lists/Intro%20to%20Lists.ipynb)</i>

Lists are probably the most popular collections used in the Python programming language. They're similar to _"arrays"_ in other programming languages.

A list is an **_ordered_**, **_heterogeneous_**, **_mutable_** collection. This means:

##### Ordered

As you add new elements, the list "remembers" the order that you chose for your elements. Example:

```python
shopping_list = []  # An empty list

shopping_list.append('Eggs')
shopping_list.append('Milk')
shopping_list.append('Bread')

print(shopping_list)  # ['Eggs', 'Milk', 'Bread']
```

In the previous example you can see that the order of the elements in the resulting list (`['Eggs', 'Milk', 'Bread']`) is the same order we chose when building the list (_"Eggs"_ first, _"Milk"_ second and finally _"Bread"_).

##### Heterogeneous

This means that you can put any type of element in a list. This is a recurrent theme in all the other Python collections, they take any type of element. Example:


```python
my_list = ["Hello", 3, True, 2.5]
```

As you can see, we're storing a string object (`"Hello"`), an integer (`3`), a boolean (`True`) and a float (`2.5`). Python lists are perfectly capable of handling any type of elements. Even other lists (we'll talk more about this later).

##### Mutable

This means that we can change lists (we can _mutate_ them). It probably sounds a little bit dumb to mention, but you'll see later that there are other collections that are **not** mutable. But going back to lists, you can simply change them at will, for example:

```python
shopping_list = []  # An empty list

shopping_list.append('Eggs')  # Add an element (changed the list)
shopping_list.append('Milk')  # Add another element

print(shopping_list)  # ['Eggs', 'Milk']

shopping_list.remove('Milk')  # Remove an element (changed it again)

print(shopping_list)  # ['Eggs']
```

Don't _overthink_ this; it's the most intuitive way of thinking collections: being mutable.

# List Operations

Having a list created is not enough. We'll need to "manipulate" these lists to achieve something useful. These are the most common operations with lists:

* Adding elements
* Counting elements (_"How many elements does this list have?"_)
* Removing elements
* Check if an element exists in a list (_"Is john@rmotr.com already part of this list?"_)
* "Concatenating" lists: Building a new list out of two or more lists.

We'll explore all these operations in detail in the following lessons.
