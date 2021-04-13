# INFO-H413-Implementation Exercise 1

-Iterative Improvement for the PFSP (Permutation Flow Shop Scheduling Problem)
-Variable Neighbourhood Descent algorithms for the PFSP

Usage : python flowshop.py instance [options]

Options :  
--vnd for Variable Neighbourhood Descent (Iterative Improvement by default)
--first or --best for First or Best improvement pivoting rule
--transpose --exchange or --insert for the neighbourhood rule
--random-init or --srz for the initial solution
--tei or --tie for the neighbourhood order (VND)

Examples :
python flowshop.py ./instances/50_20_01 --srz --first --transpose
python flowshop.py ./instances/50_20_01 --random --vnd --tei
