# 🐍 Python Complete Revision Notes

---

## 1️⃣ History of Python

Python ko **Guido van Rossum** ne 1989 me banana shuru kiya aur 1991 me Python 0.9.0 release hua tha. Naam "Monty Python's Flying Circus" show se inspired hai, saap se nahi! 🐍

Python 2.0 (2000) aur Python 3.0 (2008) major releases the — Python 3 backward incompatible tha but cleaner aur better tha, isiliye aaj sab Python 3 use karte hain.

**When to use:** Jab tumhe pata karna ho ki language mature hai ya nahi — history dikhati hai Python 30+ saal se evolve ho raha hai, isiliye ecosystem bahut strong hai.

---

## 2️⃣ Runtime Environment (Interpreter)

Python ek **interpreted language** hai — code line-by-line execute hota hai, compile karke ek saath nahi (jaise C/C++ me hota hai).

Sabse common implementation **CPython** hai (C me likha gaya interpreter), aur iske alawa PyPy (fast, JIT-based), Jython (Java pe), IronPython (.NET pe) bhi hote hain.

| Implementation | Language | Speciality |
|---|---|---|
| CPython | C | Default, most used |
| PyPy | Python (RPython) | JIT compiler, fast |
| Jython | Java | JVM par chalta hai |
| IronPython | C# | .NET framework ke liye |

**When to use:** Normal development ke liye CPython (default hi hota hai), performance-critical apps me PyPy try kar sakte ho.

---

## 3️⃣ IDE (Integrated Development Environment)

IDE ek software hai jaha code likhna, run karna, debug karna sab ek jagah ho jata hai — jaise VS Code, PyCharm, Jupyter Notebook.

| IDE | Best For |
|---|---|
| VS Code | Lightweight, extensions-rich, general purpose |
| PyCharm | Professional, large projects, built-in tools |
| Jupyter Notebook | Data science, ML, cell-by-cell execution |
| IDLE | Beginners, comes with Python installation |

**When to use:** Beginner ho to IDLE/VS Code, data science karna hai to Jupyter, bade enterprise projects ke liye PyCharm.

---

## 4️⃣ Data Types

Python me data types **dynamically typed** hote hain — variable ka type declare nahi karna padta, Python khud detect kar leta hai.

| Type | Example | Mutable? |
|---|---|---|
| `int` | `10` | ❌ No |
| `float` | `10.5` | ❌ No |
| `complex` | `2+3j` | ❌ No |
| `str` | `"hello"` | ❌ No |
| `bool` | `True/False` | ❌ No |
| `list` | `[1,2,3]` | ✅ Yes |
| `tuple` | `(1,2,3)` | ❌ No |
| `set` | `{1,2,3}` | ✅ Yes |
| `dict` | `{"a":1}` | ✅ Yes |
| `NoneType` | `None` | ❌ No |

**When to use:** Fixed data jo change nahi hoga (constants) → immutable types. Data jo change hota rahega (list of items) → mutable types.

---

## 5️⃣ Output (`print()`)

`print()` function screen pe output dikhata hai. Multiple values, separators, aur end character control kar sakte ho.

```python
print("Farhan", "BCA", sep=" - ", end="\n")
print(f"Name: {name}, Age: {age}")   # f-string (best & fastest way)
```

| Method | Example | Notes |
|---|---|---|
| f-string | `f"{x}"` | Fastest, most readable (Python 3.6+) |
| `.format()` | `"{}".format(x)` | Older style, still used |
| `%` operator | `"%s" % x` | Legacy C-style |

**When to use:** Hamesha f-strings use karo — clean, fast, aur readable hote hain.

---

## 6️⃣ Variables

Variable ek naam hai jo memory me value store karta hai. Python me `var = value` likhte hi variable create ho jata hai, type declare karne ki zarurat nahi.

```python
x = 10          # int
name = "Farhan" # str
x, y, z = 1, 2, 3   # multiple assignment
```

**Rules:** Letter/underscore se start hona chahiye, case-sensitive hai, keywords use nahi kar sakte.

**When to use:** Har jagah — data store karne, reuse karne, aur readable code likhne ke liye variables essential hain.

