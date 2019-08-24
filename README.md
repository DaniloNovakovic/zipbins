# zip-bins-csharp

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Python CLI app that zips binary files for projects built with .net framework into a single .zip file

---

## Installation

The recommended version of Python is 3.7.x as other versions have not yet been tested.

### install.sh

The best way to install (and uninstall) your Python CLI app is to use pip (pip3 for Python 3). In the root directory of the CLI source code, running `pip3 install .` will install this app using `setup.py` as “instructions”. Likewise, running `pip3 uninstall zipbins` will remove the app.

I decided to put this logic in a shell script so that I didn’t have to always manually type out these commands (which gets very tedious when you are actively developing a CLI app). So I dump it all in a shell script.

`pip3 install -e .`

Now all I have to do is run `install.sh` to “recycle” the CLI on my machine with current source code.

> Big thanks to [Thomas Stringer](https://github.com/trstringer) for his blog which you can read [here](https://medium.com/@trstringer/the-easy-and-nice-way-to-do-cli-apps-in-python-5d9964dc950d)

---

## Usage

```bash
$ zipbins --help
usage: zipbins [-h] [-v] [-p PATH] [-o OUTPUT]

Find and zip all of the compiled csharp binaries to output location

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         show program's version number and exit
  -p PATH, --path PATH  Path to the root folder (default: "."). When entering
                        value you should either use "/" instead of "\" as
                        delimiter (ex. ../dir/subdir), or wrap path in double
                        quotes (ex. "c:\dir1\dir2")
  -o OUTPUT, --output OUTPUT
                        Path to the output location relative to the provided
                        `--path` (default: "./bins.zip")

Example: zipbins -p "c:\dev\myproj" -o "../myproj-bins.zip"
```

---

## Support

Reach out to me at one of the following places!

- Website at [danilonovakovic.github.io](https://danilonovakovic.github.io/index.html)
- Linkedin at [DaniloNovakovic](https://www.linkedin.com/in/danilo-novakovi%C4%87-821934167/)

---

## License

- **[MIT license](http://opensource.org/licenses/mit-license.php)**
- Copyright 2019 © [DaniloNovakovic](https://github.com/DaniloNovakovic)
