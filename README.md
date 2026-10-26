# Data Structures & Algorithms Experiments

> A collection of small, dependency-free Python implementations that demonstrate core data-structure operations and algorithmic techniques.

This repository is an educational set of seven self-contained experiments. Each script implements a focused concept and includes an executable demonstration with representative test cases. It is intended for learning, practice, and quick reference—not as a production-ready data-structures library.

## Topics covered

- Linear and binary search
- Selection sort and bubble sort
- Stack-based undo/redo
- FIFO event queues
- Hash tables using separate chaining and linear probing
- Depth-first search (DFS) and breadth-first search (BFS)

## Requirements

- Python **3.x**
- No third-party packages or installation steps are required.

## Quick start

Clone the repository and run any experiment from its root directory:

```bash
git clone <your-repository-url>
cd DS-Experiments
python E1LBsearch.py
```

Run every demonstration at once:

```bash
for file in E*.py; do python "$file"; done
```

On Windows PowerShell:

```powershell
Get-ChildItem E*.py | ForEach-Object { python $_.Name }
```

## Experiments

| # | File | Concept | What it demonstrates |
|---|---|---|---|
| 1 | `E1LBsearch.py` | Searching | Linear search and binary search, including found and missing values. |
| 2 | `E2SBsort.py` | Sorting | Selection sort, optimized bubble sort, and extracting the five largest salaries. |
| 3 | `E3stack.py` | Stack | A text editor state model with `make_change`, `undo`, `redo`, and `display`. |
| 4 | `E4EventDeQue.py` | Queue | A bounded FIFO event queue with event addition, processing, display, and cancellation. |
| 5 | `E5HashTableChaining.py` | Hashing | Key-value storage using separate chaining to resolve collisions. |
| 6 | `E6HashTableLinearProbing.py` | Hashing | Open-addressed hash table using linear probing and a deleted-entry marker. |
| 7 | `E7DFSBFS.py` | Graph traversal | DFS over an adjacency matrix and BFS over an adjacency list. |

The matching `E1LBsearch.txt` through `E7DFSBFS.txt` files are text copies of the corresponding experiment source files.

---

## Experiment details

### 1. Searching algorithms — `E1LBsearch.py`

- `linear_search(arr, target)` checks each value in order and returns `(found, index)`.
- `binary_search(arr, target)` repeatedly halves a **sorted** sequence and returns `(found, index)`.
- The included demonstration sorts each input before running binary search, so its returned index refers to the sorted list rather than the original list.

```bash
python E1LBsearch.py
```

| Algorithm | Time complexity | Extra space |
|---|---:|---:|
| Linear search | `O(n)` | `O(1)` |
| Binary search (sorted input) | `O(log n)` | `O(1)` |

### 2. Sorting algorithms — `E2SBsort.py`

- `selection_sort(arr)` repeatedly places the smallest remaining value at the next position.
- `bubble_sort(arr)` swaps neighboring out-of-order values and exits early when a pass makes no swaps.
- `get_top_five(sorted_arr)` returns up to five highest values from an ascending-sorted list, in descending order.
- Both sorting functions copy their input, preserving the original list.

```bash
python E2SBsort.py
```

| Algorithm | Time complexity | Extra space in this implementation |
|---|---:|---:|
| Selection sort | `O(n²)` | `O(n)` (input copy) |
| Bubble sort | `O(n²)` worst case | `O(n)` (input copy) |

> The textbook in-place versions of these sorting algorithms use `O(1)` extra space. These functions use `arr.copy()` deliberately to avoid mutating the caller's list.

### 3. Undo/redo stack — `E3stack.py`

`TextEditor` models document history with two Python lists:

- `undo_stack` stores prior document states.
- `redo_stack` stores states that can be restored after an undo.
- `make_change(new_state)` saves the current state to undo history and clears redo history.
- `undo()` moves one state from undo history to redo history.
- `redo()` moves one state from redo history back to undo history.
- `display()` prints the current state.

```bash
python E3stack.py
```

The example performs edits, undo operations back to an empty document, and a redo operation.

