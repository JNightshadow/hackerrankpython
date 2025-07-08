## How to change values of string by their index?
As strings are immutable, once declared we cannot change the value by its index. The following lines would raise an error:
` string[5] = 'k' `
`TypeError: 'str' object does not support item assignment`

But we can manipulate strings in two ways:
1. Convert the string in to a list and change the value.
2. Slice the string and join it back.

```
string = 'Hello'
l = list(string)
l[0] = B
string = ''.join(l)
print(string)
```
> Bello

```
string = "Hello"
string = "B" + string[1:]
