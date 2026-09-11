# Python Practice Questions — Strings, Lists & Dictionaries

> **Goal:** Practice these as programming problems. Try solving each without looking up the solution.
> Difficulty gradually increases from **Easy → Intermediate → Challenging**.

---

# 🧵 Strings — 20 Questions

### 1. Reverse a String
Write a program that takes a string as input and prints the string in reverse order.

**Example:**
```text
Input:  hello
Output: olleh
```

### 2. Count Characters
Write a program that takes a string and counts the total number of characters **excluding spaces**.

**Example:**
```text
Input:  hello world
Output: 10
```

### 3. Count Vowels
Write a program that counts the number of vowels (`a, e, i, o, u`) in a string, regardless of uppercase/lowercase.

**Example:**
```text
Input:  Programming
Output: 3
```

### 4. Remove Vowels
Write a program that removes all vowels from a string.

**Example:**
```text
Input:  Twitter
Output: Twttr
```

### 5. Count a Specific Character
Take a string and a character from the user. Count how many times that character occurs.

**Example:**
```text
String: banana
Character: a

Output: 3
```

### 6. Check Palindrome
Write a program that checks whether a string is a palindrome.

**Example:**
```text
Input: madam
Output: Palindrome
```

### 7. Convert Name Format
Take a user's full name and convert it into:

```text
Last Name, First Name
```

**Example:**
```text
Input: Farhan Khan
Output: Khan, Farhan
```

### 8. Count Words
Write a program that counts the number of words in a sentence.

**Example:**
```text
Input: Python is easy to learn
Output: 5
```

### 9. Find Longest Word
Take a sentence and print the longest word.

**Example:**
```text
Input: Python programming is interesting
Output: programming
```

### 10. Capitalize Every Word
Write a program that converts the first character of every word to uppercase.

**Example:**
```text
Input:  python programming language
Output: Python Programming Language
```

### 11. Replace a Word
Take a sentence, a word to search for, and a replacement word. Replace all occurrences.

**Example:**
```text
Sentence: I like Java. Java is popular.
Find: Java
Replace: Python

Output: I like Python. Python is popular.
```

### 12. Remove Extra Spaces
Write a program that removes unnecessary spaces from a sentence.

**Example:**
```text
Input:  "  Python   is   easy  "
Output: "Python is easy"
```

### 13. Character Frequency
Create a program that counts how many times every character appears in a string.

**Example:**
```text
Input: banana

Output:
b: 1
a: 3
n: 2
```

### 14. Find First and Last Occurrence
Take a string and a substring from the user. Print the index of its first and last occurrence.

**Example:**
```text
String: programming programming
Search: programming

Output:
First: 0
Last: 12
```

### 15. Anagram Checker
Write a program that checks whether two strings are anagrams.

**Example:**
```text
Input 1: listen
Input 2: silent

Output: Anagram
```

### 16. Password Validator
Write a program that validates a password.

A valid password must:
- Have at least 8 characters
- Contain uppercase letters
- Contain lowercase letters
- Contain a digit
- Contain a special character

**Example:**
```text
Input: Farhan@123
Output: Valid Password
```

### 17. Compress Repeated Characters
Convert consecutive repeated characters into character + count.

**Example:**
```text
Input: aaabbccccd
Output: a3b2c4d1
```

### 18. Find Duplicate Characters
Write a program that prints all characters that occur more than once.

**Example:**
```text
Input: programming

Output:
r
g
m
```

### 19. Word Frequency
Take a sentence and count how many times each word appears.

**Example:**
```text
Input:
python is easy and python is powerful

Output:
python: 2
is: 2
easy: 1
and: 1
powerful: 1
```

### 20. Username Generator
Create a program that generates a username from a user's full name.

Rules:
- Convert everything to lowercase
- Remove spaces
- Add the first two digits of the user's birth year

**Example:**
```text
Name: Farhan Khan
Birth Year: 2006

Output:
farhankhan06
```

---

# 📋 Lists — 20 Questions

### 1. Create and Print a List
Take 5 numbers from the user, store them in a list, and print the list.

### 2. Find Largest and Smallest
Take numbers from the user and find the largest and smallest values **without using `max()` or `min()`**.

### 3. Calculate Sum
Take a list of numbers and calculate their sum.

**Do not use `sum()`.**

### 4. Count Even and Odd Numbers
Given a list of integers, count how many numbers are even and how many are odd.

**Example:**
```text
Input: [1, 2, 3, 4, 5, 6]

Output:
Even: 3
Odd: 3
```

### 5. Remove Duplicates
Remove duplicate values from a list while preserving their original order.

