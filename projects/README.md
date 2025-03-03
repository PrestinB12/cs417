# Requirements

  * Python 3.7

> This code makes use of the `f"..."` or [f-string
> syntax](https://www.python.org/dev/peps/pep-0498/). This syntax was
> introduced in Python 3.6.

# Sample Execution & Output
If run without command line arguments, using python .\parse_temps_demo.py

```
python ./
```

an error will occur

If run using

```
python .\parse_temps_demo.py .\data\sensors-2018.12.26.txt
```

the output will be

```
...
time=35220 temps=[35.0, 35.0, 44.0, 32.0]
time=35250 temps=[23.0, 24.0, 20.0, 21.0]
time=35280 temps=[22.0, 24.0, 20.0, 21.0]
time=35310 temps=[22.0, 22.0, 19.0, 20.0]
time=35340 temps=[22.0, 22.0, 19.0, 20.0]
time=35370 temps=[22.0, 21.0, 18.0, 19.0]
time=35400 temps=[22.0, 21.0, 18.0, 20.0]
time=35430 temps=[25.0, 27.0, 23.0, 24.0]
time=35460 temps=[21.0, 22.0, 19.0, 20.0]
time=35490 temps=[73.0, 75.0, 63.0, 71.0]
time=35520 temps=[80.0, 80.0, 69.0, 76.0]
time=35550 temps=[61.0, 63.0, 51.0, 57.0]
time=35580 temps=[78.0, 77.0, 66.0, 78.0]
time=35610 temps=[81.0, 80.0, 69.0, 76.0]
```
