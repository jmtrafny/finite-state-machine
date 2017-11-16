"""
Created on Fri Nov 10 11:55:29 2017

@author: James Trafny

CS332 P1

Python3.6 required to run, if not availible: https://repl.it/OGwx/latest

FSM = {
       S= finite set of strings; represented by user inputed strings
       Sigma= alphabet; input by user, space delineated
       q0= initial state; starting state of the system defined by user
       F= set of final states; acceptable ending states, space delineated
       delta= transition functioin; represented by 2d array with the column
              index representing the input and the row index representing the
              current state.
       }

Usage:  To include a file that has a prebuild fsm, call
            python fsm.py yourmachine.txt

        To create a machine without using an input file that will accept 
            strings in the form of: a+ b* a+
    
             user inputs -> a b
                          > 4
                          > 2
                          > 0
                          > 1
                          > 3
                          > 2
                          > 1
                          > 2
                          > 1
                          > 3
                          > 3
                          
"""

import numpy as np
import sys

# iff the user is including a pre-made fsm
if (len(sys.argv) == 2):
    # tn_fn need to be initialized outside of for loop below
    transition_fn = []    
    # open user included file
    with open(sys.argv[1]) as inFile:
        # for each line in the file...
        for i, line in enumerate(inFile):
            # first line contains alphabet
            if i == 0:   
                alphabet_list = line.strip().split()
                alphabet_dict = {k: v for v, k in enumerate(alphabet_list)}
            # second line contains final states
            if i == 1:
                final_state_list = [int(x) for x in line.split()]
            # third line contains initial states
            if i == 2:
                initial_state_list = line.split()
                initial_state = int(initial_state_list[0])
            # rest of the lines contain the transition function
            if i > 2:
                transition_fn.append([int(x) for x in line.split()])
                
else:
    # Get alphabet from user as list, create a dict with the indicies as values
    alphabet_list = input("Enter alphabet (seperate each symbol by space): ").split()
    cols = size_of_alphabet = len(alphabet_list)
    alphabet_dict = {k: v for v, k in enumerate(alphabet_list)}
    
    # Get state information: Total, Initial, Final
    rows = number_of_states = int(input("Enter number of states: "))
    final_state_list = [int(x) for x in input("Enter the set of final states (seperate each with a space if multiple): ").split()]
    initial_state = int(input("Enter initial state: "))

    # Create transition function represented by 2d array
    transition_fn = np.zeros((number_of_states, size_of_alphabet), dtype=int)
    for i in range(0, rows):
        for j in range(0, cols):
            transition_fn[i][j] = int(input("From state [" + str(i) + 
                                            "], enter next state when input is [" + 
                                             str(alphabet_list[j]) + "]: "))

# Put the machine to work!    
test_again = True
while test_again:
    # Set current state and get test string
    current_state = initial_state
    test_string = input("Enter a string to test (mind your alphabet): ")
        
    for symbol in test_string:
        # Symbol not in alphabet... break out early and reject string
        if symbol not in alphabet_list:
            current_state = -1
            break;
        print("Current State: {0}  Input: {1}".format(current_state, symbol))
        # New state from our transition function
        current_state = transition_fn[current_state][alphabet_dict.get(symbol)]
        
    # rof: Done with this test string    
    print("Finished State: {0}".format(current_state))
       
    # Are we in a Final state?
    if current_state in final_state_list:
        print("\n\n*** String was ACCEPTED ***")
    else:
        print("\n\n*** String was REJECTED ***")
        
    # Test another string?
    ta = input("Test another string? (Y)es or (N)o: ").upper()
    if ta == "Y":
        test_again = True
    else:
        test_again = False