**Example:**
```text
Input: [1, 2, 2, 3, 1, 4]
Output: [1, 2, 3, 4]
```

### 6. Reverse a List
Reverse a list using slicing.

### 7. Find the Second Largest
Find the second-largest number in a list.

**Example:**
```text
Input: [10, 5, 20, 8, 20, 15]
Output: 15
```

### 8. Search for an Element
Ask the user for a value and determine whether it exists in a list.

If found, print its index.

### 9. Count Occurrences
Count how many times a specific value occurs in a list.

**Example:**
```text
Input: [1, 2, 2, 3, 2, 4]
Search: 2

Output: 3
```

### 10. Separate Positive and Negative Numbers
Given a list, create two new lists:
```text
positive = [...]
negative = [...]
```

### 11. List Slicing
Given:
```python
numbers = [10, 20, 30, 40, 50, 60, 70, 80]
```

Write programs to print:
1. First 3 elements
2. Last 3 elements
3. Elements from index 2 to 5
4. Every second element
5. The list in reverse

### 12. Insert and Delete Elements
Create a program that allows the user to:
```text
1. Add an element
2. Insert an element
3. Remove an element
4. Remove the last element
5. Display the list
```

Use appropriate list methods.

### 13. Sort Without `sort()`
Sort a list of numbers in ascending order without using `sort()` or `sorted()`.

### 14. Merge Two Lists
Take two lists and create a third list containing elements from both.

**Example:**
```text
List 1: [1, 2, 3]
List 2: [4, 5, 6]

Output: [1, 2, 3, 4, 5, 6]
```

### 15. Common Elements
Find the elements that are common between two lists.

**Example:**
```text
List 1: [1, 2, 3, 4]
List 2: [3, 4, 5, 6]

Output: [3, 4]
```

### 16. List of Squares
Given a list of numbers, create a new list containing their squares.

**Example:**
```text
Input: [1, 2, 3, 4, 5]
Output: [1, 4, 9, 16, 25]
```

Use **list comprehension**.

### 17. Filter Numbers
Given a list of numbers, create a new list containing only numbers greater than 50.

Use **list comprehension**.

### 18. List of Dictionaries
Create a list containing information about 5 students.

Each student should contain:
```text
name
age
marks
```

Then print the student with the highest marks.

**Example structure:**
```python
students = [
    {"name": "Farhan", "age": 20, "marks": 85},
    {"name": "Ali", "age": 21, "marks": 92}
]
```

### 19. Shopping Cart
Create a shopping-cart program using a list.

The program should allow the user to:
```text
1. Add product
2. Remove product
3. View cart
4. Search product
5. Count products
6. Exit
```

### 20. Student Marks System
Create a program that stores multiple students in a list.

Each student should have:
```python
{
    "name": "...",
    "marks": [...]
}
```

The program should calculate and display:
- Each student's total
- Each student's average
- Highest-scoring student
- Lowest-scoring student
- Class average

---

# 📖 Dictionaries — 20 Questions

### 1. Create a Dictionary
Create a dictionary containing:
```text
name
age
city
course
```

Take all values from user input and print the dictionary.

### 2. Access a Value
Create:
```python
student = {
    "name": "Farhan",
    "age": 20,
    "course": "Python"
}
```

Ask the user for a key and print its value.

### 3. Check Key Existence
Ask the user for a key and check whether it exists in a dictionary.

**Example:**
```text
Key: age
Output: Key exists
```

### 4. Add a New Key
Given a dictionary, ask the user for a key and value and add them to the dictionary.

### 5. Update a Value
Given:
```python
student = {
    "name": "Farhan",
    "age": 20
}
```

Ask the user for a new age and update the dictionary.

### 6. Delete a Key
Create a program that asks the user for a key and removes it from the dictionary.

Handle the case where the key does not exist.

### 7. Print All Keys and Values
Given a dictionary, print all keys and values separately.

Use:
```python
keys()
values()
items()
```

### 8. Count Character Frequency
Take a string and create a dictionary containing the frequency of every character.

**Example:**
```text
Input: banana

Output:
{
    "b": 1,
    "a": 3,
    "n": 2
}
```

### 9. Word Frequency Dictionary
Take a sentence and create a dictionary containing the frequency of every word.

**Example:**
```text
Input:
python is easy python is fun

Output:
{
    "python": 2,
    "is": 2,
    "easy": 1,
    "fun": 1
}
```

### 10. Find Maximum Value
Given:
```python
marks = {
    "Farhan": 85,
    "Ali": 92,
    "John": 78,
    "Ahmed": 95
}
```

