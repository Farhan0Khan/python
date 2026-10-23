from pathlib import Path

content = r'''# Python Fundamentals and Core Syntax — Revision Notes

> **Purpose:** A structured, corrected Python syllabus for revision. This file focuses on definitions, syntax, and method names—not worked code examples.

## Table of Contents

1. [Python Fundamentals](#1-python-fundamentals)
2. [Data Types and Object Mutability](#2-data-types-and-object-mutability)
3. [Operators](#3-operators)
4. [Type Conversion and Type Casting](#4-type-conversion-and-type-casting)
5. [Functions](#5-functions)
6. [Conditional Statements](#6-conditional-statements)
7. [Loops and Loop Control](#7-loops-and-loop-control)
8. [Indexing and Slicing](#8-indexing-and-slicing)
9. [Strings](#9-strings)
10. [Lists](#10-lists)
11. [Tuples](#11-tuples)
12. [Sets and Frozensets](#12-sets-and-frozensets)
13. [Dictionaries](#13-dictionaries)
14. [Built-in Functions by Learning Level](#14-built-in-functions-by-learning-level)
15. [Important Corrections and Reminders](#15-important-corrections-and-reminders)

---

## 1. Python Fundamentals

### 1.1 What is Python?
Python is a high-level, general-purpose programming language known for readable syntax and a large standard library and ecosystem.

### 1.2 Features of Python
- Readable, relatively concise syntax
- High-level language
- Dynamically typed
- Supports multiple programming paradigms, including procedural, object-oriented, and functional styles
- Cross-platform
- Large standard library and third-party package ecosystem
- Interpreted execution model in common implementations
- Automatic memory management

### 1.3 Demand and Uses of Python
Python is widely used in:
- Web development and APIs
- Automation and scripting
- Data analysis and visualization
- Artificial intelligence and machine learning
- Scientific computing
- Testing and developer tooling
- Cybersecurity and network tools
- Education and prototyping

> **Career note:** Demand varies by role, location, and industry. Python alone is rarely enough for a job; pair it with domain skills, projects, debugging, Git, databases, and software-development fundamentals.

### 1.4 History and Future of Python
- Created by Guido van Rossum; development began in the late 1980s.
- First publicly released in 1991.
- Python 3 was introduced in 2008.
- Python continues to evolve through Python Enhancement Proposals (PEPs) and new releases.
- Future areas of use include AI, data engineering, automation, scientific computing, and backend services. Future demand cannot be guaranteed.

### 1.5 Advantages
- Easy to read and learn
- Broad ecosystem and community
- Fast development and prototyping
- Works across major operating systems
- Integrates with other languages and systems

### 1.6 Disadvantages
- Often slower than compiled languages for CPU-heavy tasks
- Can use more memory than lower-level alternatives
- Dynamic typing means some errors appear at runtime
- Mobile and browser-native application development are less central to its ecosystem than some alternatives
- Package and environment management can require care

---

## 2. Data Types and Object Mutability

Python is **dynamically typed**: a name can refer to objects of different types during execution. Python variables are names bound to objects; they are not classified simply as “stack variables” or “heap variables” in the way the original notes suggest.

### 2.1 Core Built-in Types

| Category | Types | Mutable? |
|---|---|---|
| Numeric | `int`, `float`, `complex` | No |
| Boolean | `bool` | No |
| Null-like value | `NoneType` (`None`) | No |
| Text sequence | `str` | No |
| Sequence collections | `list`, `tuple`, `range` | `list` is mutable; `tuple` and `range` are immutable |
| Set collections | `set`, `frozenset` | `set` is mutable; `frozenset` is immutable |
| Mapping | `dict` | Mutable |
| Binary sequences | `bytes`, `bytearray`, `memoryview` | Depends on type |
| Callable objects | Functions and methods | Function objects are not ordinary mutable collections |

### 2.2 Numbers
- `int`: integers of arbitrary precision (limited by available memory).
- `float`: floating-point numbers; many decimal fractions are approximations in binary.
- `complex`: numbers with real and imaginary parts.

### 2.3 Boolean
- `bool` has two values: `True` and `False`.
- Booleans are a subtype of integers in Python, but they should normally be used for logical truth values.

### 2.4 None
- `None` represents the absence of a value or a missing result.
- Its type is `NoneType`.
- Check it with identity comparison: `value is None`.

### 2.5 String
- `str` represents Unicode text.
- Strings are immutable sequences of characters.

### 2.6 Collection Types
- `list`: ordered, mutable sequence; permits duplicates.
- `tuple`: ordered, immutable sequence; permits duplicates.
- `set`: mutable collection of unique, hashable elements; no positional indexing.
- `frozenset`: immutable set.
- `dict`: mutable mapping of unique, hashable keys to values; preserves insertion order in modern Python.

### 2.7 Mutable vs Immutable
- **Mutable:** an object can be changed after it is created, such as a list, set, or dictionary.
- **Immutable:** an object cannot be changed in place, such as an integer, float, string, or tuple.
- A tuple is immutable, but it can contain a mutable object; that inner object may still change.
- Assignment creates or changes a name binding. It does not automatically copy an object.

---

## 3. Operators

### 3.1 Arithmetic Operators

| Operator | Meaning |
|---|---|
| `+` | Addition |
| `-` | Subtraction |
| `*` | Multiplication |
| `/` | True division |
| `//` | Floor division |
| `%` | Remainder (modulo) |
| `**` | Exponentiation |

### 3.2 Comparison Operators
- `<` — less than
- `>` — greater than
- `<=` — less than or equal to
- `>=` — greater than or equal to
- `==` — equal values
- `!=` — not equal values

Comparison expressions generally evaluate to a Boolean value. Some comparisons between incompatible types raise `TypeError`.

### 3.3 Assignment Operators
- `=`, `+=`, `-=`, `*=`, `/=`, `//=`, `%=`, `**=`
- Bitwise assignment forms include `&=`, `|=`, `^=`, `<<=`, and `>>=`.
- Assignment is a statement, not an equality comparison.

### 3.4 Bitwise Operators
- `&` — bitwise AND
- `|` — bitwise OR
- `^` — bitwise XOR
- `~` — bitwise NOT
- `<<` — left shift
- `>>` — right shift

Bitwise operators work on integer bit patterns. Do not confuse `^` (XOR) with exponentiation (`**`).

### 3.5 Logical Operators
- `and`
- `or`
- `not`

`and` and `or` short-circuit and can return one of their operands, not necessarily a Boolean object.

### 3.6 Identity Operators
- `is`
- `is not`

These test whether two references point to the **same object**. Use `==` to compare values in most cases; use `is` for singleton checks such as `None`.

### 3.7 Membership Operators
- `in`
- `not in`

These test membership in a sequence or collection. For a dictionary, membership checks keys.

### 3.8 Operator Precedence
Operator precedence determines how expressions are grouped. Use parentheses `()` when they make an expression clearer or remove ambiguity.

---

## 4. Type Conversion and Type Casting

### 4.1 Implicit Type Conversion
Python may automatically convert compatible numeric values during an operation, such as promoting an integer to a floating-point value.

### 4.2 Explicit Type Casting / Conversion
Common constructors:
- `int()`
- `float()`
- `complex()`
- `str()`
- `bool()`
- `list()`
- `tuple()`
- `set()`
- `frozenset()`
- `dict()`
- `bytes()`
- `bytearray()`

**Important:** Conversion is not always possible. Invalid input may raise `ValueError` or `TypeError`; converting a float to an integer truncates the fractional part toward zero rather than rounding.

---

## 5. Functions

### 5.1 Calling and Defining Functions
- Define a function with `def`.
- Call a function by writing its name followed by parentheses.
- `return` sends a result back to the caller and ends that function call.
- If a function reaches its end without a `return` value, it returns `None`.

### 5.2 Parameters vs Arguments
- **Parameter:** a name in a function definition.
- **Argument:** a value or object supplied when calling the function.

### 5.3 Common Parameter Kinds
- Positional parameters
- Keyword arguments
- Default parameters
- Variable positional parameters: `*args`
- Variable keyword parameters: `**kwargs`
- Positional-only parameters (before `/`)
- Keyword-only parameters (after `*`)

Avoid using a mutable object as a default parameter value unless shared state is intentional.

### 5.4 Python Argument Passing
Python uses **object sharing** (also described as call by object reference or call by assignment). A function receives references to objects:
- Rebinding a parameter does not rebind the caller’s variable.
- Mutating a shared mutable object can be visible to the caller.
- This is not accurately described as purely “call by value” or “call by reference” in the traditional sense.

### 5.5 Other Function Concepts
- Nested functions: functions defined inside other functions
- Higher-order functions: functions that accept or return other functions
- Passing a function as an argument
- Lambda expressions: small anonymous functions
- Recursion: a function calling itself
- Scope: local, enclosing, global, and built-in
- Docstrings: documentation strings for modules, classes, and functions
- Type hints: optional annotations describing expected types

### 5.6 `pass`
`pass` is a no-operation statement used where Python syntax requires a statement but no action is needed yet.

### 5.7 `return` vs a Function That Performs Work
- A function may **return** a value for its caller to use.
- A function may perform an action (a side effect), such as printing or modifying an object.
- A function can do both.

---

## 6. Conditional Statements

### 6.1 `if`, `elif`, and `else`
Use conditional statements to select which block executes based on a condition.

### 6.2 Truthiness
Falsy values include `False`, `None`, numeric zero, and empty collections or strings. Most other objects are truthy.

### 6.3 Logical Conditions
- `and`: both conditions must be truthy
- `or`: at least one condition must be truthy
- `not`: negates truthiness

### 6.4 `match` / `case`
Structural pattern matching was introduced in Python 3.10. It compares a value against patterns and can bind matched parts to names.

---

## 7. Loops and Loop Control

### 7.1 `while`
Repeats a block while a condition remains truthy.

### 7.2 `for`
Iterates over items from an iterable, such as a list, string, dictionary, set, or `range`.

### 7.3 Loop Control
- `break`: exits the nearest enclosing loop.
- `continue`: skips the rest of the current iteration and proceeds to the next.
- `pass`: does nothing.
- Loop `else`: runs if the loop finishes without being terminated by `break`.

### 7.4 `range()`
Creates an immutable range sequence, commonly used for integer iteration. It supports a start, stop, and optional step; the stop value is excluded.

---

## 8. Indexing and Slicing

### 8.1 Indexing
Indexing accesses an item by position in a sequence.
- Positive indices count from the beginning, starting at `0`.
- Negative indices count from the end, starting at `-1`.
- Strings, lists, and tuples support indexing.
- Sets do not support positional indexing.
- Dictionaries are accessed by key, not by positional index.

### 8.2 Slicing
Slicing selects part of a sequence using the general form:

`sequence[start:stop:step]`

- `start` is included.
- `stop` is excluded.
- `step` controls the interval and may be negative.
- Omitted values use defaults based on the step direction.
- Slicing strings, lists, and tuples produces a new object of the same general sequence type.

---

## 9. Strings

A string (`str`) is an immutable Unicode sequence of text.

### 9.1 String Operations
- Indexing and slicing
- Concatenation with `+`
- Repetition with `*`
- Membership checks with `in` and `not in`
- Formatting with f-strings, `str.format()`, and format specifications
- Escape sequences such as `\n`, `\t`, `\\`, and `\"`

### 9.2 String Methods

| Method | Purpose |
|---|---|
| `capitalize()` | Capitalizes the first character and lowercases the rest |
| `casefold()` | Produces a form suited to caseless comparisons |
| `center()` | Centers text within a specified width |
| `count()` | Counts non-overlapping occurrences |
| `encode()` | Encodes text to bytes |
| `endswith()` | Tests the ending of a string |
| `expandtabs()` | Replaces tab characters using tab stops |
| `find()` | Finds a substring; returns `-1` if absent |
| `format()` | Formats values into a string |
| `format_map()` | Formats using a mapping |
| `index()` | Finds a substring; raises `ValueError` if absent |
| `isalnum()` | Tests whether all characters are alphanumeric and the string is non-empty |
| `isalpha()` | Tests whether all characters are alphabetic and the string is non-empty |
| `isascii()` | Tests whether all characters are ASCII; empty strings return `True` |
| `isdecimal()` | Tests whether all characters are decimal characters and the string is non-empty |
| `isdigit()` | Tests whether all characters are digit characters and the string is non-empty |
| `isidentifier()` | Tests whether text is a valid identifier |
| `islower()` | Tests whether cased characters are lowercase |
| `isnumeric()` | Tests whether all characters are numeric and the string is non-empty |
| `isprintable()` | Tests whether all characters are printable; empty strings return `True` |
| `isspace()` | Tests whether all characters are whitespace and the string is non-empty |
| `istitle()` | Tests title-case formatting |
| `isupper()` | Tests whether cased characters are uppercase |
| `join()` | Joins an iterable of strings using this string as separator |
| `ljust()` | Left-aligns text within a width |
| `lower()` | Converts cased characters to lowercase |
| `lstrip()` | Removes leading whitespace or specified characters |
| `maketrans()` | Creates a translation table for `translate()` |
| `partition()` | Splits into a three-part tuple at the first separator |
| `removeprefix()` | Removes a matching prefix, if present |
| `removesuffix()` | Removes a matching suffix, if present |
| `replace()` | Replaces occurrences of a substring |
| `rfind()` | Finds the last occurrence; returns `-1` if absent |
| `rindex()` | Finds the last occurrence; raises `ValueError` if absent |
| `rjust()` | Right-aligns text within a width |
| `rpartition()` | Splits into a three-part tuple at the last separator |
| `rsplit()` | Splits from the right |
| `rstrip()` | Removes trailing whitespace or specified characters |
| `split()` | Splits text into a list |
| `splitlines()` | Splits at line boundaries |
| `startswith()` | Tests the beginning of a string |
| `strip()` | Removes leading and trailing whitespace or specified characters |
| `swapcase()` | Swaps uppercase and lowercase forms |
| `title()` | Converts text to title case |
| `translate()` | Translates characters using a translation table |
| `upper()` | Converts cased characters to uppercase |
| `zfill()` | Pads the left side with zeroes |

> **Reminder:** Strings are immutable. String methods return a result rather than changing the original string in place.

---

## 10. Lists

A list is an ordered, mutable sequence that allows duplicate elements and can contain objects of different types.

### 10.1 List Operations
- Indexing and slicing
- Concatenation and repetition
- Membership tests
- Iteration
- Nested lists
- List comprehensions
- Copying: assignment creates an alias; `copy()` creates a shallow copy

### 10.2 List Methods

| Method | Purpose |
|---|---|
| `append()` | Adds one item to the end |
| `clear()` | Removes all items |
| `copy()` | Returns a shallow copy |
| `count()` | Counts equal items |
| `extend()` | Adds items from an iterable |
| `index()` | Returns the index of the first matching item |
| `insert()` | Inserts an item at a position |
| `pop()` | Removes and returns an item, defaulting to the last |
| `remove()` | Removes the first matching item |
| `reverse()` | Reverses the list in place |
| `sort()` | Sorts the list in place |

> **Reminder:** In-place methods such as `append()`, `extend()`, `sort()`, and `reverse()` generally return `None`.

---

## 11. Tuples

A tuple is an ordered, immutable sequence that allows duplicate elements.

### 11.1 Tuple Concepts
- Indexing and slicing
- Packing and unpacking
- A one-item tuple requires a trailing comma
- A tuple cannot have its item references replaced, but it may contain mutable objects

### 11.2 Tuple Methods
| Method | Purpose |
|---|---|
| `count()` | Counts equal items |
| `index()` | Returns the index of the first matching item |

Tuples have only these two public data-specific methods.

---

## 12. Sets and Frozensets

A set stores unique, hashable elements. A regular `set` is mutable and does not support indexing. A `frozenset` is immutable.

### 12.1 Set Operations
- Union: elements in either set
- Intersection: elements shared by both sets
- Difference: elements in the first set but not the second
- Symmetric difference: elements in either set but not both
- Subset and superset tests
- Disjointness tests

### 12.2 Set Methods

| Method | Purpose |
|---|---|
| `add()` | Adds one element |
| `clear()` | Removes all elements |
| `copy()` | Returns a shallow copy |
| `difference()` | Returns elements not in the other set(s) |
| `difference_update()` | Removes elements found in the other set(s) |
| `discard()` | Removes an element if present; no error if absent |
| `intersection()` | Returns common elements |
| `intersection_update()` | Keeps only common elements |
| `isdisjoint()` | Tests whether there are no common elements |
| `issubset()` | Tests whether all elements are contained in another set |
| `issuperset()` | Tests whether all elements of another set are contained here |
| `pop()` | Removes and returns an arbitrary element |
| `remove()` | Removes an element; raises `KeyError` if absent |
| `symmetric_difference()` | Returns elements in either set but not both |
| `symmetric_difference_update()` | Replaces the set with the symmetric difference |
| `union()` | Returns all unique elements from the sets |
| `update()` | Adds elements from one or more iterables |

### 12.3 Frozenset
`frozenset` supports the non-mutating set operations, including `copy()`, `difference()`, `intersection()`, `isdisjoint()`, `issubset()`, `issuperset()`, `symmetric_difference()`, and `union()`. It does not have mutation methods such as `add()`, `clear()`, `discard()`, `pop()`, `remove()`, or update-in-place methods.

---

## 13. Dictionaries

A dictionary (`dict`) is a mutable mapping of unique, hashable keys to values. Insertion order is guaranteed in modern Python (Python 3.7+).

### 13.1 Dictionary Concepts
- Access values using keys
- Keys must be hashable; values may be of any type
- Keys are unique
- Membership tests check keys
- Dictionaries can be nested
- `keys()`, `values()`, and `items()` return dynamic view objects

### 13.2 Dictionary Methods

| Method | Purpose |
|---|---|
| `clear()` | Removes all items |
| `copy()` | Returns a shallow copy |
| `fromkeys()` | Creates a dictionary from keys with a shared initial value |
| `get()` | Returns a value or a default if the key is missing |
| `items()` | Returns a view of key-value pairs |
| `keys()` | Returns a view of keys |
| `pop()` | Removes a key and returns its value |
| `popitem()` | Removes and returns the most recently inserted key-value pair |
| `setdefault()` | Returns the value for a key; inserts the default if missing |
| `update()` | Adds or updates entries |
| `values()` | Returns a view of values |

> **Caution:** `dict.fromkeys(keys, mutable_value)` uses the same value object for every key. If that value is mutable, the entries share it.

---

## 14. Built-in Functions by Learning Level

This is a suggested learning order, not an official Python classification. Python has many more built-ins than the list below.

### Level 1 — Fundamentals
1. `print()`
2. `input()`
3. `type()`
4. `len()`
5. `int()`
6. `float()`
7. `str()`
8. `bool()`
9. `range()`
10. `isinstance()`

### Level 2 — Problem Solving
1. `sum()`
2. `min()`
3. `max()`
4. `sorted()`
5. `abs()`
6. `round()`
7. `all()`
8. `any()`
9. `enumerate()`
10. `zip()`

### Level 3 — Intermediate Python
1. `map()`
2. `filter()`
3. `iter()`
4. `next()`
5. `reversed()`
6. `getattr()`
7. `hasattr()`
8. `callable()`
9. `repr()`
10. `super()`

### More Useful Built-ins to Learn Later
- Numeric and conversion: `complex()`, `divmod()`, `pow()`
- Collections: `dict()`, `list()`, `tuple()`, `set()`, `frozenset()`
- Iteration: `aiter()`, `anext()`, `iter()`, `next()`
- Object inspection: `dir()`, `id()`, `vars()`, `help()`
- Attributes and types: `delattr()`, `setattr()`, `issubclass()`
- Input/output and files: `open()`
- Functional tools: `staticmethod()`, `classmethod()`, `property()`
- Other important built-ins: `hash()`, `hex()`, `oct()`, `ord()`, `chr()`, `bin()`, `format()`, `memoryview()`, `object()`, `slice()`, `bytes()`, `bytearray()`, `eval()`, `exec()`, `compile()`, `globals()`, `locals()`

> Some built-ins, such as `eval()` and `exec()`, should be studied carefully because executing untrusted text can be unsafe.

---

## 15. Important Corrections and Reminders

- Python does **not** classify its built-in types into a simple “primitive/static/stack/immutable” group versus a “reference/dynamic/heap/mutable” group. Python is dynamically typed, and all values are objects.
- `tuple` is immutable; it is not a mutable/reference type in the same sense as `list`, `dict`, and `set`.
- Functions are callable objects, not a standard collection data type parallel to lists and dictionaries.
- `is` checks object identity; `==` checks value equality.
- Python's argument model is best described as **object sharing**; “call by value vs call by reference” is an oversimplification.
- `range()` is a type/constructor as well as a commonly used iteration tool; it is not an operator.
- `and`, `or`, and `not` are logical operators, not comparison operators.
- `^` is bitwise XOR; `**` is exponentiation.
- The string `is...` methods often return `False` for an empty string, but `isascii()` and `isprintable()` return `True` for an empty string.
- Most list, set, and dictionary methods that mutate the object return `None`.
- Use official Python documentation as the final reference when you need exact behavior for a particular Python version.

---

## Quick Revision Checklist

- [ ] Explain what Python is and where it is used.
- [ ] Identify built-in types and explain mutability.
- [ ] Distinguish value equality (`==`) from identity (`is`).
- [ ] Recognize arithmetic, comparison, assignment, bitwise, logical, identity, and membership operators.
- [ ] Explain implicit conversion and explicit casting.
- [ ] Define functions and distinguish parameters from arguments.
- [ ] Understand `return`, `pass`, default parameters, `*args`, and `**kwargs`.
- [ ] Use conditionals, loops, and loop-control statements.
- [ ] Understand indexing and slicing.
- [ ] Recall string, list, tuple, set, and dictionary methods.
- [ ] Know common built-in functions and their purposes.
'''

path = Path("/mnt/data/python.md")
path.write_text(content, encoding="utf-8")
print(f"Created {path} ({len(content.splitlines())} lines, {path.stat().st_size} bytes)")
