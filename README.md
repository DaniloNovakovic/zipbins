# zip-bins-csharp

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Python CLI app that zips binary files for projects built with .net framework into a single .zip file

## Installation

To install zipbash cli run `install.sh` script (ex. `./install.sh` from bash terminal) or you can use `pip3` (ex. `pip3 install .`)

## Usage

```cmd
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
                        `--path` (default: "./bins.zip").

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
