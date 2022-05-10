# rename
small Python script used to batch rename files using regex

## Example usage
rename.py must be placed in the folder it will be used in (or in a folder in your PATH variable).

Example files before running
```
folder
├── file 1.txt
├── file 2.txt
├── file 3.txt
├── file 4.docx
└── rename.py
```


```
folder>python rename.py
Pattern: (\w+) (\d).txt
Replacement: \2 \1.txt
```

Files after running

```
folder
├── 1 file.txt
├── 2 file.txt
├── 3 file.txt
├── file 4.docx
└── rename.py
```