---

## 7️⃣ Input (`input()`)

`input()` user se keyboard se data leta hai — hamesha **string** return karta hai, chahe number type karo.

```python
age = int(input("Enter age: "))   # type-casting zaroori hai numbers ke liye
```

**When to use:** Jab program ko user se runtime pe data chahiye ho (forms, calculators, CLI tools).

---

## 8️⃣ Operators

### 🔹 Unary Operator
Sirf ek operand pe kaam karta hai. Example: `-x`, `+x`, `not x`

### 🔹 Binary Operators

**a) Arithmetic Operators**

| Operator | Meaning | Example |
|---|---|---|
| `+` | Addition | `5+2=7` |
| `-` | Subtraction | `5-2=3` |
| `*` | Multiplication | `5*2=10` |
| `/` | Division (float) | `5/2=2.5` |
| `//` | Floor Division | `5//2=2` |
| `%` | Modulus | `5%2=1` |
| `**` | Exponent | `5**2=25` |

**b) Comparison (Relational) Operators**

| Operator | Meaning |
|---|---|
| `==` | Equal to |
| `!=` | Not equal to |
| `>` `<` | Greater/Less than |
| `>=` `<=` | Greater/Less than equal to |

**c) Logical Operators**

| Operator | Meaning | Example |
|---|---|---|
| `and` | Dono True ho to True | `True and False = False` |
| `or` | Ek bhi True ho to True | `True or False = True` |
| `not` | Reverse karta hai | `not True = False` |

**d) Bitwise Operators**

| Operator | Meaning | Example |
|---|---|---|
| `&` | AND | `5 & 3 = 1` |
| `\|` | OR | `5 \| 3 = 7` |
| `^` | XOR | `5 ^ 3 = 6` |
| `~` | NOT | `~5 = -6` |
| `<<` | Left Shift | `5 << 1 = 10` |
| `>>` | Right Shift | `5 >> 1 = 2` |

### 🔹 Ternary Operator (Conditional Expression)
One-line if-else. Example: `result = "Pass" if marks>=40 else "Fail"`

### 🔹 Membership Operators
`in` aur `not in` — check karte hain ki element kisi sequence (list/string/tuple) me hai ya nahi.

```python
"a" in "apple"   # True
5 not in [1,2,3] # True
```

### 🔹 Identity Operators
`is` aur `is not` — check karte hain ki do variables same memory location point kar rahe hain ya nahi (value nahi, identity compare karta hai).

### 🔹 Assignment Operators
`=`, `+=`, `-=`, `*=`, `/=`, `//=`, `%=`, `**=` — value assign aur update karne ke liye.

**When to use:** Arithmetic → calculations, Comparison → conditions, Logical → multiple conditions combine karna, Bitwise → low-level/flags/performance work, Ternary → short conditional assignment, Membership → searching, Identity → object comparison (especially `None` check karte time `is None` use karo).

---

## 9️⃣ Strings & String Methods

String characters ka immutable sequence hai, single/double/triple quotes me likhte hain.

```python
s = "Hello Farhan"
```

| Method | Use | Example |
|---|---|---|
| `.lower()` / `.upper()` | Case change | `"Hi".lower() → "hi"` |
| `.strip()` | Extra spaces hatana | `" hi ".strip() → "hi"` |
| `.split()` | String ko list me todna | `"a,b".split(",") → ['a','b']` |
| `.join()` | List ko string banana | `",".join(['a','b']) → "a,b"` |
| `.replace()` | Replace text | `"hi".replace("h","H")` |
| `.find()` | Index dhundo | `"hi".find("i") → 1` |
| `.format()` | Formatting | `"{}".format(x)` |
| `.count()` | Occurrence count | `"aa".count("a") → 2` |
| `len()` | Length | `len("hi") → 2` |
| Slicing | Substring nikalna | `s[0:3]` |

**When to use:** Text processing, user input cleaning, data parsing, report generation — string methods almost har project me use hote hain (jaise tumhare Bole Churiya project me product names format karne me).

---

## 🔟 Control Flow & Loops

Control flow decide karta hai code kaunse order me execute hoga.

