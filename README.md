# 📚 Library Digitization
This project implements a digitization system for books in the IITD library. It provides tools to extract distinct words from each book and supports keyword-based search using custom-built hash tables or sorting-based approaches. Implemented as part of COL106 Assignment 4, it demonstrates both data structure design and algorithmic efficiency.
## 🔍 Problem Overview
Each book consists of a list of words. The library system supports:
- Extracting distinct words from books.
- Performing keyword search across the library.
- Printing books with their respective word sets.

Two core implementations are provided:
- MuskLibrary: Uses MergeSort to extract unique words.
- JGBLibrary: Uses custom-built HashTables with:
  - Chaining (Jobs)
  - Linear Probing (Gates)
  - Double Hashing (Bezos)
## 🧠 Key Features
- ✅ Custom-built HashSet and HashMap with support for insert, find, and dynamic resizing.
- 🔁 Dynamic resizing based on load factor to conserve memory.
- 🧪 Two separate libraries:
  - MuskLibrary: Simpler, sort-based method.
  - JGBLibrary: Advanced, collision-handling hash table approach.
- 📖 Keyword search and book-wise word listing.

## ⏱ Time Complexities

| Function               | MuskLibrary    | JGBLibrary (Hash-based) |
| ---------------------- | -------------- | ----------------------- |
| `__init__`             | `O(kW log W)`  | `O(table size)`         |
| `add_book`             | N/A            | `O(W)`                  |
| `distinct_words`       | `O(D + log k)` | `O(D)`                  |
| `count_distinct_words` | `O(log k)`     | `O(1)`                  |
| `search_keyword`       | `O(k log D)`   | `O(k)`                  |
| `print_books`          | `O(kD)`        | `O(kD)`                 |

## 🧱 Project Structure
> dynamic hash table.py   # DynamicHashSet and DynamicHashMap with resizing
> 
> hash table.py           # Base HashTable, HashSet, and HashMap implementations
> 
> library.py              # MuskLibrary and JGBLibrary classes
> 
> prime generator.py      # Prime number generator for resizing (do not modify)
> 
> main.py                 # Debugging and test file
## ⚠ Constraints & Notes
- ❌ No use of Python dict, set, or hash libraries.
- 📏 All hash tables are implemented from scratch.
- ✅ Follow specific print formatting as required by autograder.
- 🧪 Use DynamicHashSet and DynamicHashMap for space-efficient resizing.

