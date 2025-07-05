## Using list comprehension to find average:

```
average = sum([x for x in student_marks[query_name]]) / len(student_marks[query_name])
print(f"{average:.2f}")  # Output: 26.50

```
Here, memory gets allocated.

## Using generator expression to find average

```
average = sum(x for x in student_marks[query_name]) / len(student_marks[query_name])
print(f"{average:.2f}")  # Output: 26.50

```
Here memory isn't allocated yet so performance will be good for large lists. (Lazy allocation)
