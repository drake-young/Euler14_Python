from timeit import default_timer


# ===========================================================
# PROBLEM 14 -- Longest Collatz Sequence
# ===========================================================
#
#  The following iterative sequence is defined for the set
#  of positive integers:
#
#       n --> n/2 (n is even)
#       n --> 3n+1 (n is odd)
#
#  Using the rule above and starting with 13, we generate the
#  following sequence:
#
#  13 --> 40 --> 20 --> 10 --> 5 --> 16 --> 8 --> 4 --> 2 --> 1
#
#  It can be seen that this sequence (starting at 13 and
#  finishing at 1) contains 10 items, Although it has not been
#  proved yet (Collatz Problem), it is thought that all numbers
#  finish at 1.
#
#  Which starting under one million produces the longest chain?
#
#  NOTE: Once the chain starts, the terms are allowed to go
#  above one million
#
# ===========================================================
def problem_14( ):
    # Print Problem Context
    print( "Project Euler Problem 14 -- Longest Collatz Sequence" )

    # Set Up Variables
    start_time  =  default_timer( )
    n           =  1000001
    chainLens   =  [1] * n
    power       =  1
    y           =  2

    # Every Power of two has a chain length equal to the power + 1
    # i.e.
    #   8 = 2^3 (power + 1 = 3 + 1 = 4
    #   8 --> 4 --> 2 --> 1 (chain of length 4)
    # Record these first to begin memoizing results
    while y < len( chainLens ):
        chainLens[y] = power + 1
        y      *=  2
        power  +=  1

    # Iterate through all numbers <= 1,000,000
    for x in range( 1 , n ):
        a = x
        # Iterate through indices. Whenever a chain length is still 1, perform the
        # sequence until a memoized chain is found. updating the appropriate indices
        # in the memo
        while a > 1:
            # only record length of the chain in memo if the start of the chain doesn't exceed the size of the memo
            if a < n:
                if chainLens[a] is not 1:
                    chainLens[x]  +=  chainLens[a] - 1
                    break  # Break while a>1
            chainLens[x]  +=  1

            # Perform the next step of the sequence on a
            if a % 2 is 0:
              a  //=  2
            else:
                a  =  3*a + 1

            continue  # while a>1 (added for readability
        continue  # for x (added for readability

    # Compute Results
    result = chainLens.index( max( chainLens ) )

    # Calculate Execution Time
    end_time = default_timer()
    execution_time = (end_time - start_time) * 1000

    # Display Results
    print( "   Maximum Chain Start:   %d"      %  result )
    print( "   Computation Time:      %.3fms"  %  execution_time )
    return



if __name__ == '__main__':
    problem_14( )