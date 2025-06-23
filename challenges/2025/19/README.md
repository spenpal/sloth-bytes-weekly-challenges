# No Yelling

Create a function that transforms sentences ending with multiple question marks `?` or exclamation marks `!` into a sentence ending with only **one** of those punctuation marks. Punctuation **in the middle** of the sentence should remain unchanged.

## Examples

```python
noYelling("What went wrong?????????")
# Output: "What went wrong?"

noYelling("Oh my goodness!!!")
# Output: "Oh my goodness!"

noYelling("I just!!! can!!! not!!! believe!!! it!!!")
# Output: "I just!!! can!!! not!!! believe!!! it!"

noYelling("Oh my goodness!")
# Output: "Oh my goodness!"
```

## Notes

-   Only change ending punctuation — keep the exclamation or question marks in the middle of the sentence the same.
-   Do not worry about mixed punctuation (e.g. no cases ending in ?!??!).
-   Sentences that do not end with ? or ! should remain unchanged.
-   Sentences that end with a single ! or ? should also remain unchanged.
