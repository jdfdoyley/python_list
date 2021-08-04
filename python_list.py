# Create a list
# =============

# A list of integers
numbers = [1, 2, 3, 4, 5]

# A list of Strings
names = ["Josephine", "Jess", "Marsha", "Krystal"]

# A list of mixed type
employee = [
    "Jessie", "Lewis", 30, (1761, "S Military Hwy", "Norfolk", "VA", 23502),
    True
]

# An empty list
empty_list = []

# The list() Constructor
# ======================

# Convert a string to a list
letters = list('abcdef')  # Output: ['a', 'b', 'c', 'd', 'e', 'f']
print(letters)

# Convert a tuple to a list
numbers = list((2, 4, 6, 8))  # Output: [2, 4, 6, 8]
print(numbers)

# Nested List in Python
# =====================

author = [
    "Dan", "Brown",
    ["Angels & Demons", "The Da Vinci Code", "The Lost Symbol", "Inferno"]
]
print(author)

# Access List Items by Index
# ==========================

# Access the first cat in the list
cats = ["persian", "bengal", "maine", "siamese", "ragdoll"]
print(cats[0])  # Output: persian

# Access the third cat in the list
print(cats[2])  # Output: maine