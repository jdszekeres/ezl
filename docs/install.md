# install 
### pre-compiled
#### the easy way
* download the latest release
* use as following
 ```bash
./ezl filename.ezl
```
### download from source
#### the hard way
* clone the repo
```bash
git clone https://www.github.com/jdszekeres/ezl.git
```
* install pyinstaller
```bash
pip3 install pyinstaller
```
* build
``` bash
python3 -m pyinstaller --onefile ezl.py
```
* your executable is in the dist folder
