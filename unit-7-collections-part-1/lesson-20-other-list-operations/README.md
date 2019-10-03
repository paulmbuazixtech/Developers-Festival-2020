<i>Access the Jupyter Notebook for this lesson [here](https://github.com/rmotr-curriculum/base-python-curriculum/blob/master/unit-7-collections-part-1/lesson-20-other-list-operations/Other%20Operations%20with%20Lists.ipynb)</i>

Most important list operations covered during this video:

* `in`
* `len`
* `count`

# The `in` operator

Checking if a given element is part of a list is a simple operation that will involve the `in` operator. Let's see an example first:

```python
shopping_list = ['Milk', 'Eggs', 'Bread']

print('Bread' in shopping_list)  # True
print('Cookies' in shopping_list)  # False

do_i_need_to_buy_milk = 'Milk' in shopping_list

print(do_i_need_to_buy_milk)  # True
```

Something to note is that `in` is an **_operator_**, not a function (as `len`, for example) or a list method (like `my_list.remove()` or `my_list.append()`). We use `in` as we'd use other operators (`+`, `-`, etc).

# The `len` operator

Given a list `my_list`, how can you know how many elements does it have? The answer is simple: the `len` function:

```python
my_list = ['a', 'b', 'c']

print(len(my_list))  # 3

my_list.append('d')

new_length = len(my_list)
print(new_length)  # 4
```

We usually refer to "counting elements" as _"getting the **length** of a list"_. You can associate the `len` function with the **_length_** word.
