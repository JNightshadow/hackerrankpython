# Explanation of the Regular Expression

```
if(re.match(r'^[a-zA-Z]+[a-zA-Z-\._0-9]*@[a-zA-Z]+\.[a-zA-Z]{1,3}$',addrCheck[1])):
```
`r` - Ensures that backslashes are not interpreted as escape characters.
`[a-zA-Z]+` - Checks if the first character contains alphabets and has atleast one occurence.
`[a-zA-Z-\._0-9]*` - Checks if the characters coming after  alphabets,hyphens,dots or digits.
                     `\` is used as an escape character. Other wise it would check if ANY character is present at the place of dot (.)

`@` - Exactly one occurence of `@`

`[a-zA-Z]+ ` - occurence of one or more alphabets.

`\.` - Checks for exactly one dot (.)

`[a-zA-Z]{1,3}$` - Check for 3 alphabets. `$` indicates it has to have exactly 3 characters and nothing after.
