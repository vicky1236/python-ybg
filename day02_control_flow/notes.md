# Day 2 — Operators and Control Flow

> **Focus:** Arithmetic, comparisons, Boolean logic, conditional branches, loops, `range()`, `continue`, and `break`.

## Learning Outcomes

By the end of Day 2, I can:

- Use arithmetic operators to calculate infrastructure capacity.
- Explain the difference between `/`, `//`, and `%`.
- Create Boolean expressions with comparison operators.
- Combine conditions using `and`, `or`, and `not`.
- Build ordered decision trees with `if`, `elif`, and `else`.
- Explain why the first matching branch wins.
- Repeat work with `for`, `range()`, and `while` loops.
- Control loop execution using `continue` and `break`.
- Recognize how a missing state update can create an infinite loop.
- Build a DevOps-focused Deployment Decision Engine.

## 1. Arithmetic Operators

| Operator | Purpose | Example | Result |
|---|---|---|---:|
| `+` | Addition | `5 + 2` | `7` |
| `-` | Subtraction | `5 - 2` | `3` |
| `*` | Multiplication | `5 * 2` | `10` |
| `/` | Normal/true division | `17 / 4` | `4.25` |
| `//` | Floor division | `17 // 4` | `4` |
| `%` | Remainder/modulo | `17 % 4` | `1` |
| `**` | Exponent/power | `2 ** 3` | `8` |

### `/`, `//`, and `%`

Suppose 17 pods must be distributed across nodes that each support four pods:

```python
total_pods = 17
pods_per_node = 4

print(total_pods / pods_per_node)   # 4.25
print(total_pods // pods_per_node)  # 4
print(total_pods % pods_per_node)   # 1
```

- `/` returns the full division result.
- `//` returns the number of complete groups for positive values.
- `%` returns the number remaining after those complete groups.

Four nodes hold 16 pods, but the remaining pod still requires another node.

```python
fully_occupied_nodes = total_pods // pods_per_node
remaining_pods = total_pods % pods_per_node
required_nodes = fully_occupied_nodes

if remaining_pods > 0:
    required_nodes += 1

print(required_nodes)  # 5
```

## 2. Comparison Operators

Comparison expressions return `True` or `False`.

| Operator | Meaning | Example |
|---|---|---|
| `==` | Equal values | `environment == "prod"` |
| `!=` | Values are not equal | `status != "healthy"` |
| `>` | Greater than | `cpu_usage > 90` |
| `<` | Less than | `replicas < 3` |
| `>=` | Greater than or equal | `cpu_usage >= 90` |
| `<=` | Less than or equal | `attempt <= max_attempts` |

Do not confuse assignment with value comparison:

```python
environment = "prod"       # Assignment
environment == "prod"      # Comparison: True
```

## 3. `if`, `elif`, and `else`

Conditional statements allow a program to select one path.

```python
if cpu_usage >= 90:
    status = "CRITICAL"
elif cpu_usage >= 70:
    status = "WARNING"
else:
    status = "HEALTHY"
```

- `if` checks the first condition.
- `elif` is checked only when every earlier condition was false.
- `else` runs when no previous condition matched.
- Only the first matching branch executes.

### Why Branch Order Matters

CPU `95` satisfies both of these comparisons:

```text
95 >= 90 → True
95 >= 70 → True
```

The critical threshold must come first. If `>= 70` came first, Python would classify `95` as `WARNING` and never check the critical branch.

General rule:

> Arrange overlapping branches from the most specific or highest-priority condition to the broader condition.

## 4. First-Match Decision Flow

Consider this order:

```python
if deployment_frozen:
    reason = "Deployment is frozen"
elif not tests_passed:
    reason = "Tests failed"
elif cpu_usage >= 90:
    reason = "High CPU usage"
```

If deployment is frozen, tests failed, and CPU is 95, the selected reason is:

```text
Deployment is frozen
```

Python enters the first matching branch and skips the remaining `elif` branches. It does not automatically choose the condition that looks most severe.

## 5. Boolean Logic

Boolean operators combine or reverse conditions.

### `and`

`A and B` is `True` only when both expressions are true.

