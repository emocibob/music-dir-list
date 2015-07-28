# music-dir-list

A script which lists my `Music` directory into a `txt` or `md` file.
The script is written to run on Windows.

Example of the structure for the `Music` directory.
```
├───Artist A
│   └───[YEAR] Album 1
├───Artist B
│   └───[YEAR] Album 2
│       └───Optional subdir
│           └───Deeper optional subdir
└───Artist C
    ├───[YEAR] Album 3
    └───[YEAR] Album 4
```

Output file example. The album subdirs can be, if specified so, removed from the output.
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

----------

No. of artists: 3
No. of albums: 4
```
