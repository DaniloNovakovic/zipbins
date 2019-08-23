# zip-bins-csharp

Python CLI app that zips binary files for projects built with .net framework into a single .zip file

## Getting started

To install zipbash cli run `install.sh` script (ex. `./install.sh` from bash)

Usage: `zipbins [-h] [-v] [-p PATH] [-o OUTPUT]`

Find and zip all of the compiled csharp binaries to output location

Optional arguments:
  `-h`, `--help`            show this help message and exit
  `-v`, `--version`         show program's version number and exit
  `-p PATH`, `--path PATH`  Path to the root folder (default: `"."`). When entering
                        value you should either use `/` instead of `\` as
                        delimiter (ex. `../dir/subdir`), or wrap path in double
                        quotes (ex. `"c:\dir1\dir2"`)
  `-o OUTPUT`, `--output OUTPUT`
                        Path to the output location relative to the provided
                        `--path` (default: `"./bins.zip"`).

Example: `zipbins -p "c:\dev\myproj" -o "../myproj-bins.zip"`