| A | B | A `and` B |
|:---:|:---:|:---:|
| `True` | `True` | `True` |
| `True` | `False` | `False` |
| `False` | `True` | `False` |
| `False` | `False` | `False` |

### `or`

`A or B` is `True` when at least one expression is true.

| A | B | A `or` B |
|:---:|:---:|:---:|
| `True` | `True` | `True` |
| `True` | `False` | `True` |
| `False` | `True` | `True` |
| `False` | `False` | `False` |

### `not`

`not` reverses a Boolean value:

```python
not True   # False
not False  # True
```

### Deployment Authorization Example

```python
tests_passed = True
approval_received = False
emergency_change = True
deployment_frozen = False

can_deploy = (
    tests_passed
    and (approval_received or emergency_change)
    and not deployment_frozen
)
```

Evaluation:

```text
approval_received or emergency_change → False or True → True
not deployment_frozen                 → not False → True
True and True and True                → True
```

Parentheses make the intended grouping clearer.

## 6. Converting `yes`/`no` Input to Boolean

`input()` returns a string. Comparing that string with `"yes"` produces a Boolean:

```python
tests_passed = input("Tests passed? yes/no: ") == "yes"
```

| User input | Comparison | Stored value |
|---|---|:---:|
| `yes` | `"yes" == "yes"` | `True` |
| `no` | `"no" == "yes"` | `False` |

After this conversion, `tests_passed` is Boolean. Do not compare it again with the string `"yes"`:

```python
if tests_passed:          # Correct
    print("Tests passed")

if not tests_passed:      # Correct check for failed tests
    print("Tests failed")
```

For the current exercise, inputs must use exact lowercase `yes` or `no`. Normalizing input will be covered with string methods.

## 7. `for` Loops

A `for` loop processes each item in an iterable.

```python
cpu_readings = [40, 75, 95]

for cpu_usage in cpu_readings:
    if cpu_usage >= 90:
        status = "CRITICAL"
    elif cpu_usage >= 70:
        status = "WARNING"
    else:
        status = "HEALTHY"

    print(f"CPU: {cpu_usage}% | Status: {status}")
```

The loop variable receives one value per iteration:

```text
Iteration 1 → cpu_usage = 40
Iteration 2 → cpu_usage = 75
Iteration 3 → cpu_usage = 95
```

Code indented inside the loop repeats. Code aligned outside the loop runs after the loop finishes.

## 8. `range()`

`range()` generates integers commonly used for fixed-count repetition.

```python
for attempt in range(1, 4):
    print(attempt)
```

Output:

```text
1
2
3
```

The stop value is excluded:

```text
range(1, 4) → 1, 2, 3
range(4)    → 0, 1, 2, 3
range(5)    → 0, 1, 2, 3, 4
```

The full form is:

```python
range(start, stop, step)
```

## 9. `while` Loops

A `while` loop repeats while its condition remains true.

```python
attempt = 1
max_attempts = 3

while attempt <= max_attempts:
    print(f"Health check attempt: {attempt}")
    attempt += 1
```

The loop prints attempts 1, 2, and 3. After the last increment, `attempt` becomes 4 and the condition becomes false.

### Infinite Loop Risk

If the state controlling the condition never changes, the loop may never end:

```python
attempt = 1

while attempt <= 3:
    print(attempt)
    # Missing attempt increment
```

Here, `attempt` stays `1`, so `1 <= 3` remains true forever. Use `Ctrl+C` to interrupt an accidental infinite terminal loop.

## 10. Compound Assignment

These statements are equivalent:

```python
attempt = attempt + 1
attempt += 1
```

Other compound operators include `-=`, `*=`, and `/=`.

## 11. `continue` and `break`

### `continue`

Skips the remaining code in the current iteration and begins the next iteration.

### `break`

Terminates the entire loop immediately.

```python
for attempt in range(1, 6):
    if attempt == 2:
        print("Attempt 2 skipped")
        continue

    if attempt == 4:
        print("Attempt 4 succeeded")
        break

    print(f"Attempt {attempt} failed")
```

Output:

```text
Attempt 1 failed
Attempt 2 skipped
Attempt 3 failed
Attempt 4 succeeded
```

Attempt 2 does not print `failed` because `continue` skips the rest of that iteration. Attempt 5 never starts because `break` ends the loop during attempt 4.

