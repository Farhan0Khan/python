
> **Purpose:** A structured revision guide, ordered from beginner fundamentals to intermediate Python concepts.  
> **Format:** Definitions, syntax patterns, and reminders only — no worked code examples.

---

## 1. Introduction to Python 🌱

### 1.1 What is Python?
**Definition:** Python is a high-level, general-purpose programming language known for readable syntax and a large standard library.

### 1.2 Features of Python
- **Readable syntax:** Designed to be relatively easy to read and write.
- **Interpreted execution:** Common Python implementations execute code through an interpreter/runtime.
- **Dynamically typed:** Variable names are not permanently bound to one declared type.
- **Strongly typed:** Operations generally do not silently treat unrelated types as interchangeable.
- **Multi-paradigm:** Supports procedural, object-oriented, and functional programming styles.
- **Cross-platform:** Runs on major operating systems.
- **Large ecosystem:** Provides a standard library and third-party packages.
- **Automatic memory management:** Uses memory-management mechanisms including reference counting and garbage collection in CPython.

### 1.3 Demand and uses of Python
**Definition:** Python is widely used because it supports rapid development and has mature libraries across many domains. Demand varies by region, industry, and role.

**Application areas:** Web development, automation, scripting, data analysis, AI and machine learning, scientific computing, testing, education, cybersecurity tooling, and desktop utilities.

### 1.4 History and future
- **History:** Created by Guido van Rossum; first publicly released in 1991.
- **Major milestone:** Python 3 was released in 2008 and is the modern language family.
- **Future outlook:** Python is likely to remain important in automation, data, AI, education, and backend development, though no language’s future demand is guaranteed.
- **Version awareness:** Learn current Python 3 practices and check compatibility when using libraries or older environments.

### 1.5 Advantages and limitations
**Advantages:** Readability, fast development, extensive libraries, portability, community support, and versatility.

**Limitations:** Often slower than compiled languages for CPU-heavy tasks, can use substantial memory, has runtime type errors, and is not ideal for every mobile, embedded, or performance-critical use case.

---

## 2. How Python Organizes Code 🧱

### 2.1 Statements, expressions, and comments
- **Statement:** An instruction that performs an action.
- **Expression:** A combination of values and operations that produces a value.
- **Comment:** Explanatory text ignored by the Python interpreter.
- **Docstring:** A string used to document a module, class, or function.

### 2.2 Indentation and blocks
**Definition:** Python uses indentation to group statements into blocks rather than braces.

**Syntax pattern:** A block begins after a colon (`:`); its statements are consistently indented.

### 2.3 Names, variables, and assignment
- **Variable/name:** A name bound to an object.
- **Assignment:** Binds a name to an object or updates its binding.
- **Naming rules:** Names are case-sensitive, cannot begin with a digit, and cannot be Python keywords.
- **Naming convention:** Use `snake_case` for variables and functions; use descriptive names.

### 2.4 Keywords and identifiers
- **Keyword:** A reserved word with a special meaning in Python.
- **Identifier:** A user-defined name for an object, function, class, module, or other entity.

### 2.5 Input and output
- **`print()`**: Displays information.
- **`input()`**: Reads user input and returns it as a string.
- **Formatting output:** Understand f-strings, format specifications, separators, and line endings.

### 2.6 Errors and debugging basics
- **Syntax error:** Code does not follow Python grammar.
- **Runtime exception:** An error occurs while code is running.
- **Logical error:** The program runs but produces an incorrect result.
- Learn to read tracebacks, identify the relevant line, and distinguish error types.

---

## 3. Data Types and Object Model 🧬

### 3.1 The correct mental model
**Important correction:** Python variables are names bound to objects. Objects live in memory, but it is misleading to classify Python types simply as “primitive/stack” versus “reference/heap.” Python does not expose a universal stack-versus-heap rule for each type.

- **Dynamic typing:** A name can be rebound to an object of another type.
- **Mutability:** Whether an object can change after creation.
- **Identity:** The identity of a particular object.
- **Type:** The category that defines an object’s behavior and operations.
- **Assignment and aliasing:** Multiple names can refer to the same object.

### 3.2 Numeric types
- **`int` — Integer:** Whole numbers with arbitrary precision, limited in practice by available memory.
- **`float` — Floating-point:** Approximate real-number representation.
- **`complex` — Complex number:** A number with real and imaginary components.
- **`bool` — Boolean:** Represents `True` or `False`; it is a subclass of `int`.
- **`NoneType`:** The type of the single value `None`, commonly used to represent absence of a value.

### 3.3 Sequence types
- **`str` — String:** Immutable sequence of Unicode characters.
- **`list` — List:** Mutable, ordered sequence.
- **`tuple` — Tuple:** Immutable, ordered sequence.
- **`range` — Range:** Immutable sequence-like representation of an arithmetic progression.

### 3.4 Set types
- **`set` — Set:** Mutable collection of unique, hashable elements; unordered.
- **`frozenset` — Frozen set:** Immutable set of unique, hashable elements.

### 3.5 Mapping type
- **`dict` — Dictionary:** Mutable mapping of unique, hashable keys to values. Insertion order is preserved in modern Python.

### 3.6 Binary and other built-in types
- **`bytes`:** Immutable sequence of byte values.
- **`bytearray`:** Mutable sequence of byte values.
- **`memoryview`:** Provides access to binary data without necessarily copying it.
- **Functions:** Functions are objects and can be assigned to names, passed as arguments, and returned.
- **Classes and instances:** Classes define custom types; instances are objects created from classes.
- **Modules:** Objects that provide a namespace for Python definitions.

