# Binary Search Algorithms
This repository contains Python code implementing two different methods for searching elements in a list: a slow linear search method (`typ_search`) and a more efficient binary search method (`bin_search`).

### typ_search
- The `typ_search` function performs a linear search through a given list to find a target element.
- It iterates through each element of the list and compares it with the target element until a match is found or the end of the list is reached.
- This method has a time complexity of O(n), where n is the number of elements in the list.

### bin_search
- The `bin_search` function implements a binary search algorithm to find a target element in a sorted list.
- It divides the search space in half at each step by comparing the target element with the middle element of the current range.
- This method has a time complexity of O(log n), making it much faster than linear search for large lists.

### Performance Analysis
The repository also includes code to compare the performance of the two search algorithms. You can measure the average time taken by each algorithm to search for elements in a large sorted list.

### License
This project is licensed under the [Apache 2.0](LICENSE) - see the LICENSE file for details.

*Feel free to clone down this repository and test it out yourself!*