Key rule:

```text
continue → skip this iteration's remaining work and keep looping
break    → stop the entire loop
```

## 12. Day 2 Mini-Project — Deployment Decision Engine

The program evaluates deployment safety gates and deploys replicas only after approval.

```python
service_name = input("Enter service name: ")
env_name = input("Enter environment name: ")
cpu_usage = int(input("Enter CPU usage percentage: "))
desired_replicas = int(input("Enter desired replicas: "))
tests_passed = input("Enter tests passed (yes or no): ") == "yes"
approval_received = input("Enter approval received (yes or no): ") == "yes"
deployment_frozen = input("Enter deployment frozen (yes or no): ") == "yes"

if deployment_frozen:
    decision = "BLOCKED"
    reason = "Deployment is frozen"
elif not tests_passed:
    decision = "BLOCKED"
    reason = "Tests failed"
elif cpu_usage >= 90:
    decision = "BLOCKED"
    reason = "High CPU usage"
elif env_name == "prod" and not approval_received:
    decision = "BLOCKED"
    reason = "Production approval was not received"
else:
    decision = "APPROVED"
    reason = "All conditions met for deployment"

print("\n=== Deployment Decision ===")
print(f"Service: {service_name}")
print(f"Environment: {env_name}")
print(f"Decision: {decision}")
print(f"Reason: {reason}")

if decision == "APPROVED":
    for replica in range(1, desired_replicas + 1):
        print(f"Deploying replica {replica} of {desired_replicas}")

    print("Deployment completed")
```

### Decision Priority

1. Deployment freeze
2. Failed tests
3. Critical CPU usage
4. Missing production approval
5. Approval when all checks pass

The ordering is an explicit business rule. Moving a branch changes which reason wins when multiple conditions are true.

## 13. Debugging Lessons

### `ValueError`

Entering `yes` when Python expects desired replicas causes:

```python
desired_replicas = int("yes")
```

```text
ValueError: invalid literal for int()
```

The value has the correct source type (`str`) but invalid content for integer conversion. Exception handling will later make this user-friendly.

### `NameError`

Using `decision` before assigning it would raise `NameError`. Every possible branch must assign values that later code requires.

### `IndentationError`

Blocks under `if`, `elif`, `else`, `for`, and `while` require consistent indentation.

## 14. Interview Quick Review

1. **What is the difference between `/`, `//`, and `%`?**  
   `/` returns true division, `//` returns the floor-division quotient, and `%` returns the remainder.

2. **Does Python evaluate every `elif` condition?**  
   No. It stops after the first matching branch.

3. **What is the difference between `and` and `or`?**  
   `and` requires every operand to be truthy; `or` requires at least one truthy operand.

4. **What does `not` do?**  
   It reverses the truth value of an expression.

5. **Why is the stop value excluded from `range()`?**  
   Python defines `range` as a half-open interval: start included, stop excluded.

6. **When should `for` be preferred over `while`?**  
   Use `for` when iterating over items or a known range. Use `while` when repetition depends on a changing condition.

7. **What causes an infinite `while` loop?**  
   The condition never becomes false, often because the controlling state is not updated.

8. **What is the difference between `continue` and `break`?**  
   `continue` skips to the next iteration; `break` exits the loop.

## Day 2 Completion Checklist

- [x] Used arithmetic, floor division, and modulo.
- [x] Calculated required infrastructure capacity.
- [x] Built `if/elif/else` decision trees.
- [x] Practised comparison and Boolean operators.
- [x] Iterated over values with `for`.
- [x] Used `range()` with an excluded stop value.
- [x] Built and safely terminated a `while` loop.
- [x] Explained `continue` and `break`.
- [x] Triggered and understood a real `ValueError`.
- [x] Built and tested the Deployment Decision Engine.
- [x] Passed the Day 2 checkpoint.
- [x] Committed and pushed Day 2 files.

## One-Minute Recap

> Operators calculate and compare values. Boolean expressions combine deployment gates. An `if/elif/else` chain executes only the first matching branch, so ordering is part of the program's behaviour. `for` loops iterate over items or ranges, while `while` loops repeat until a condition changes. `continue` skips the rest of one iteration; `break` stops the entire loop.