### 3.7 Mutable versus immutable
- **Immutable:** An object cannot be changed after it is created. Common examples include `int`, `float`, `bool`, `complex`, `str`, `tuple` (its contained objects may still be mutable), `bytes`, and `frozenset`.
- **Mutable:** An object can be changed after creation. Common examples include `list`, `dict`, `set`, and `bytearray`.
- **Hashability:** A hashable object has a stable hash during its lifetime and can be used as a dictionary key or set element. Immutability alone does not guarantee hashability in every case.

### 3.8 Type inspection
- **`type()`**: Returns an object’s type.
- **`isinstance()`**: Checks whether an object is an instance of a type or a compatible subclass.
- **`id()`**: Returns an identity value for an object during its lifetime; do not use it as a permanent identifier.

---

## 4. Operators and Expressions ⚙️

### 4.1 Arithmetic operators
- `+` addition
- `-` subtraction
- `*` multiplication
- `/` true division
- `//` floor division
- `%` remainder (modulo)
- `**` exponentiation
- Unary `+` and `-` for sign

### 4.2 Comparison operators
- `==` equal to
- `!=` not equal to
- `<` less than
- `>` greater than
- `<=` less than or equal to
- `>=` greater than or equal to

**Reminder:** Comparisons produce Boolean results. Chained comparisons are supported.

### 4.3 Assignment operators
- `=` assignment
- `+=`, `-=`, `*=`, `/=`, `//=`, `%=`, `**=`
- `&=`, `|=`, `^=`, `<<=`, `>>=`
- `:=` assignment expression (the “walrus” operator)

### 4.4 Logical operators
- `and` — logical conjunction
- `or` — logical disjunction
- `not` — logical negation

**Reminder:** `and` and `or` short-circuit and may return one of their operands, not necessarily a `bool`.

### 4.5 Bitwise operators
- `&` bitwise AND
- `|` bitwise OR
- `^` bitwise XOR
- `~` bitwise inversion
- `<<` left shift
- `>>` right shift

### 4.6 Membership operators
- `in` — checks membership
- `not in` — checks non-membership

### 4.7 Identity operators
- `is` — checks whether two references point to the same object
- `is not` — checks whether they point to different objects

**Important:** Use equality (`==`) to compare values; use identity (`is`) when object identity is what matters, especially for `None`.

### 4.8 Operator precedence
**Definition:** Precedence determines which operations are grouped first. Parentheses make intended grouping clearer. Learn the precedence order for arithmetic, shifts, bitwise, comparisons, Boolean operators, and assignment expressions.

---

## 5. Type Conversion and Casting 🔄

### 5.1 Implicit conversion
**Definition:** Python may automatically convert certain compatible numeric values during an operation, such as combining an integer and a float.

### 5.2 Explicit conversion
**Definition:** Explicit conversion requests a new representation or type using a constructor or conversion function.

Common conversions:
- `int()` — integer conversion
- `float()` — floating-point conversion
- `complex()` — complex-number conversion
- `str()` — string representation
- `bool()` — truth-value conversion
- `list()` — list construction
- `tuple()` — tuple construction
- `set()` — set construction
- `dict()` — dictionary construction from suitable input
- `bytes()` and `bytearray()` — binary data construction

### 5.3 Conversion cautions
- Not every value can be converted to every type.
- Some conversions lose information, such as converting a float to an integer.
- `str(value)` creates a string representation; it does not guarantee a reversible conversion.
- `bool()` follows truth-value rules; empty collections, zero, `None`, and `False` are falsy, while most other objects are truthy.

---

import pypandoc

