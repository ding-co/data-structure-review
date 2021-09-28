## [Search]

### _Hash Table (Map)_

- Hash Table / Hash Map

  - use Hash Key -> put data into a Bucket
  - Hash Function
    - can be used to map data of arbitrary size to data of fixed size
  - T.C: O(1)

- Choosing a hash function

  - good hash function conditions
    - calculate fast
    - crash times small
      - different key -> different value
    - values are uniform-distributed
  - representative of Hash Function
    - h(k) = k mod M (prime number)
    - intermediate square: square -> extract specific bits
    - Folding: fold and add
    - bit extraction
    - number analysis, ...

- Collision resolution
  - Chaining
  - Open addressing (extra space X)
    - Linear probing (+n)
    - Quadratic probing (+n^2)
    - Double hashing

#

## [Note]

- Hash
  - Data Structure
    - for search
    - key -> bucket
    - like a mail box
  - Encryption/Security
    - val = hash_f(key)
    - key -> unique value (different)
    - not crashed value
    - value -> key difficult (for security)
- Static Hashing
  - bucket size always fixed
- Dynamic Hashing

  - Data input many => bucket size increase

- Hash vs. Balanced Tree
  - Hash
    - pros: insert/delete => O(1); bucket size big enough + Hash Function good
    - cons: O(n) + alpha; Collision too much <br/>
      storage waste
  - Balanced Tree
    - pros: insert/delete/search => O(log n) <br/>
      storage not waste <br/>
      inorder-traverse; sorted
    - cons: slower than Hash
