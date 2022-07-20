# filetime.py

A Python module to convert datetime to/from a
[Win32 FILETIME structure](https://msdn.microsoft.com/en-us/library/windows/desktop/ms724284).

[Reference algorithm](https://support.microsoft.com/en-us/help/167296)

## Usage

Install from PyPI: `pip install winfiletime`

Example usage:

```py
import datetime
import winfiletime

# Convert a datetime to a filetime
winfiletime.from_datetime(datetime.datetime(2009, 7, 25, 23, 0))
# 128930364000000000

# Convert a filetime to a datetime
winfiletime.to_datetime(128930364000000000)
# datetime.datetime(2009, 7, 25, 23, 0)
```

## License

This project is hereby released in the Public Domain.
See the `LICENSE` file for the full CC0 license text.
