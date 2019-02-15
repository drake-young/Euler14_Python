# Euler14_Python

Problem 14 of Project Euler solved in Python 3 using PyCharm. The approach used to solve this problem involves memoizing chain lengths, and using pre-computed lengths to simplify computation of future lengths. Algorithm is subject for improvement as its current runtime speed is the slowest of the first 14 problems at the moment. may be subject to be updated in the future. 

## Project Euler Problem 14 -- Longest Collatz Sequence

The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)<br/>
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

**NOTE:** Once the chain starts the terms are allowed to go above one million.

## Authors

* **Drake Young** - *Initial work* - [drake-young](https://github.com/drake-young)

See also the list of [contributors](https://github.com/drake-young/Euler14_Python/contributors) who participated in this project.

## Additional Links and References

* [Project Euler Homepage](https://projecteuler.net/about)
* [Project Euler Problem 14](https://projecteuler.net/problem=14)
* [.gitignore template](https://github.com/github/gitignore/blob/master/Global/JetBrains.gitignore)