```python
if condition:
    ...
elif condition2:
    ...
else:
    ...
```

| Loop | Use Case |
|---|---|
| `for` | Jab iterations ki count known ho (list, range) |
| `while` | Jab condition-based repeat karna ho (count unknown) |
| `break` | Loop turant rok do |
| `continue` | Current iteration skip karke next pe jao |
| `pass` | Kuch mat karo, placeholder |

```python
for i in range(5):
    if i == 3:
        break
```

**When to use:** `for` → known sequence pe kaam (list of products), `while` → jab tak condition true rahe (game loop, retry logic).

---

## 1️⃣1️⃣ Collections — List, Tuple, Set, Dictionary (Detailed)

### 📋 List
Ordered, **mutable**, duplicate allow karta hai. `[]` se banate hain.

**Common Methods:** `.append()`, `.insert()`, `.remove()`, `.pop()`, `.sort()`, `.reverse()`, `.extend()`, `.index()`, `.count()`, `.clear()`

```python
fruits = ["apple", "banana"]
fruits.append("mango")   # ['apple','banana','mango']
```

**When to use:** Jab order matter kare aur data change hota rahe (e.g., shopping cart items, to-do list).

---

### 📦 Tuple
Ordered, **immutable**, duplicate allow karta hai. `()` se banate hain.

**Common Methods:** `.count()`, `.index()` (sirf ye do, kyunki immutable hai)

```python
point = (10, 20)
```

**When to use:** Jab data change nahi hona chahiye — fixed records (coordinates, database rows, function returns with multiple values). Tuples list se **fast** hote hain.

---

### 🎯 Set
Unordered, **mutable**, duplicate **allow nahi karta**. `{}` se banate hain (empty set ke liye `set()` use karo).

**Common Methods:** `.add()`, `.remove()`, `.discard()`, `.union()`, `.intersection()`, `.difference()`, `.issubset()`

```python
s = {1, 2, 2, 3}   # {1, 2, 3}
```

**When to use:** Duplicates hatane ke liye, membership check fast karne ke liye (`in` operator O(1) hota hai), mathematical set operations (union/intersection) ke liye.

---

### 🗂️ Dictionary
Key-value pairs, **mutable**, keys unique hote hain (Python 3.7+ me insertion-ordered). `{}` se banate hain.

**Common Methods:** `.keys()`, `.values()`, `.items()`, `.get()`, `.update()`, `.pop()`, `.setdefault()`

```python
student = {"name": "Farhan", "course": "BCA"}
student.get("name")   # "Farhan"
```

**When to use:** Jab key ke through value fetch karni ho — real world objects represent karne ke liye best (jaise ek product ka JSON: `{"name":"Bangle", "price":499}`).

---

### 🔍 Difference Table (List vs Tuple vs Set vs Dict)

| Feature | List | Tuple | Set | Dictionary |
|---|---|---|---|---|
| Ordered | ✅ Yes | ✅ Yes | ❌ No | ✅ Yes (3.7+) |
| Mutable | ✅ Yes | ❌ No | ✅ Yes | ✅ Yes |
| Duplicates | ✅ Allowed | ✅ Allowed | ❌ Not Allowed | Keys unique, values duplicate ho sakti hain |
| Syntax | `[]` | `()` | `{}` | `{key: value}` |
| Indexing | ✅ Yes | ✅ Yes | ❌ No | ❌ No (key se access) |
| Speed | Medium | Fast | Fast lookup | Fast lookup |

### ✂️ Slicing
List, tuple, string sab pe kaam karta hai: `sequence[start:stop:step]`

```python
lst = [0,1,2,3,4,5]
lst[1:4]     # [1,2,3]
lst[::-1]    # reverse: [5,4,3,2,1,0]
lst[::2]     # [0,2,4]
```

**When to use:** Jab data ka part chahiye ho — pagination, reversing, skipping elements.

---

## 1️⃣2️⃣ Functions (Complete)

Function reusable block of code hai jo specific task perform karta hai.

```python
def greet(name):
    return f"Hello {name}"
```

