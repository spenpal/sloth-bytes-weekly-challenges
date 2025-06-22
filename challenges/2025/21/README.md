# Remove the Computer Virus

Your computer might have been infected by a virus! Create a function that finds the viruses in files and removes them from your computer.

## Examples

```python
removeVirus("PC Files: spotifysetup.exe, virus.exe, dog.jpg")
# Output: "PC Files: spotifysetup.exe, dog.jpg"

removeVirus("PC Files: antivirus.exe, cat.pdf, lethalmalware.exe, dangerousvirus.exe")
# Output: "PC Files: antivirus.exe, cat.pdf"

removeVirus("PC Files: notvirus.exe, funnycat.gif")
# Output: "PC Files: notvirus.exe, funnycat.gif"
```

## Notes

-   Bad files will contain `"virus"` or `"malware"`, but `"antivirus"` and `"notvirus"` are safe and should **not** be removed.
-   Return `"PC Files: Empty"` if there are no files left on the computer.
