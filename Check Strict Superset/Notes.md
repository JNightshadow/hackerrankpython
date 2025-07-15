This program is just to show us that using sets are faster and efficient compared to lists.
- It eliminates duplicates.
- It takes O(1) time for subset checking whereas in list it would take O(n) time.

  ---
  Here's a table thanks to ChatGPT!

| Feature                | `set`                            | `list`                            |
|------------------------|----------------------------------|------------------------------------|
| ✅ Subset Checking     | `O(1)` average time per item     | `O(n)` time per item               |
| ✅ Uniqueness          | Automatically removes duplicates | Keeps duplicates                   |
| ✅ Faster Lookup       | Hash-based (like a dictionary)   | Needs to scan every element        |
| ✅ Clean Subset Syntax | `subset.issubset(A)`             | No direct equivalent               |
| ❌ Ordered             | ❌ No                             | ✅ Yes                             |