| Concept | Meaning | Example |
|---|---|---|
| Parameters vs Arguments | Parameter = function definition me, Argument = call karte time value | `def f(x):` → x is parameter |
| Default Arguments | Default value set karna | `def f(x=5):` |
| `*args` | Multiple positional arguments (tuple banata hai) | `def f(*args):` |
| `**kwargs` | Multiple keyword arguments (dict banata hai) | `def f(**kwargs):` |
| Return | Value wapas bhejta hai | `return x` |
| Lambda | Anonymous one-line function | `lambda x: x*2` |
| Recursion | Function khud ko call kare | Factorial, Fibonacci |

```python
def demo(*args, **kwargs):
    print(args)     # tuple: (1,2,3)
    print(kwargs)   # dict: {'name':'Farhan'}

demo(1, 2, 3, name="Farhan")
```

### 🔒 Closures
Closure ek function hai jo apne outer function ke variables ko "yaad" rakhta hai, even after outer function execute ho chuka ho.

```python
def outer(msg):
    def inner():
        print(msg)   # inner() outer ka 'msg' yaad rakhta hai
    return inner

greet = outer("Hi Farhan")
greet()   # "Hi Farhan"
```

**When to use:** `*args/**kwargs` → jab pata na ho kitne arguments aayenge (flexible APIs), Closures → decorators banane ke liye, state maintain karne ke liye without classes, Lambda → short throwaway functions (sorting keys, map/filter).

---

## 1️⃣3️⃣ Scope (Variable Scope)

Scope decide karta hai variable kaha accessible hai. Python **LEGB Rule** follow karta hai.

| Scope | Meaning |
|---|---|
| **L**ocal | Function ke andar defined variable |
| **E**nclosing | Outer function ka variable (nested functions) |
| **G**lobal | File-level variable |
| **B**uilt-in | Python ke built-in names (`print`, `len`) |

```python
x = "global"
def func():
    x = "local"   # ye alag hai global x se
    print(x)
```

`global` keyword se global variable ko function ke andar modify kar sakte ho.

**When to use:** Bade projects me variable naming clashes avoid karne ke liye scope samajhna zaroori hai.

---

## 1️⃣4️⃣ Exception Handling

Errors ko gracefully handle karne ke liye `try-except` use karte hain, taaki program crash na ho.

```python
try:
    x = 10/0
except ZeroDivisionError as e:
    print("Error:", e)
else:
    print("No error occurred")
finally:
    print("Always runs")
```

| Block | Purpose |
|---|---|
| `try` | Risky code |
| `except` | Error handle karo |
| `else` | Agar error na aaye to chale |
| `finally` | Hamesha chalega, chahe error ho ya na ho |
| `raise` | Manually exception throw karna |

**When to use:** File operations, API calls, user input, database connections — jahan bhi runtime error ka chance ho wahan exception handling zaroor use karo.

---

## 1️⃣5️⃣ File Handling

Files read/write karne ke liye `open()` function use hota hai.

```python
with open("data.txt", "r") as f:
    content = f.read()
```

| Mode | Meaning |
|---|---|
| `"r"` | Read (default) |
| `"w"` | Write (overwrite) |
| `"a"` | Append |
| `"r+"` | Read + Write |
| `"rb"` / `"wb"` | Binary mode |

| Method | Use |
|---|---|
| `.read()` | Pura file content string me |
| `.readline()` | Ek line |
| `.readlines()` | List of lines |
| `.write()` | Likhna |
| `.close()` | File band karna (with block me auto hota hai) |

**When to use:** Hamesha `with open(...)` use karo — ye automatically file close kar deta hai, even error aane pe bhi. Config files, logs, CSV data read/write karne ke liye zaroori hai.

---

## 1️⃣6️⃣ Map, Filter, Reduce

Functional programming tools jo list/iterable pe operation apply karte hain.

| Function | Purpose | Example |
|---|---|---|
| `map()` | Har element pe function apply karo | `map(lambda x: x*2, [1,2,3]) → [2,4,6]` |
| `filter()` | Condition ke basis pe filter karo | `filter(lambda x: x>2, [1,2,3]) → [3]` |
| `reduce()` | Sabko combine karke ek value banao (functools se import) | `reduce(lambda a,b: a+b, [1,2,3]) → 6` |

