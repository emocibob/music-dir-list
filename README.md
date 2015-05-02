# music-dir-list

The purpose of the program is to list my Music directory into a `txt` or `md` file.

Example of the structure for the Music directory.
```
Artist A
..[YEAR] Album 1
Artist B
..[YEAR] Album 2
....Optional subdir
......Deeper optional subdir
Artist C
..[YEAR] Album 3
..[YEAR] Album 4
```

Output example. The album subdirs can be, if specified so, removed from the output.
```
Artist A
    - [YEAR] Album 1
    
Artist B
    - [YEAR] Album 2
        - Optional subdir
            - Deeper optional subdir
            
Artist C
    - [YEAR] Album 3
    - [YEAR] Album 4
```