# The Actual Memory Size of Your USB Flash Drive

Create a function that takes the memory size (`ms`) as an argument and returns the actual memory size.

## Examples

```python
actualMemorySize("32GB")
# Output: "29.76GB"

actualMemorySize("2GB")
# Output: "1.86GB"

actualMemorySize("512MB")
# Output: "476MB"
```

## Notes

-   The actual storage loss on a USB device is 7% of the overall memory size.
-   If the actual memory size is greater than 1 GB, round the result to two decimal places and return it in GB.
-   If the actual memory size after adjustment is less than 1 GB, return the result in MB.
-   For the purposes of this challenge, assume: 1 GB = 1000 MB
