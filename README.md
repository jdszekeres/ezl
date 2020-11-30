# EZL
easy to learn simple programming language
# install
use the executable in directory
# compile
__gcc__ must be installed
``` bash
./ezl filename.ezl
```
if gcc is not installed you can use the --no-gcc argument
# run
``` bash
./filename
```
# examples
calculator
```
PRINT "enter the first digit"
INPUT num
PRINT "type one for addition, two for subtraction"
PRINT "three for multiplication", and four for division"
PRINT "..."
INPUT type
PRINT "what is your second number"
INPUT numtwo
IF type == 1.0 THEN
	PRINT num + numtwo
ENDIF
IF type == 2.0 THEN
	PRINT num - numtwo
ENDIF
IF type == 3.0 THEN
	PRINT num * numtwo
ENDIF
IF type == 4.0 THEN
	PRINT num / numtwo
ENDIF
```
see more in examples folder
