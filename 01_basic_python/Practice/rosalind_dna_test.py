 # Input: ATAGATCACGTAGT
import argparse
parser = argparse.ArgumentParser()
parser.add_argument(‘--seq’)
args = parser.parse_args()
sequence = args.seq

 A = 0
 C = 0
 G = 0
 T = 0

 for base in sequence:
     if  base == ‘A’:
        A += 1
	elif base == ‘C’:
	    C += 1
    elif base == ‘G’:
        G += 1
    elif base == ‘T’:
        T += 1

 print(A, C, G, T)

 # Output: 5 2 3 4

