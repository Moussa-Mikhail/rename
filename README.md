# rename
Small Python script used to batch rename files using regex.

## Example usage
rename.py must be placed in the folder it will be used in (or in a folder included in PATH). If it is placed in PATH then it will called by "rename.py", quotes included in the command.

Example files before running
```
folder
├── file 1.txt
├── file 2.txt
├── file 3.txt
├── file 4.docx
└── rename.py
```

Example command
```
C:\path\to\folder>rename.py
Match: (\w+) (\d).txt
Replacement: \2 \1.txt
```

If rename.py is placed in PATH then it will be called by
```
C:\path\to\folder>"rename.py"
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