content = r"""# Python Strings and Collections — Detailed Notes 🐍

## 6. Strings, Indexing, and Slicing 🔤

## 6.1 String Fundamentals

### Definition
A **string (`str`)** is an immutable sequence of Unicode characters. Strings represent text and support indexing, slicing, iteration, searching, formatting, and many other operations.

### String syntax

```python
single = 'Hello'
double = "Python"
multiline = """This is
a multiline string."""
```

Single and double quotes both create strings. Triple quotes are commonly used for multiline strings and docstrings.

### Escape sequences

Escape sequences represent special characters inside string literals.

| Sequence | Meaning |
|---|---|
| `\n` | New line |
| `\t` | Horizontal tab |
| `\\` | Backslash |
| `\'` | Single quote |
| `\"` | Double quote |
| `\r` | Carriage return |
| `\b` | Backspace |
| `\0` | Null character |
| `\uXXXX` | Unicode character using four hexadecimal digits |
| `\UXXXXXXXX` | Unicode character using eight hexadecimal digits |

```python
message = "Hello\nPython"
path = "C:\\Users\\Student"
```

### Raw strings

A raw string reduces the special interpretation of backslashes. It is often useful for regular expressions and Windows-style paths.

```python
path = r"C:\Users\Student"
```

A raw string cannot end with an odd number of backslashes because the final backslash would escape the closing quote.

### String immutability

A string cannot be changed in place. Operations that appear to modify a string create a new string instead.

```python
word = "python"
word = word.upper()
```

The second statement binds `word` to a new string. It does not mutate the original string object.

### String length

```python
text = "Python"
print(len(text))  # 6
```

`len()` returns the number of Unicode code points in the string, not necessarily the number of user-perceived characters. Some visible characters consist of multiple code points.

---

## 6.2 String Indexing

### Definition
**Indexing** accesses one character from a sequence by its position.

### Syntax

```python
string[index]
```

```python
word = "PYTHON"

print(word[0])   # P
print(word[1])   # Y
print(word[-1])  # N
print(word[-2])  # O
```

### Index rules

- Positive indexing starts at `0` from the beginning.
- Negative indexing starts at `-1` from the end.
- The last positive index is `len(string) - 1`.
- The first negative index is `-len(string)`.
- An index outside the valid range raises `IndexError`.
- Strings are immutable, so assigning to an indexed position raises `TypeError`.

```python
word = "PYTHON"

# word[0] = "p"  # TypeError: strings cannot be changed in place
```

### Index positions

For the string `"PYTHON"`:

| Character | P | Y | T | H | O | N |
|---|---:|---:|---:|---:|---:|---:|
| Positive index | 0 | 1 | 2 | 3 | 4 | 5 |
| Negative index | -6 | -5 | -4 | -3 | -2 | -1 |

### Safe access

Use a length check or exception handling when an index may be invalid. Do not assume every string contains a character at a particular position.

---

## 6.3 String Slicing

### Definition
**Slicing** extracts a portion of a sequence using a start position, stop position, and optional step.

### Syntax

```python
sequence[start:stop:step]
```

- `start`: Index where slicing begins; included.
- `stop`: Index where slicing ends; excluded.
- `step`: Distance and direction between selected positions.
- Omitted `start`, `stop`, or `step` values use defaults.
- The default step is `1`.
- A step of `0` raises `ValueError`.
- Out-of-range slice boundaries are normally handled without `IndexError`.

```python
word = "PYTHON"

print(word[0:3])   # PYT
print(word[2:])    # THON
print(word[:4])    # PYTH
print(word[::2])  # PTO
print(word[::-1]) # NOHTYP
```

### Common slicing patterns

| Pattern | Meaning |
|---|---|
| `text[:]` | Select the whole sequence (shallow copy for lists; a string result for strings) |
| `text[start:]` | From `start` to the end |
| `text[:stop]` | From the beginning up to, but excluding, `stop` |
| `text[start:stop]` | Select the specified interval |
| `text[::step]` | Select using a step |
| `text[::-1]` | Reverse the sequence |
| `text[-n:]` | Select the last `n` items |
| `text[:-n]` | Exclude the last `n` items |

### Negative steps

A negative step traverses the sequence backwards. Choose boundaries carefully because the stop position remains excluded.

### Slicing versus indexing

- Indexing returns one element and can raise `IndexError`.
- Slicing returns a sequence section and generally tolerates out-of-range boundaries.
- For strings, both return strings.

---

## 6.4 String Operators and Membership

```python
first = "Hello"
second = "Python"

print(first + " " + second)  # Hello Python
print("ha" * 3)              # hahaha
print("Py" in second)        # True
print("Java" not in second)  # True
```

| Operation | Purpose |
|---|---|
| `+` | Concatenate strings |
| `*` | Repeat a string |
| `in` | Test whether a substring exists |
| `not in` | Test whether a substring does not exist |
| `==`, `!=` | Compare string values |
| `<`, `>`, `<=`, `>=` | Lexicographic comparison |

String comparisons are lexicographic and case-sensitive. For case-insensitive comparison, normalize both strings, for example with `.casefold()`.

---

## 6.5 String Methods — Complete Practical Reference

String methods do not mutate the original string. They return a new string or another result.

### A. Case conversion

| Method | Purpose | Example result |
|---|---|---|
| `upper()` | Convert letters to uppercase | `"hello".upper()` → `"HELLO"` |
| `lower()` | Convert letters to lowercase | `"HELLO".lower()` → `"hello"` |
| `capitalize()` | Capitalize the first character and lowercase the rest | `"pYTHON".capitalize()` → `"Python"` |
| `title()` | Convert words to title case | `"hello world".title()` → `"Hello World"` |
| `swapcase()` | Reverse the case of letters | `"PyThOn".swapcase()` → `"pYtHoN"` |
| `casefold()` | Aggressive normalization for caseless comparison | `"HELLO".casefold()` → `"hello"` |

### B. Removing surrounding characters

| Method | Purpose | Example result |
|---|---|---|
| `strip()` | Remove surrounding whitespace or specified characters | `"  hi  ".strip()` → `"hi"` |
| `lstrip()` | Remove from the left side | `"  hi".lstrip()` → `"hi"` |
| `rstrip()` | Remove from the right side | `"hi  ".rstrip()` → `"hi"` |

**Important:** The optional argument to `strip()`, `lstrip()`, and `rstrip()` is a set of characters to remove, not a literal prefix or suffix.

### C. Searching and counting

| Method | Purpose | Example result |
|---|---|---|
| `find(sub)` | First matching index, or `-1` | `"banana".find("na")` → `2` |
| `rfind(sub)` | Last matching index, or `-1` | `"banana".rfind("na")` → `4` |
| `index(sub)` | First matching index; raises `ValueError` if absent | `"banana".index("na")` → `2` |
| `rindex(sub)` | Last matching index; raises `ValueError` if absent | `"banana".rindex("na")` → `4` |
| `count(sub)` | Count non-overlapping occurrences | `"banana".count("na")` → `2` |

Some searching methods accept optional `start` and `end` boundaries.

### D. Prefix and suffix checks

| Method | Purpose |
|---|---|
| `startswith(prefix)` | Test whether a string starts with a prefix |
| `endswith(suffix)` | Test whether a string ends with a suffix |

Both return a Boolean and can accept a tuple of alternatives.

```python
filename = "report.pdf"
print(filename.endswith(".pdf"))  # True
```

### E. Replacing and translating

| Method | Purpose |
|---|---|
| `replace(old, new)` | Replace occurrences of a substring |
| `maketrans()` | Build a translation table |
| `translate(table)` | Translate or remove characters using a translation table |

```python
text = "I like Java"
print(text.replace("Java", "Python"))  # I like Python
```

`replace()` returns a new string. It does not modify the original.

### F. Splitting and joining

| Method | Purpose |
|---|---|
| `split(sep=None, maxsplit=-1)` | Split from the left into a list |
| `rsplit(sep=None, maxsplit=-1)` | Split from the right |
| `splitlines()` | Split at line boundaries |
| `partition(sep)` | Split into a 3-item tuple at the first separator |
| `rpartition(sep)` | Split into a 3-item tuple at the last separator |
| `join(iterable)` | Join strings using the string as a separator |

```python
sentence = "red,green,blue"
print(sentence.split(","))  # ['red', 'green', 'blue']

words = ["Learn", "Python"]
print(" ".join(words))  # Learn Python
```

**Common mistake:** `join()` is called on the separator string, and the iterable must contain strings.

### G. Alignment and padding

| Method | Purpose |
|---|---|
| `center(width, fillchar=' ')` | Center text within a width |
| `ljust(width, fillchar=' ')` | Left-align text |
| `rjust(width, fillchar=' ')` | Right-align text |
| `zfill(width)` | Pad the left side with zeroes |
| `expandtabs(tabsize=8)` | Expand tab characters |

```python
print("42".zfill(5))  # 00042
```

### H. Character classification

These methods return `True` or `False`.

| Method | Returns `True` when… |
|---|---|
| `isalpha()` | All characters are alphabetic and the string is non-empty |
| `isalnum()` | All characters are alphabetic or numeric and the string is non-empty |
| `isascii()` | All characters are ASCII (empty strings also return `True`) |
| `isdecimal()` | All characters are decimal characters and the string is non-empty |
| `isdigit()` | All characters are digit characters and the string is non-empty |
| `isnumeric()` | All characters are numeric characters and the string is non-empty |
| `isidentifier()` | The string is a valid Python identifier |
| `islower()` | Cased characters are lowercase and at least one cased character exists |
| `isupper()` | Cased characters are uppercase and at least one cased character exists |
| `istitle()` | The string follows title-case rules |
| `isspace()` | All characters are whitespace and the string is non-empty |
| `isprintable()` | All characters are printable (empty strings return `True`) |

`isdecimal()`, `isdigit()`, and `isnumeric()` are related but not identical. For ordinary decimal digits, `isdecimal()` is the narrowest of the three.

### I. String formatting

#### F-strings

F-strings embed expressions inside braces.

```python
name = "Aisha"
age = 20
print(f"{name} is {age} years old.")
```

#### Format specifications

```python
price = 12.5
print(f"Price: {price:.2f}")  # Price: 12.50
```

Learn width, alignment, precision, thousands separators, and numeric formatting.

#### `format()` method

```python
print("Hello, {}".format("Python"))
```

#### Percent formatting

Older formatting style still appears in existing code, but f-strings are generally preferred for new code.

### J. Other string-related operations

- `ord(character)`: Return the Unicode code point of a character.
- `chr(number)`: Return the character for a valid Unicode code point.
- `len(string)`: Return the number of code points.
- `str(value)`: Create a string representation of a value.

### String practice checklist

- [ ] Explain string immutability.
- [ ] Use positive and negative indexing.
- [ ] Slice with positive and negative steps.
- [ ] Search, replace, split, and join text.
- [ ] Validate text with classification methods.
- [ ] Format values using f-strings.
- [ ] Distinguish `find()` from `index()`.
- [ ] Distinguish `strip()` from prefix/suffix removal.

---

# 7. Core Collections: Lists, Tuples, Sets, and Dictionaries 📦

## 7.1 Lists

### Definition
A **list (`list`)** is a mutable, ordered sequence that permits duplicate elements and can contain objects of different types.

### Syntax

```python
numbers = [10, 20, 30]
mixed = [1, "Python", True]
empty = []
```

### Accessing list elements

```python
fruits = ["apple", "banana", "mango"]

print(fruits[0])    # apple
print(fruits[-1])   # mango
print(fruits[0:2])  # ['apple', 'banana']
```

Lists support indexing and slicing. Indexing outside the valid range raises `IndexError`.

### Updating list elements

```python
fruits = ["apple", "banana", "mango"]
fruits[1] = "orange"
```

Lists are mutable, so elements can be replaced, inserted, or removed.

### List methods

| Method | Purpose | Important detail |
|---|---|---|
| `append(x)` | Add one item to the end | Adds `x` as one item, even if it is a list |
| `extend(iterable)` | Add each item from an iterable | Expands the iterable into the list |
| `insert(i, x)` | Insert an item at an index | Existing items shift right |
| `remove(x)` | Remove the first matching value | Raises `ValueError` if not found |
| `pop([i])` | Remove and return an item | Defaults to the last item; invalid index raises `IndexError` |
| `clear()` | Remove all items | Leaves an empty list |
| `index(x[, start[, end]])` | Find the first matching index | Raises `ValueError` if absent |
| `count(x)` | Count equal items | Returns an integer |
| `sort(key=None, reverse=False)` | Sort the list in place | Returns `None` |
| `reverse()` | Reverse the list in place | Returns `None` |
| `copy()` | Create a shallow copy | Nested objects are shared |

### List method examples

```python
numbers = [1, 2]
numbers.append(3)
print(numbers)  # [1, 2, 3]

numbers.extend([4, 5])
print(numbers)  # [1, 2, 3, 4, 5]

numbers.insert(1, 99)
print(numbers)  # [1, 99, 2, 3, 4, 5]

numbers.remove(99)
last = numbers.pop()
print(last)     # 5
```

### Sorting

```python
numbers = [4, 1, 3, 2]
numbers.sort()
print(numbers)  # [1, 2, 3, 4]

numbers.sort(reverse=True)
print(numbers)  # [4, 3, 2, 1]
```

`sort()` changes the list in place and returns `None`. By contrast, `sorted(iterable)` returns a new sorted list.

```python
numbers = [4, 1, 3]
result = sorted(numbers)
print(result)   # [1, 3, 4]
print(numbers)  # [4, 1, 3]
```

### Common list operations

```python
a = [1, 2]
b = [3, 4]

print(a + b)       # [1, 2, 3, 4]
print(a * 3)       # [1, 2, 1, 2, 1, 2]
print(2 in a)      # True
print(len(a))      # 2
```

### List comprehensions

A list comprehension creates a list from an iterable, optionally filtering items.

```python
squares = [n * n for n in range(1, 6)]
print(squares)  # [1, 4, 9, 16, 25]

evens = [n for n in range(10) if n % 2 == 0]
print(evens)  # [0, 2, 4, 6, 8]
```

### Nested lists

A nested list contains other lists.

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

print(matrix[0][1])  # 2
```

### Aliasing and copying

```python
original = [1, 2, 3]
alias = original
alias.append(4)

print(original)  # [1, 2, 3, 4]
```

`alias` and `original` refer to the same list.

```python
original = [1, 2, 3]
copy_list = original.copy()
copy_list.append(4)

print(original)   # [1, 2, 3]
print(copy_list)  # [1, 2, 3, 4]
```

`copy()` is shallow. For nested lists, inner lists are still shared.

### Shallow versus deep copy

```python
import copy

original = [[1, 2], [3, 4]]
shallow = original.copy()
deep = copy.deepcopy(original)
```

- A shallow copy creates a new outer list but shares nested objects.
- A deep copy recursively copies nested objects where supported.

### List pitfalls

- `append([3, 4])` adds one nested list; `extend([3, 4])` adds two elements.
- `remove()` removes by value; `pop()` removes by index and returns the removed value.
- `sort()` returns `None`; do not assign its return value to the list variable.
- A list slice creates a shallow copy, not a deep copy.
- Avoid modifying a list while iterating over it unless the behavior is deliberate.

---

## 7.2 Tuples

### Definition
A **tuple (`tuple`)** is an ordered sequence that cannot be structurally changed after creation. It permits duplicate elements and can contain values of different types.

### Syntax

```python
coordinates = (10, 20)
empty_tuple = ()
single_item = (5,)
also_tuple = 5, 6, 7
```

**Important:** A single-item tuple needs a trailing comma. Parentheses alone do not make an expression a tuple.

### Indexing and slicing

```python
colors = ("red", "green", "blue")

print(colors[0])    # red
print(colors[-1])   # blue
print(colors[0:2])  # ('red', 'green')
```

### Tuple packing and unpacking

```python
person = ("Ali", 21)  # Packing
name, age = person    # Unpacking
```

The number of targets must match the number of values unless extended unpacking is used.

```python
first, *middle, last = (1, 2, 3, 4, 5)
```

### Tuple methods

Tuples have only two main methods:

| Method | Purpose |
|---|---|
| `count(value)` | Count occurrences of a value |
| `index(value[, start[, end]])` | Find the first matching index; raises `ValueError` if absent |

```python
numbers = (1, 2, 2, 3)
print(numbers.count(2))  # 2
print(numbers.index(3))  # 3
```

### Tuple operators

```python
a = (1, 2)
b = (3, 4)

print(a + b)   # (1, 2, 3, 4)
print(a * 2)   # (1, 2, 1, 2)
print(2 in a)  # True
print(len(a))  # 2
```

### Immutability does not freeze nested objects

```python
data = ([1, 2], "Python")
data[0].append(3)

print(data)  # ([1, 2, 3], 'Python')
```

The tuple structure remains fixed, but the contained list can change.

### When to use tuples

- Fixed records or grouped values
- Returning multiple values from a function
- Data that should not be structurally changed
- Dictionary keys, only when all contained elements are hashable

---

## 7.3 Sets and Frozensets

### Definition
A **set (`set`)** is a mutable collection of unique, hashable elements. Sets do not provide positional indexing and do not guarantee a meaningful positional order.

### Syntax

```python
numbers = {1, 2, 3}
empty_set = set()
unique = set([1, 1, 2, 3])

print(unique)  # {1, 2, 3} (display order may vary)
```

`{}` creates an empty dictionary, not an empty set.

### Set methods

| Method | Purpose | Important detail |
|---|---|---|
| `add(x)` | Add one element | Duplicates do not create extra elements |
| `update(iterable, ...)` | Add elements from one or more iterables | Mutates the set |
| `remove(x)` | Remove an element | Raises `KeyError` if absent |
| `discard(x)` | Remove an element if present | Does not raise an error if absent |
| `pop()` | Remove and return an arbitrary element | Raises `KeyError` if empty |
| `clear()` | Remove all elements | Leaves an empty set |
| `copy()` | Make a shallow copy | Elements are shared references |

### Set method examples

```python
numbers = {1, 2, 3}
numbers.add(4)
numbers.update([4, 5, 6])
numbers.discard(2)
print(numbers)  # {1, 3, 4, 5, 6} (display order may vary)
```

### Set mathematical operations

Let `a = {1, 2, 3}` and `b = {3, 4, 5}`.

| Operation | Operator | Method |
|---|---|---|
| Union | `a \| b` | `a.union(b)` |
| Intersection | `a & b` | `a.intersection(b)` |
| Difference | `a - b` | `a.difference(b)` |
| Symmetric difference | `a ^ b` | `a.symmetric_difference(b)` |
| Subset | `a <= b` | `a.issubset(b)` |
| Proper subset | `a < b` | Strict subset comparison |
| Superset | `a >= b` | `a.issuperset(b)` |
| Proper superset | `a > b` | Strict superset comparison |
| Disjointness | — | `a.isdisjoint(b)` |

```python
a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)  # {1, 2, 3, 4, 5}
print(a & b)  # {3}
print(a - b)  # {1, 2}
print(a ^ b)  # {1, 2, 4, 5}
```

### In-place set operations

- `update()` or `|=` — union update
- `intersection_update()` or `&=` — intersection update
- `difference_update()` or `-=` — difference update
- `symmetric_difference_update()` or `^=` — symmetric-difference update

These operations mutate the existing set.

### Set membership and deduplication

```python
items = ["a", "b", "a", "c", "b"]
unique_items = set(items)

print("a" in unique_items)  # True
```

Converting a list to a set removes duplicates, but the set does not preserve the original list's positional ordering as a contract.

### Frozenset

A **`frozenset`** is an immutable set.

```python
fixed = frozenset([1, 2, 3])
print(2 in fixed)  # True
```

A frozenset supports set operations but does not provide mutating methods such as `add()` or `remove()`. A frozenset can be a dictionary key if its elements are hashable.

### Set pitfalls

- Set elements must be hashable.
- Lists and dictionaries cannot be set elements.
- Sets cannot be indexed or sliced.
- `remove()` raises `KeyError` when the item is absent; `discard()` does not.
- Do not rely on set display order.
- A set literal such as `{1, 2, 3}` is not a dictionary because it contains values rather than key-value pairs.

---

## 7.4 Dictionaries

### Definition
A **dictionary (`dict`)** is a mutable mapping that associates unique, hashable keys with values. Modern Python dictionaries preserve insertion order.

### Syntax

```python
person = {
    "name": "Sara",
    "age": 22,
    "city": "Delhi"
}

empty_dict = {}
```

### Accessing values

```python
person = {"name": "Sara", "age": 22}

print(person["name"])       # Sara
print(person.get("age"))    # 22
print(person.get("email"))  # None
```

- `dictionary[key]` raises `KeyError` if the key is missing.
- `dictionary.get(key)` returns `None` by default if the key is missing.
- `dictionary.get(key, default)` returns the specified default if the key is missing.

### Adding and updating values

```python
person = {"name": "Sara"}
person["age"] = 22
person["name"] = "Sana"
person.update({"city": "Delhi", "age": 23})
```

Assigning to an existing key updates its value. Assigning to a new key adds an entry.

### Dictionary methods

| Method | Purpose | Important detail |
|---|---|---|
| `get(key[, default])` | Retrieve a value safely | Does not raise `KeyError` for a missing key |
| `keys()` | Return a dynamic view of keys | View reflects later dictionary changes |
| `values()` | Return a dynamic view of values | View reflects later dictionary changes |
| `items()` | Return a dynamic view of key-value pairs | Iteration yields pairs |
| `update(other)` | Add or update entries | Mutates the dictionary |
| `setdefault(key[, default])` | Return the value; insert default if absent | Mutates only when key is missing |
| `pop(key[, default])` | Remove a key and return its value | Missing key raises `KeyError` unless default is supplied |
| `popitem()` | Remove and return the most recently inserted item | Raises `KeyError` if empty |
| `clear()` | Remove all entries | Leaves an empty dictionary |
| `copy()` | Make a shallow copy | Nested values are shared references |
| `fromkeys(iterable[, value])` | Create a dictionary with specified keys and a common value | The same value object is used for each key |

### Dictionary method examples

```python
person = {"name": "Sara", "age": 22}

print(person.keys())
print(person.values())
print(person.items())

person.setdefault("city", "Delhi")
person.update({"age": 23})
age = person.pop("age")

print(age)     # 23
print(person)  # {'name': 'Sara', 'city': 'Delhi'}
```

### Iterating through dictionaries

```python
person = {"name": "Sara", "age": 22}

for key in person:
    print(key)

for value in person.values():
    print(value)

for key, value in person.items():
    print(key, value)
```

By default, iterating over a dictionary produces its keys.

### Dictionary membership

```python
person = {"name": "Sara", "age": 22}

print("name" in person)       # True
print("Sara" in person)       # False
print("Sara" in person.values())  # True
```

`in` checks keys, not values.

### Dictionary comprehensions

```python
squares = {n: n * n for n in range(1, 5)}
print(squares)  # {1: 1, 2: 4, 3: 9, 4: 16}
```

### Nested dictionaries

```python
students = {
    "student1": {"name": "Ali", "marks": 85},
    "student2": {"name": "Sara", "marks": 92}
}

print(students["student2"]["marks"])  # 92
```

### Dictionary keys and hashability

Keys must be hashable. Common valid keys include strings, numbers, and tuples containing only hashable values. Lists, sets, and dictionaries cannot be keys.

### `fromkeys()` caution

```python
keys = ["a", "b", "c"]
data = dict.fromkeys(keys, [])
```

Every key refers to the same list object in this example. Mutating the list through one key affects what is seen through the others. Use a comprehension to create a separate list per key when that is the intended behavior.

### Dictionary views

`keys()`, `values()`, and `items()` return dynamic view objects rather than ordinary lists. They reflect dictionary changes. Convert them to a list if a separate list snapshot is required.

### Dictionary pitfalls

- Accessing a missing key with brackets raises `KeyError`.
- `in` checks keys by default.
- Keys must be hashable.
- `copy()` is shallow.
- `popitem()` removes the most recently inserted entry in modern Python.
- `setdefault()` inserts a key if it is missing; it is not just a read operation.

---

## 7.5 Choosing the Right Collection

| Feature | List | Tuple | Set | Dictionary |
|---|---|---|---|---|
| Main purpose | Ordered collection | Fixed ordered collection | Unique elements | Key-value mapping |
| Mutable container | Yes | No | Yes | Yes |
| Allows duplicates | Yes | Yes | No | Keys are unique |
| Indexing | Yes | Yes | No | Access by key |
| Slicing | Yes | Yes | No | No |
| Membership | Checks elements | Checks elements | Checks elements | Checks keys by default |
| Typical syntax | `[1, 2]` | `(1, 2)` | `{1, 2}` | `{"a": 1}` |
| Empty form | `[]` | `()` | `set()` | `{}` |

### Quick decision guide

- Need an ordered, changeable sequence? Use a **list**.
- Need an ordered sequence that should not be structurally changed? Consider a **tuple**.
- Need unique values and set mathematics? Use a **set**.
- Need to associate keys with values? Use a **dictionary**.

---

## 7.6 Shared Collection Concepts

### Iteration

All four collection types can be iterated over.

```python
for item in ["a", "b", "c"]:
    print(item)
```

Dictionaries iterate over keys by default; use `.values()` or `.items()` when needed.

### Truthiness

Empty built-in collections are falsy; non-empty collections are truthy.

```python
items = []

if not items:
    print("The collection is empty")
```

### Copying and aliasing

Assignment creates another name for the same object; it does not copy a collection.

```python
a = [1, 2]
b = a
b.append(3)

print(a)  # [1, 2, 3]
```

### Shallow copies

Common shallow-copy techniques include:
- `list.copy()`
- `dictionary.copy()`
- Slicing a list
- The `copy.copy()` function

Shallow copies create a new outer container but share nested objects.

### Deep copies

`copy.deepcopy()` recursively copies objects where supported. Deep copying is not always necessary or appropriate, particularly for resources or objects that should be shared.

### Complexity awareness

Typical average-case performance:
- List indexing: **O(1)**
- List search: **O(n)**
- Appending to a list: **amortized O(1)**
- Dictionary key lookup: **average O(1)**
- Set membership: **average O(1)**

These are typical implementation-level expectations, not guarantees for every possible case.

---

## 7.7 Common Mistakes — Revision Table ⚠️

| Mistake | Correct understanding |
|---|---|
| Using `{}` for an empty set | Use `set()` |
| Assuming tuples cannot contain lists | Tuples can contain mutable objects |
| Using `remove()` when an index is needed | Use `pop(index)` to remove and return by position |
| Expecting `sort()` to return a sorted list | `sort()` mutates and returns `None`; use `sorted()` for a new list |
| Thinking `append()` and `extend()` are identical | `append()` adds one item; `extend()` adds items from an iterable |
| Assuming `dict[key]` is safe for missing keys | Use `get()` or handle `KeyError` |
| Assuming dictionary membership checks values | It checks keys by default |
| Expecting a set to preserve positional order | Sets do not provide positional ordering guarantees |
| Assuming `copy()` copies nested objects recursively | It is a shallow copy |
| Assuming a string method changes the original string | Strings are immutable; methods return results |
| Assuming `strip("abc")` removes the exact substring `"abc"` | It removes any of those characters from both ends |
| Assuming `find()` raises an exception when not found | `find()` returns `-1`; `index()` raises `ValueError` |

---

## 7.8 Practice Checklist ✅

### Strings
- [ ] Explain string immutability and Unicode.
- [ ] Use positive and negative indexing.
- [ ] Slice using start, stop, and step.
- [ ] Apply case conversion and whitespace removal.
- [ ] Search, count, replace, split, and join strings.
- [ ] Use classification methods and f-strings.
- [ ] Explain the difference between `find()` and `index()`.

### Lists
- [ ] Create, index, slice, update, and iterate through lists.
- [ ] Explain `append()` versus `extend()`.
- [ ] Explain `remove()` versus `pop()`.
- [ ] Use sorting, list comprehensions, and nested lists.
- [ ] Explain aliasing, shallow copy, and deep copy.

### Tuples
- [ ] Create empty, single-item, and multi-item tuples.
- [ ] Index, slice, pack, and unpack tuples.
- [ ] Explain tuple immutability and nested mutable objects.

### Sets
- [ ] Create sets and remove duplicates.
- [ ] Add and remove elements safely.
- [ ] Use union, intersection, difference, and symmetric difference.
- [ ] Explain set hashability and `frozenset`.

### Dictionaries
- [ ] Create, access, add, update, and delete entries.
- [ ] Use `get()`, `setdefault()`, `pop()`, and `update()`.
- [ ] Iterate over keys, values, and items.
- [ ] Explain key hashability, dynamic views, and shallow copies.

---

## 8. Quick Method Summary 🧾

### Strings
`capitalize()`, `casefold()`, `center()`, `count()`, `encode()`, `endswith()`, `expandtabs()`, `find()`, `format()`, `format_map()`, `index()`, `isalnum()`, `isalpha()`, `isascii()`, `isdecimal()`, `isdigit()`, `isidentifier()`, `islower()`, `isnumeric()`, `isprintable()`, `isspace()`, `istitle()`, `isupper()`, `join()`, `ljust()`, `lower()`, `lstrip()`, `maketrans()`, `partition()`, `removeprefix()`, `removesuffix()`, `replace()`, `rfind()`, `rindex()`, `rjust()`, `rpartition()`, `rsplit()`, `rstrip()`, `split()`, `splitlines()`, `startswith()`, `strip()`, `swapcase()`, `title()`, `translate()`, `upper()`, `zfill()`.

### Lists
`append()`, `clear()`, `copy()`, `count()`, `extend()`, `index()`, `insert()`, `pop()`, `remove()`, `reverse()`, `sort()`.

### Tuples
`count()`, `index()`.

### Sets
`add()`, `clear()`, `copy()`, `difference()`, `difference_update()`, `discard()`, `intersection()`, `intersection_update()`, `isdisjoint()`, `issubset()`, `issuperset()`, `pop()`, `remove()`, `symmetric_difference()`, `symmetric_difference_update()`, `union()`, `update()`.

### Dictionaries
`clear()`, `copy()`, `fromkeys()`, `get()`, `items()`, `keys()`, `pop()`, `popitem()`, `setdefault()`, `update()`, `values()`.

> **Note:** This guide covers the standard methods for these built-in types. Some methods have optional arguments and behavior that depends on the input; consult Python's official documentation when you need exact edge-case details.
"""

