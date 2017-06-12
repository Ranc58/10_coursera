# Coursera Dump

This programm get 20 random courses from [coursera.org](https://coursera.org)
and create ```coursera.xlsx``` in program folder 
with some information about course: 
1. Course name
2. Course language
3. Start course date
4. Course duration(on weeks)
5. Course rate 

If file already exist - program will add information to it, not rewrite.

# How to Install

Python 3 should be already installed. Then use pip (or pip3 if there is a conflict with old Python 2 setup) to install dependencies:
```bash
pip install -r requirements.txt # alternatively try pip3
```

# Quick launch:

Launching on Linux: 
```bash
$ python coursera.py
Please wait.
Done! Your file "coursera.xlsx" in folder <dirpath>
```
Launching on Windows is same

