## [Sort basic]

### _Sort_

- Sorting order: Ascending / Descending
- Key: values used to sort
  - ex) book <br/>
    (title, number, book classification code, ...) <- key candidates for sort
- sort types
  - internal sort; sorting inside memory (main memory)
  - external sort; sorting with external storage (HDD)
- sort stability
  - ex 1) 1 diamond, 2 clover, 3 spade, 2 heart (4 cards) <br/>
    (clover is before heart) <br/>
    if ascending order => 1 diamond, 2, 2, 3 spade <br/>
    if front 2 is heart and after is clover => unstable <br/>
    -> it breaks original position
  - ex 2) aa Univ. 18 John, bb Univ. 18 Ann, ... (10000 students) <br/>
    if I want to sort with Univ, StdId, name (ascending order) <br/>
    I can use all three at once to sort them out but it's too hard <br/>
    => if we have a stable algorithm, name -> StdId -> Univ (sorting order) <br/>
    (stable algorithm; keep each sorting stage)

### _Sort way_

- Card game

  - when I play the card game, I sort the cart on my hands
  - ascending order

    1. find the smallest card and locate to first position (selection sort)

       - how to find the smallest card?
         - one array, declare a variable <br/>
           (select smaller card index for each comparison)

       |  Selection Sort  | worst case | best case | average case |
       | :--------------: | :--------: | :-------: | :----------: |
       | time complexity  |   O(n^2)   |  O(n^2)   |    O(n^2)    |
       | space complexity |    O(1)    |   O(1)    |     O(1)     |

    2. library; Put the book on the shelf and arrange it right away (Insertion sort)

       - Insertion Sort 1
       - Insert from one array to another array <br/>
         (use two arrays)
       - Compare every insert and sort
       - Compare numbers from the beginning

       | Insertion Sort 1 | worst case | best case | average case |
       | :--------------: | :--------: | :-------: | :----------: |
       | time complexity  |   O(n^2)   |  O(n^2)   |    O(n^2)    |
       | space complexity |    O(n)    |   O(n)    |     O(n)     |

       - Insertion Sort 2
       - use one array, 1 variable
       - Assume you've got one
       - every compare, and swap
       - Compare numbers from the beginning
       - whe have to shift rest numbers
       - compare 1, shift n <br/>
         compare n, shift 0 <br/>
         each 1 card => operation: n

       | Insertion Sort 2 | worst case | best case | average case |
       | :--------------: | :--------: | :-------: | :----------: |
       | time complexity  |   O(n^2)   |  O(n^2)   |    O(n^2)    |
       | space complexity |    O(1)    |   O(1)    |     O(1)     |

       - Insertion Sort 3
       - use one array, 1 variable
       - Compare numbers from the end
       - we don't have to shift rest numbers
       - reversed case => worst case <br/>
         pre-sorted case => best case (only read)

       | Insertion Sort 3 | worst case | best case | average case |
       | :--------------: | :--------: | :-------: | :----------: |
       | time complexity  |   O(n^2)   |   O(n)    |    O(n^2)    |
       | space complexity |    O(1)    |   O(1)    |     O(1)     |

    3. bubble sort

       - only compare next to number (every compare two numbers)
       - worst case; compare n-1 / swap n-1 (\* n)
       - base case; compare n-1 / swap 0 (\* n)

       |   Bubble Sort    | worst case | best case | average case |
       | :--------------: | :--------: | :-------: | :----------: |
       | time complexity  |   O(n^2)   |  O(n^2)   |    O(n^2)    |
       | space complexity |    O(1)    |   O(1)    |     O(1)     |

- insertion sort (reversed direction) is good <br/>
  among above naive/easy 3 sort ways.

#

### [Note]

- sort example 1) <br/>
  sort 5 number cards [5, 2, 7, 1, 9]
  - Ascending order
    - [1, 2, 5, 7, 9]
  - Descending order
    - [9, 7, 5, 2, 1]
  - how to instruct to computer?
- I need to be able to split up what I can do (think) <br/>
  => and then I can code with computer
- Shell Sort; insertion sort improvement
- Merge Sort/Quick Sort/Heap Sort
- Radix Sort/Counting Sort
- Recommendation: Insertion/Shell/Merge/Quick/Heap Sort