output_path = "/mnt/data/python_strings_collections_detailed.md"
pypandoc.convert_text(content, "md", format="md", outputfile=output_path, extra_args=["--standalone"])
print(f"Created: {output_path}")


## 8. Conditional Statements and Boolean Logic 🚦

### 8.1 Truth values
**Definition:** Conditions are evaluated for truthiness. Falsy values include `False`, `None`, numeric zero, and empty built-in collections or strings.

### 8.2 `if`, `elif`, and `else`
**Definition:** Conditional statements select which block runs based on conditions.

**Syntax pattern:** `if condition: ...`, followed by optional `elif condition: ...` and `else: ...`.

### 8.3 Nested conditionals
**Definition:** A conditional inside another conditional. Use when a decision depends on an earlier decision, but avoid excessive nesting.

### 8.4 `match` and `case`
**Definition:** Structural pattern matching selects a case based on the shape or value of an object.

**Syntax pattern:** `match subject:` followed by one or more `case pattern:` clauses.

**Version note:** `match`/`case` was introduced in Python 3.10.

### 8.5 Conditional expressions
**Definition:** An expression that chooses between two values based on a condition.

### 8.6 Combining conditions
Study `and`, `or`, `not`, comparison chaining, short-circuit evaluation, and nested conditions.

---

