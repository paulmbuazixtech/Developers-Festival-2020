<i>Notebook for this lesson can be found [here](https://github.com/rmotr-curriculum/base-python-curriculum/blob/master/unit-7-collections-part-1/lesson-24-iterating-lists/Iterating%20Lists).</i>

Iteration is key to understand how lists work. To properly understand lists you should be familiar with the **for loop** (control flow statement).

The good news is that it's simple to understand. Here are a few examples:
```python
names = ['Mary', 'Tom', 'Rose']
for name in names:
    print(name)
# This will print the names, each in a new line:
# Mary
# Tom
# Rose

numbers = [0, 1, 2, 3, 4]
for number in numbers:
    # I can define whatever I want inside the **for loop body**
    double = number * 2
    print(double)
# This will print the numbers, doubled (one number per line):
# 0
# 2
# 4
# 6
# 8
```
As you can see in the previous example, a `for loop` is composed of a few things:

![Python for loop explained](https://cloud.githubusercontent.com/assets/872296/20549004/261aac18-b107-11e6-8ff0-1e8ef783f737.png)

**Note 1:** `for` is a keyword, should always be used

**Note 2:** `name` in this case is a variable that **we choose**. We can choose whatever name we want for this variable (`name`, `n`, `a_name`). **It'll reference each one of the elements in the list**

**Note 3:** `in` is also a keyword. It precedes the list we'll iterate.

**Note 4:** `names` is the **list itself**. It's the list we want to iterate

**Note 5:** Finally, the **for loop body**. This is really important. We'll express here whatever we want to do with each one of the elements as we iterate through the list.
