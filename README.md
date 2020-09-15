# ezl
easy to learn simple programming language
# install
download latest relase
# compile
__gcc__ must be installed
``` bash
cd ezl
./ezl filename.ezl
```
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

