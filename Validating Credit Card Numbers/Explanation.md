## Code
```
import re
if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        creditCard = input()
        pattern = r"[456]\d{3}(-?\d{4}){3}$"
        if(not re.match(pattern,creditCard)):
            print("Invalid")
            continue
        repeatCheckPattern = r"(\d)\1{3,}"
        removedsymbols = creditCard.replace("-","")
        if( re.search(repeatCheckPattern,removedsymbols)):
            print("Invalid")
            continue
        else:
            print("Valid")
            
```
` pattern = r"[456]\d{3}(-?\d{4}){3}$" `

- `[456]` checks if the first digit is 4,5 or 6
- \d is the same as `[0-9]`, it checks whether the character is a digit or not
- {3} checks whethere there are 3 digits i.e. the next three digits have to be numbers
- `-?` indicates that a dash may or may not be present
- For now, this just validates whether the rest of the characters are digits or not.
- But for it to be validated as a credit card it shouldn't have more than 4 same consecutive digits
- To check for repetition we use the regular expression: ` repeatCheckPattern = r"(\d)\1{3,}"`
- `\1` after the digit observes one digit and checks if the rest 3 or more characters are repeating. This is how we check for repetition
We do need some practice to quickly grasp these regular expressions!

[regular expressions 101](https://regex101.com/) is a page that lets you test out regular expressions and get possible explanations. Check it out!

## Extra Information that I gathered while working on this code

- `re.match() vs re.search()` - If I use match() it would check if it matches the beginning of the string. So for the current problem it wouldn't work as I need to search whether there are more than 4 consecutive digits anywhere in the string!

 | Quantifier | Meaning                   |
| ---------- | ------------------------- |
| `{3}`      | **Exactly** 3 times       |
| `{3,}`     | **3 or more** times       |
| `{3,5}`    | **Between 3 and 5** times |

- Using $ at the end would check the end of the string so ` repeatCheckPattern = r"(\d)\1{3}$"` would be wrong!

Some notes I asked from ChatGPT:

# 📚 Advanced Regular Expressions – Cheat Sheet with Examples

| **Concept**            | **Regex**                     | **Purpose**                                            | **Example Input**        | **Matches? / Why**                                    |
|------------------------|-------------------------------|--------------------------------------------------------|---------------------------|--------------------------------------------------------|
| **Backreference `\1`** | `(\d)\1{3}`                   | Match a digit repeated 4 times                         | `1111`                    | ✅ Yes – `1` repeated 4 times                          |
|                        |                               |                                                        | `1234`                    | ❌ No – no repetition                                 |
| **Double Word**        | `\b(\w+)\s+\1\b`              | Detect repeated words                                  | `hello hello`             | ✅ Yes – `hello` repeated                             |
|                        |                               |                                                        | `hi there`                | ❌ No repetition                                      |
| **Lookahead**          | `\d(?=\d{3})`                 | Match a digit only if followed by 3 more digits        | `12345`                   | ✅ Matches 1, 2                                        |
|                        |                               |                                                        | `12`                      | ❌ Not enough digits after                            |
| **Negative Lookahead** | `\b(?!cat)\w+`                | Match words that are **not** "cat"                     | `dog cat bird`            | ✅ Matches `dog`, `bird`; ❌ Skips `cat`               |
| **Lookbehind**         | `(?<=\$)\d+`                  | Match numbers **only if preceded by `$`**              | `Price is $200`           | ✅ Matches `200`                                      |
|                        |                               |                                                        | `Cost 200`                | ❌ No `$` before number                               |
| **Negative Lookbehind**| `(?<!\$)\d+`                  | Match number **not** preceded by `$`                   | `Price is 200`            | ✅ Matches `200`                                      |
|                        |                               |                                                        | `$200`                    | ❌ Skipped due to `$`                                 |
| **Non-Capturing Group**| `(?:abc){2}`                  | Match "abcabc", but **don’t create a group**           | `abcabc`                  | ✅ Yes – matches `abcabc`                             |
|                        | `(abc){2}`                    | Captures "abc" and repeats it twice                    | `abcabc`                  | ✅ Yes – also captures `abc` as group 1               |

---

## 📝 Notes

- `\b` → Word boundary (used to ensure full words are matched)
- `\w+` → One or more word characters (a–z, A–Z, 0–9, _)
- `\1`, `\2`, etc. → Backreferences to captured groups
- `(?:...)` → Non-capturing group
- `(?=...)` → Lookahead (positive)
- `(?!...)` → Negative lookahead
- `(?<=...)` → Lookbehind (positive)
- `(?<!...)` → Negative lookbehind

---

💡 Use `re.search()` to apply these patterns to any part of a string. Always prefer raw strings (`r"pattern"`) when writing regex in Python.

