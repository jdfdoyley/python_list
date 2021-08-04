# Python List

What is a list?

- a list is a sequence of values
- a Python list is similar to that of an array in other programming languages

What are the values in a list called?

- the values in a list is called **elements**

What are some important thing to note about Python lists?

- Python lists are ordered
- Python lists can be accessed using an index
- Python lists can store any object type
- Python lists are changeable or mutable

## Creating a Python List

How do you create a List?

- there are several ways to create a new list
- the simplest way is to enclose the elements in a square bracket `[]`

  ```Python
    # A list of integers
    numbers = [1, 2, 3, 4, 5]

    # A list of Strings
    names = ["Josephine", "Jess", "Marsha", "Krystal"]

    # A list of mixed type
    employee = [
        "Jessie", "Lewis", 30, (1761, "S Military Hwy", "Norfolk", "VA", 23502),
        True
    ]
  ```

What a list containing zero elements is called?

- A list containing zero elements is called an **empty list**

How do you create an empty list?

```python
    # An empty list
    empty_list = []
```

Is there any other way to create a Python list?

- Yes! List comprehension is another way to create a list but that will be covered later

## Python List Constructor (`list()`)

What is the Python `list()` constructor use for?

- You can use the `list()` constructor to convert other data types to list

  ```python
  letters = list('abcdef')
  # Output: ['a', 'b', 'c', 'd', 'e', 'f']
  ```

## Nesting Lists in Python

- a nested list is when you have sub-lists within a main or parent list

How do you create a nested list in Python?

```python
author = [
    "Dan", "Brown",
    ["Angels & Demons", "The Da Vinci Code", "The Lost Symbol", "Inferno"]
]
```

## Accessing List Items using Index

- a Python list has a key-value pair type relationship
- this means every value has an associated key
- with list, this is called the index
- so each value maps to an index value and vice-versa
- the index of a list ALWAYS starts from zero (0)
- this means that the first value in a list always maps to the index value 0

How do you access a Python list?

```python
# Access the first cat in the list
cats = ["persian", "bengal", "maine", "siamese", "ragdoll"]
print(cats[0])  # Output: persian

# Access the third cat in the list
print(cats[2])  # Output: maine
```

What happens when you try to access an index position that is more that the number of elements in the list?

- the Python interpreter will return a `IndexError: list out of range` error