Find the student with the highest marks.

### 11. Find Minimum Value
Using the same dictionary, find the student with the lowest marks.

### 12. Calculate Dictionary Values
Given:
```python
prices = {
    "apple": 50,
    "banana": 30,
    "orange": 80
}
```

Calculate the total price.

### 13. Merge Dictionaries
Given two dictionaries, merge them into one dictionary.

Handle duplicate keys appropriately.

**Example:**
```python
a = {"name": "Farhan", "age": 20}
b = {"city": "Meerut", "course": "Python"}

Output:
{
    "name": "Farhan",
    "age": 20,
    "city": "Meerut",
    "course": "Python"
}
```

### 14. Dictionary Comprehension
Given:
```python
numbers = [1, 2, 3, 4, 5, 6]
```

Create:
```python
{
    1: 1,
    2: 4,
    3: 9,
    4: 16,
    5: 25,
    6: 36
}
```

using **dictionary comprehension**.

### 15. Filter Dictionary
Given:
```python
marks = {
    "Farhan": 85,
    "Ali": 45,
    "Ahmed": 92,
    "John": 38
}
```

Create a new dictionary containing only students who scored **60 or above**.

### 16. Nested Dictionary
Create a dictionary containing information about multiple students:

```python
students = {
    "farhan": {
        "age": 20,
        "marks": 85,
        "city": "Meerut"
    },
    "ali": {
        "age": 21,
        "marks": 92,
        "city": "Delhi"
    }
}
```

Ask the user for a student's name and print their:
- Age
- Marks
- City

### 17. Find Students by Marks
Given a nested dictionary of students, print the names of all students who scored more than 80.

### 18. Inventory System
Create a dictionary-based inventory system.

Each product should contain:
```text
product name
price
quantity
```

The program should allow:
```text
1. Add product
2. Update quantity
3. Update price
4. Search product
5. Delete product
6. Display inventory
7. Exit
```

### 19. Phone Book
Create a phone-book application using a dictionary.

The program should allow:
```text
1. Add contact
2. Search contact
3. Update contact
4. Delete contact
5. Display all contacts
6. Exit
```

Example:
```python
contacts = {
    "Farhan": "9876543210",
    "Ali": "9876501234"
}
```

### 20. Student Management System
Build a complete student-management program using a **list of dictionaries**.

Each student should contain:
```python
{
    "id": 101,
    "name": "Farhan",
    "age": 20,
    "marks": {
        "python": 85,
        "math": 90,
        "english": 78
    }
}
```

Implement:
```text
1. Add student
2. Search student by ID
3. Search student by name
4. Update student
5. Delete student
6. Display all students
7. Calculate student's total marks
8. Calculate student's average
9. Find highest-scoring student
10. Find lowest-scoring student
11. Find class average
12. Exit
```

---

# 🎯 Methods & Concepts Covered

| Topic | Important methods/concepts |
|---|---|
| **Strings** | `lower()` |
| | `upper()` |
| | `capitalize()` |
| | `title()` |
| | `strip()` |
| | `split()` |
| | `join()` |
| | `replace()` |
| | `find()` |
| | `rfind()` |
| | `count()` |
| | `startswith()` |
| | `endswith()` |
| | `isalpha()` |
| | `isdigit()` |
| | `isalnum()` |
| | `isspace()` |
| | Indexing |
| | Slicing |
| | String formatting |
| **Lists** | `append()` |
| | `insert()` |
| | `extend()` |
| | `remove()` |
| | `pop()` |
| | `clear()` |
| | `index()` |
| | `count()` |
| | `sort()` |
| | `reverse()` |
| | Membership `in` |
| | Indexing |
| | Slicing |
| | List concatenation |
| | List comprehension |
| | Nested lists |
| | List of dictionaries |
| **Dictionaries** | `get()` |
| | `keys()` |
| | `values()` |
| | `items()` |
| | `update()` |
| | `pop()` |
| | `popitem()` |
| | `setdefault()` |
| | `clear()` |
| | Membership `in` |
| | Dictionary comprehension |
| | Nested dictionaries |
| | Dictionaries + lists |
| | Lists + dictionaries |
| | Frequency counting |
| | Searching/filtering |
| | CRUD operations |

---

# 📚 Recommended Practice Order

1. **Strings — Questions 1–20**
2. **Lists — Questions 1–20**
3. **Dictionaries — Questions 1–20**
4. **List of Dictionaries**
5. **Nested Dictionaries**
6. **Mini Projects**

The final questions are designed to move from basic method usage toward practical programming and CRUD-style applications.
