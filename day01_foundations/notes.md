# Day 1 — Python Foundations

> **Focus:** Python execution, variables, objects, core data types, mutability, input, conversion, f-strings, and traceback reading.

## Learning Outcomes

By the end of Day 1, I can:

- Explain that a Python variable is a name bound to an object.
- Identify common Python data types with `type()`.
- Explain the difference between mutable and immutable objects.
- Explain assignment, value equality, and object identity.
- Use `.copy()` to create a separate list object.
- Accept user input and convert it using `int()` or `float()`.
- Format readable output using f-strings.
- Read a Python traceback from the bottom upward.
- Build a small DevOps-focused Deployment Profile program.

## 1. How Python Executes a Script

Python normally executes a script from top to bottom. A name must be defined before it is used.

```python
service_name = "buddybot"
print(service_name)
```

Python first binds `service_name` to the string object `"buddybot"`, then passes that value to `print()`.

## 2. Variables and Objects

A variable is a **name that refers to an object**.

```python
replicas = 3
```

- `replicas` is the variable name.
- `3` is an integer object.
- `=` binds the name to the object.

The assignment operator does not mean “is equal to” in the mathematical sense. It means “bind the name on the left to the value produced on the right.”

### Python Object vs Kubernetes Object

The word **object** is used in both technologies, but the context is different:

| Python object | Kubernetes object |
|---|---|
| A runtime value with a type, identity, and value | An API resource describing desired cluster state |
| Examples: `3`, `"buddybot"`, a list, a function | Examples: Pod, Deployment, Service, Namespace |
| Exists in the Python process memory | Stored and managed through the Kubernetes API server |

## 3. Core Data Types

| Type | Example | Meaning |
|---|---|---|
| `str` | `"buddybot"` | Text |
| `int` | `3` | Whole number |
| `float` | `0.5` | Decimal number |
| `bool` | `True` | Boolean value: `True` or `False` |
| `NoneType` | `None` | No value / value not available |
| `list` | `["pod-1", "pod-2"]` | Ordered, mutable collection |

Use `type()` to inspect an object's type:

```python
service_name = "buddybot"
cpu_limit = 0.5
is_healthy = True
last_error = None

print(type(service_name))  # <class 'str'>
print(type(cpu_limit))     # <class 'float'>
print(type(is_healthy))    # <class 'bool'>
print(type(last_error))    # <class 'NoneType'>
```

Python is dynamically typed: the runtime value determines the type currently associated with a name.

## 4. Immutable Objects

An immutable object cannot be changed after it is created. Integers, floats, strings, booleans, and `None` are immutable.

```python
replicas = 3
desired_replicas = replicas

replicas = replicas + 2

print(replicas)          # 5
print(desired_replicas)  # 3
```

Initially, both names refer to the integer `3`. The expression `replicas + 2` creates the new integer `5`, and only `replicas` is rebound to it. `desired_replicas` continues referring to `3`.

## 5. Mutable Objects

A mutable object can be changed after it is created. Lists are mutable.

```python
running_pods = ["buddybot-1", "buddybot-2"]
backup_pods = running_pods

running_pods.append("buddybot-3")

print(running_pods)
print(backup_pods)
```

Output:

```text
['buddybot-1', 'buddybot-2', 'buddybot-3']
['buddybot-1', 'buddybot-2', 'buddybot-3']
```

`backup_pods = running_pods` does not create another list. Both names refer to the same list, so a mutation is visible through both names.

## 6. Assignment vs Copy

### Same list object

```python
backup_pods = running_pods
```

This creates another reference to the same list.

### Separate list object

```python
backup_pods = running_pods.copy()
```

This creates a new list containing the same current values.

```python
running_pods = ["buddybot-1", "buddybot-2"]
backup_pods = running_pods.copy()

running_pods.append("buddybot-3")

print(running_pods)                 # Three items
print(backup_pods)                  # Two items
print(running_pods is backup_pods)  # False
```

`.copy()` creates a shallow copy. For Day 1, the important point is that it creates a separate outer list. Nested collections will be covered later.

## 7. `=`, `==`, and `is`

| Operator | Purpose | Example |
|---|---|---|
| `=` | Assignment/binding | `service = "buddybot"` |
| `==` | Value equality | `first == second` |
| `is` | Object identity | `first is second` |

```python
original = ["pod-1", "pod-2"]
same_reference = original
separate_copy = original.copy()

print(original == same_reference)  # True: equal values
print(original is same_reference)  # True: same object
print(original == separate_copy)   # True: equal values
print(original is separate_copy)   # False: different objects
```

