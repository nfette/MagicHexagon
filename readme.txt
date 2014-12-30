About

Here you can see the puzzle:
http://www.uncommongoods.com/product/aristotles-number-puzzle

Here is one blog of a some arithmetic simplifications for a solution:
http://hwiechers.blogspot.com/2013/03/solving-artitotles-number-puzzle.html

Here are some amazingly short codes to solve:
http://codegolf.stackexchange.com/questions/24891/solve-aristotles-number-problem

In the solution presented here, I counted how many combinations of 3,
4, and 5 numbers add to 38. Then I used these sets as the building
blocks for the solution, iteratively inserting them into rows and
checking whether they match the other rows. But first, finding that
there are relatively fewer combinations of 3 numbers adding to 38, I
started by assembling the outside edge. By iterating over sets for the
building blocks, symmetry is built-in an no duplication occurs. The
number of outside edge arrangements shrinks by checking that adjacent
sets actually have the same number (think, the graph has one loop).
At that point, there are only a few thousand edge arrangements, and
a few hundred options for the next row to insert. For the next several
rows inserted, the number of valid arrangements decreases, until
the puzzle is completely filled.

So anyhow, this is an inefficient solution, but a fun use for the
set() type and itertools in Python.
