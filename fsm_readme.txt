To create your own machine, create a text file of the following form:

Line 1:    Language alphabet; can be any set of symbols space delineated.
Line 2:    Set of final accepting states, must be integers space delineated;
Line 3:    Initial state, single integer value.
Lines 4-n: Transition function with the index representing the input and line representing state.

The three included files (m1.txt, m2.txt, and m3.txt) contain example machines.

m1 will accept strings in the form: a(a^b)*a
m2 will accept strings in the form: 0*1*2*
m3 will accept strings in the form: a+b+a*

To include a file with the script, type:

python fsm.py m1.txt

where m1.txt is the file you wish to include.