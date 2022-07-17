from Check_Function import *
from Class import *


import sys
inFile = sys.argv[0]

f = open(inFile, "r")

for line in f:


    input = line.split()

    h1 = Hand(input[:5])
    h2 = Hand(input[-5:])

    if h1.get_rank() > h2.get_rank():
        print ("black wins")
    if h2.get_rank() > h1.get_rank():
        print ("white wins")
    if h1.get_rank() == h2.get_rank():
        print ("tie")