## 9. Loops and Iteration 🔁

### 9.1 `while` loop
**Definition:** Repeats a block while a condition remains true.

**Syntax pattern:** `while condition: ...`

### 9.2 `for` loop
**Definition:** Iterates over the items supplied by an iterable.

**Syntax pattern:** `for item in iterable: ...`

### 9.3 `range()`
**Definition:** Produces an immutable range of integers, often used for counting or repeated iteration.

**Syntax pattern:** `range(stop)` or `range(start, stop, step)`

### 9.4 Loop control
- `break` — exits the nearest enclosing loop.
- `continue` — skips to the next iteration of the nearest enclosing loop.
- `pass` — performs no action; acts as a placeholder.
- Loop `else` — runs if the loop finishes without being terminated by `break`.

### 9.5 Nested loops
**Definition:** A loop inside another loop. Understand iteration counts and the effect of `break` and `continue` on the nearest loop.

### 9.6 Iteration tools
- `enumerate()` — pairs items with a counter.
- `zip()` — iterates over corresponding items from multiple iterables.
- `reversed()` — provides reverse iteration where supported.
- Iterable versus iterator
- `iter()` and `next()`
- Exhaustion and `StopIteration`

---

## 10. Functions 🧩

### 10.1 What is a function?
**Definition:** A reusable unit of code that may accept inputs, perform operations, and return a result.

