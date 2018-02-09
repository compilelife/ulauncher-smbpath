Extension for [ulauncher](https://ulauncher.io/) which convert samba path between linux and windows world. 

In Linux world, you got samba path like `smb://127.0.0.1/compilelife`. 

But Windows' guy sends you their samba path like `\\127.0.0.1\compilelife`.

Then, conmunication becomes complicated.

To make it eaysier, convert it with smbpath.py:

```
python smbpath.py smb://127.0.0.1/compilelife
```

or

```
python smbpath.py \\127.0.0.1\compilelife
```

The easiest way:

![linux->windows shot](images/1.png)

![windows->linux shot](images/2.png)

Alt+1 or just enter to copy then converted path to clipboard.

Enjoy it.