Key rule:

> `==` compares values. `is` compares identity.

Use `is` commonly for singleton checks such as:

```python
if last_error is None:
    print("No error recorded")
```

Do not use `is` as a replacement for normal string or number comparison.

## 8. User Input and Type Conversion

`input()` always returns a string, even when the user types digits.

```python
replicas = input("Enter replicas: ")
print(type(replicas))  # <class 'str'>
```

Convert the returned string when a numeric value is required:

```python
replicas = int(input("Enter replicas: "))
cpu_per_replica = float(input("Enter CPU per replica: "))
```

Evaluation happens from the inside outward:

```text
input() → "3" → int("3") → 3
```

### Common Conversion Error

```python
cpu = int("0.5")
```

This raises `ValueError` because `"0.5"` is not a valid integer representation.

Correct conversion:

```python
cpu = float("0.5")
```

## 9. F-Strings

An f-string inserts expressions into readable text using `{}`.

```python
service_name = "buddybot"
replicas = 3

print(f"Service: {service_name}")
print(f"Current replicas: {replicas}")
```

The `f` before the opening quote is required.

## 10. Reading a Traceback

Example failure:

```python
desired_replicas = 5
current_replicas = "3"
replicas_to_add = desired_replicas - current_replicas
```

Python raises:

```text
TypeError: unsupported operand type(s) for -: 'int' and 'str'
```

Read a traceback from the bottom upward:

1. Read the final line for the exception type and reason.
2. Find the file and line number.
3. Inspect the failing expression.
4. Check the runtime types and values involved.
5. Fix the cause, then rerun the program.

The fix is to convert the input before calculation:

```python
current_replicas = int(input("Enter current replicas: "))
```

## 11. Day 1 Mini-Project — Deployment Profile

The program accepts deployment details and calculates scaling and CPU requirements.

```python
engineer_name = input("Enter engineer name: ")
service_name = input("Enter service name: ")
environment_name = input("Enter environment name: ")
current_replicas = int(input("Enter current replicas: "))
desired_replicas = int(input("Enter desired replicas: "))
cpu_per_replica = float(input("Enter CPU per replica: "))

replicas_to_add = desired_replicas - current_replicas
total_required_cpu = desired_replicas * cpu_per_replica

print("\n=== Deployment Profile ===")
print(f"Engineer: {engineer_name}")
print(f"Service: {service_name}")
print(f"Environment: {environment_name}")
print(f"Current replicas: {current_replicas}")
print(f"Desired replicas: {desired_replicas}")
print(f"Replicas to add: {replicas_to_add}")
print(f"CPU per replica: {cpu_per_replica} cores")
print(f"Total required CPU: {total_required_cpu} cores")
```

Example output:

```text
=== Deployment Profile ===
Engineer: Vicky
Service: buddybot
Environment: dev
Current replicas: 3
Desired replicas: 5
Replicas to add: 2
CPU per replica: 0.5 cores
Total required CPU: 2.5 cores
```

Scaling down and validating invalid input will be handled later with conditions and exception handling.

## 12. Interview Quick Review

1. **What is a Python variable?**  
   A name bound to an object.

2. **What does `input()` return?**  
   Always a string.

3. **Why did changing an integer not change the second variable?**  
   Integers are immutable; the changed name was rebound to a new integer object.

4. **Why did appending to a shared list affect both names?**  
   Both names referred to the same mutable list object.

5. **What is the difference between `==` and `is`?**  
   `==` compares values; `is` compares object identity.

6. **Why does `.copy()` change an identity comparison to `False`?**  
   It creates a separate list object with a different identity.

7. **What is the difference between `TypeError` and `ValueError` in today's examples?**  
   `TypeError` occurred when subtracting incompatible types. `ValueError` occurs when a conversion receives an invalid value, such as `int("0.5")`.

## Day 1 Completion Checklist

- [x] Practised variables and core types.
- [x] Compared immutable integers and mutable lists.
- [x] Used assignment and `.copy()`.
- [x] Explained `==` versus `is`.
- [x] Used `input()`, `int()`, and `float()`.
- [x] Triggered and fixed a real `TypeError`.
- [x] Built and ran the Deployment Profile program.
- [x] Passed the Day 1 concept checkpoint.
- [ ] Commit and push Day 1 files.

## One-Minute Recap

> Python names refer to objects. Immutable operations create new objects, while mutable operations can change existing objects. `==` checks values and `is` checks identity. User input is always a string, so numeric calculations require explicit conversion. When code fails, read the traceback from the bottom upward.
