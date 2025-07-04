
## Example




All permutations of  are:
.

Print an array of the elements that do not sum to .


## Input Format

Four integers  and , each on a separate line.

## Constraints

Print the list in lexicographic increasing order.

## Sample Input 0

`1
1
1
2`
## Sample Output 0

`[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]`
## Explanation 0

Each variable  and  will have values of  or . All permutations of lists in the form .
Remove all arrays that sum to  to leave only the valid permutations.

## Sample Input 1

`2
2
2
2`
## Sample Output 1

`[[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 2], [0, 2, 1], [0, 2, 2], [1, 0, 0], [1, 0, 2], [1, 1, 1], [1, 1, 2], [1, 2, 0], [1, 2, 1], [1, 2, 2], [2, 0, 1], [2, 0, 2], [2, 1, 0], [2, 1, 1], [2, 1, 2], [2, 2, 0], [2, 2, 1], [2, 2, 2]]`