### 4. Event queue — `E4EventDeQue.py`

`EventQueueSystem` is a bounded FIFO queue with a default capacity of 10 events.

- `add_event(event)` appends an event unless the queue is full.
- `process_event()` removes and processes the oldest event.
- `cancel_event(event)` removes a matching pending event.
- `display_events()` prints pending events from front to rear.

```bash
python E4EventDeQue.py
```

The implementation uses a Python list. Appending is amortized `O(1)`, while `pop(0)` and removing an event are `O(n)`. A `collections.deque` would provide `O(1)` removal from the front in a production queue.

### 5. Hash table with separate chaining — `E5HashTableChaining.py`

`HashTableChaining` stores integer keys and values in a fixed-size bucket array.

- The hash function is `key % size`.
- Each bucket is a list of `[key, value]` pairs.
- Colliding keys share a bucket (for example, `15` and `25` both map to index `5` in a table of size `10`).
- `insert` adds a key or updates an existing key; `search` retrieves its value; `delete` removes it.

```bash
python E5HashTableChaining.py
```

Average insert/search/delete time is `O(1)` with a good distribution of keys; in the worst case, operations are `O(n)` when many keys occupy one bucket.

### 6. Hash table with linear probing — `E6HashTableLinearProbing.py`

`HashTableLinearProbing` demonstrates open addressing with integer keys.

- The initial position is calculated with `key % size`.
- A collision advances one slot at a time, wrapping around the table.
- Deletions set a slot to the `"DELETED"` sentinel rather than `None`, so probes can continue past deleted entries.
- `display()` prints the table contents and slot indexes.

```bash
python E6HashTableLinearProbing.py
```

Expected operations are `O(1)` at a reasonable load factor; a probe can take `O(size)` in the worst case. The fixed-capacity table reports an overflow if no usable slot remains.

### 7. Graph traversal — `E7DFSBFS.py`

This experiment represents the same undirected graph in two forms:

- **DFS** uses an adjacency matrix and recursive traversal starting at node `A`.
- **BFS** uses an adjacency list and a queue starting at node `A`.

```bash
python E7DFSBFS.py
```

Example traversal output:

```text
DFS: A B D C E
BFS: A B C D E
```

DFS scans each matrix row, so this implementation runs in `O(V²)`. BFS is conceptually `O(V + E)` with an efficient queue; because it uses `list.pop(0)`, its current queue removal can make the implementation `O(V²)` in the worst case. Replacing the list with `collections.deque` would retain `O(V + E)` traversal time.

## Project structure

```text
DS-Experiments/
├── E1LBsearch.py                 # Linear and binary search
├── E2SBsort.py                   # Selection sort, bubble sort, top-five query
├── E3stack.py                    # Stack-based text editor history
├── E4EventDeQue.py               # Bounded event queue
├── E5HashTableChaining.py        # Hash table with separate chaining
├── E6HashTableLinearProbing.py   # Hash table with linear probing
├── E7DFSBFS.py                   # DFS and BFS graph traversals
├── E1LBsearch.txt ... E7DFSBFS.txt # Text copies of the experiment sources
└── README.md
```

## Verification

Each Python file contains its own demonstration cases and can be run directly. The examples cover successful operations, misses, collisions, deletion, queue capacity checks, and graph traversal order. All seven scripts run successfully with Python 3 using the commands above.

## Notes

- The implementations prioritize clarity over production performance.
- Hash-table keys must be integers because the hash functions use the modulo operator.
- `E7DFSBFS.py` executes its traversal demo when imported as well as when run directly; the other experiment demos are protected by `if __name__ == "__main__":`.
- No license file is currently included. Add a license before publishing if you want to define reuse terms.

## GitHub repository description

**Data Structures & Algorithms experiments in Python: searching, sorting, stacks, queues, hash tables, DFS, and BFS.**

## Suggested GitHub topics

`python` `data-structures` `algorithms` `searching` `sorting` `hash-table` `stack` `queue` `graph-algorithms` `dfs` `bfs` `computer-science`
