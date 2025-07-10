`s[i].upper() if i == 0 or s[i-1].isspace()`

- `s[i-1]` does not generate an error because of **short-circuiting** - since the first condition of OR is true `s[i-1]` is not evaluated.
- Similiarly for AND, as soon as the first condition is false, rest of the conditions are not evaluated.
- For the problem I am converting the character to uppercase if its the first one in the string or if the previous character is space
- Using the build it in function `title()` would not work as the it capitalizes the first alphabetical character. For the problem `123alpha` should remain the same as first character is a number.
    - `title()` would convert it in to `123Alpha`.
