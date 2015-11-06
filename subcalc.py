#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys

def subcalc(slash):
    """    Subcalc is a simple function to convert a slash-notation netmask 
        into a dotted decimal notation netmask.

        Usage: subcalc(netmask)
        Example: subcalc (24)
                 will return 255.255.255.0

        Note: As input to subcalc, enter only the number, not the leading slash.
              If an invalid slash-notation netmask is sent to subcalc.
              it will return -1
    """
    # Check if the value is an int, if it's not then quit and return -1
    if isinstance(slash, int) == False:
        return -1
        sys.exit()
    # Check the size of the netmask, if bogus, then quit end return -1
    if slash < 0 or slash > 32:
        return -1
        sys.exit()

    zeroes = "0" * (32-slash) # Fill up "the rest" with zeroes
    binNum = "1" * slash # Fill up the binary string with ones
    binNum = binNum + zeroes # Put together the ones and the zeroes (tot = 32)
    sub = "" # Initalize sub-variable

    # Divide the binary string into four groups
    group = []
    group.append(binNum[0:8])
    group.append(binNum[8:16])
    group.append(binNum[16:24])
    group.append(binNum[24:])

    # For each group, convert to decimal type and end with a dot and append
    # the result to the sub-variable
    for i in group:
        sub += (str(int(i, 2))+".")
    return sub.rstrip(".") # Strip of the last dot

def main():
    # A simple implementation of the subcalc-function above
    # Takes one command-line argument (the netmask)
    if len(sys.argv) < 2: 
        print "Usage: subcalc.py <netmask in slash-notation>"
        print "Example: subcalc.py 24"
        sys.exit()
    arg = int(sys.argv[1]) # Have to typecast here since arguments are strings
    print subcalc(arg)
    
    #help(subcalc)

if __name__=='__main__':
    main()