```python
nums = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, nums))
evens = list(filter(lambda x: x%2==0, nums))
```

**When to use:** Jab list comprehension se bhi kaam ho jaye, but functional style pasand ho ya existing function ko directly pass karna ho (`map(str, nums)`). Large data pipelines me common hai.

---

## 1️⃣7️⃣ OOPs (Object-Oriented Programming)

Python objects aur classes ke through real-world entities model karta hai.

```python
class Student:
    def __init__(self, name, course):   # constructor
        self.name = name
        self.course = course

    def display(self):
        print(f"{self.name} - {self.course}")

s1 = Student("Farhan", "BCA")
s1.display()
```

| Concept | Meaning |
|---|---|
| **Class** | Blueprint/template |
| **Object** | Class ka instance |
| **`__init__`** | Constructor, object banate hi call hota hai |
| **`self`** | Current object ka reference |
| **Encapsulation** | Data ko class ke andar bind karna (private vars `_var`, `__var`) |
| **Inheritance** | Ek class dusri class ke properties le sakti hai |
| **Polymorphism** | Same method name, different behavior |
| **Abstraction** | Implementation details hide karna, sirf essential dikhana |

```python
class Animal:
    def sound(self):
        print("Some sound")

class Dog(Animal):        # Inheritance
    def sound(self):       # Polymorphism (method overriding)
        print("Bark")
```

| Pillar | Real-life Example |
|---|---|
| Encapsulation | ATM machine — internal logic hidden, sirf buttons expose |
| Inheritance | Child class "car" inherits "vehicle" properties |
| Polymorphism | "draw()" method Circle aur Square dono me different kaam kare |
| Abstraction | Car chalane ke liye engine internals janna zaroori nahi |

**When to use:** Jab tumhare project me multiple related entities ho (jaise Bole Churiya me `Product`, `Cart`, `User` classes) — OOP code ko organized, reusable aur scalable banata hai. Chhote scripts ke liye functional approach bhi chalta hai.

---

## 1️⃣8️⃣ Python Architecture

Python code execution ka internal flow samajhna important hai.

```
Source Code (.py) → Compiler → Bytecode (.pyc) → PVM (Python Virtual Machine) → Output
```

| Component | Role |
|---|---|
| **Source Code** | Tumhara `.py` file |
| **Compiler** | Bytecode me convert karta hai (`.pyc`, human-unreadable but platform-independent) |
| **PVM (Python Virtual Machine)** | Bytecode ko actual machine code me interpret karta hai — ye Python interpreter ka core hai |
| **GIL (Global Interpreter Lock)** | Ek time pe sirf ek thread Python bytecode execute kar sakta hai (multi-threading limit) |

**When to use:** Ye samajhna zaroori hai jab performance optimize karni ho, multi-threading vs multi-processing decide karna ho, ya interview me "Python interpreted hai ya compiled?" jaise questions aaye — answer hai: **both** (compile to bytecode, then interpret).

---

## 📌 Quick Revision Summary Table

| Topic | One-Line Takeaway |
|---|---|
| History | Guido van Rossum, 1991, readability-focused |
| Runtime | CPython default interpreter |
| Data Types | Dynamically typed, mutable vs immutable |
| Operators | Arithmetic, Comparison, Logical, Bitwise, Ternary, Membership |
| Strings | Immutable, rich method set |
| Loops | `for` known iterations, `while` condition-based |
| List | Mutable, ordered, flexible |
| Tuple | Immutable, fast, fixed data |
| Set | Unique elements, fast lookup |
| Dict | Key-value, fastest access by key |
| Functions | `*args`/`**kwargs` for flexibility, closures for state |
| Scope | LEGB rule |
| Exceptions | `try-except-finally` for safety |
| File Handling | `with open()` best practice |
| Map/Filter | Functional one-liners on iterables |
| OOP | 4 pillars — Encapsulation, Inheritance, Polymorphism, Abstraction |
| Architecture | Source → Bytecode → PVM |

---

*Bhai, ye notes revision ke liye hain — exam se pehle isko ek baar fatafat scan kar lena, sab yaad aa jayega! 💪*
