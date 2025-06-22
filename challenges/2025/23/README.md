# Next in the Alphabet

Create a function which returns the next letters alphabetically in a given string.  
If the last letter is a **"Z"**, change the rest of the letters accordingly.

## Examples

```python
next_letters("A")
# Output: "B"
# 'A' becomes 'B' – simple increment.

next_letters("ABC")
# Output: "ABD"
# 'C' becomes 'D' – last character changes without carry.

next_letters("Z")
# Output: "AA"
# 'Z' rolls over to 'A', and since there's no previous letter, we add a new 'A'.
# Think of it like 9 + 1 = 10, here Z + 1 = AA.

next_letters("CAZ")
# Output: "CBA"
# 'Z' → 'A' (carry), 'A' → 'B' (no carry), so "CAZ" becomes "CBA".
# Like incrementing 129 → 130 but in letters.

next_letters("")
# Output: "A"
# Empty input is treated as 0 → return 'A'.
```