### 10.2 Defining and calling functions
**Syntax pattern:** `def function_name(parameters): ...`

Study function definition, function call, indentation, docstrings, and function scope.

### 10.3 Parameters versus arguments
- **Parameter:** A name in a function definition.
- **Argument:** A value or object supplied when calling the function.

### 10.4 Argument-passing patterns
- Positional arguments
- Keyword arguments
- Default parameter values
- Positional-only parameters
- Keyword-only parameters
- Variable positional arguments: `*args`
- Variable keyword arguments: `**kwargs`
- Argument unpacking with `*` and `**`

### 10.5 Return values
- `return` sends a value back to the caller and ends that function call.
- A function without an explicit return value returns `None`.
- Distinguish returning a value from displaying output with `print()`.
- Functions may return multiple values, typically represented as a tuple.

### 10.6 Scope and name resolution
- Local scope
- Enclosing function scope
- Global/module scope
- Built-in scope
- `global` and `nonlocal`
- LEGB name-resolution rule

### 10.7 Mutable arguments and object references
**Important correction:** Python uses *call by object sharing* (also described as call by assignment). A function receives a reference to the same object; rebinding a parameter does not rebind the caller’s variable, but mutating a shared mutable object can be visible to the caller. “Call by value versus call by reference” is an imperfect description of Python.

### 10.8 Advanced function patterns
- Nested functions
- Functions as objects
- Passing functions as arguments
- Returning functions
- Higher-order functions
- Lambda expressions
- Closures
- Decorators (introductory concept)
- Recursion and base cases

### 10.9 Built-in functions
Built-in functions are available without importing a module. Learn their purpose, accepted inputs, and return values.

#### Level 1 — Fundamentals
- `print()` — display output
- `input()` — read text input
- `type()` — inspect an object’s type
- `len()` — return the length of a supported object
- `int()` — construct an integer
- `float()` — construct a float
- `str()` — construct a string representation
- `bool()` — convert according to truth-value rules
- `range()` — represent a range of integers
- `isinstance()` — check type membership

#### Level 2 — Problem solving
- `sum()` — total numeric items
- `min()` — smallest item or value
- `max()` — largest item or value
- `sorted()` — return a new sorted list
- `abs()` — absolute value or magnitude
- `round()` — round a number
- `all()` — test whether all items are truthy
- `any()` — test whether at least one item is truthy
- `enumerate()` — pair items with indexes/counters
- `zip()` — combine corresponding items from iterables

#### Level 3 — Iteration and object introspection
- `map()` — apply a function to iterable items lazily
- `filter()` — select items using a predicate lazily
- `iter()` — obtain an iterator
- `next()` — retrieve the next iterator item
- `reversed()` — obtain a reverse iterator where supported
- `getattr()` — retrieve a named attribute
- `hasattr()` — test for an attribute
- `callable()` — test whether an object appears callable
- `repr()` — obtain a developer-oriented representation
- `super()` — access parent-class behavior through the method resolution order

#### Additional useful built-ins
- `dir()`, `help()`, `id()`
- `list()`, `tuple()`, `set()`, `dict()`, `frozenset()`
- `complex()`, `bytes()`, `bytearray()`
- `ord()`, `chr()`
- `bin()`, `oct()`, `hex()`
- `divmod()`, `pow()`
- `slice()`, `hash()`
- `open()`
- `staticmethod()`, `classmethod()`, `property()`
- `vars()`, `globals()`, `locals()`
- `breakpoint()`


