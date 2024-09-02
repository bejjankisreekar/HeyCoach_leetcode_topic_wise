# Heap in Data Structures
- A heap is a specialized tree-based data structure that satisfies the heap property. 
- There are two main types of heaps: **Max Heap** and **Min Heap**. 
- The heap is used in various applications, including priority queues, graph algorithms, and memory management.

## 1. Heap Property
- Max Heap: In a max heap, the value of each node is greater than or equal to the values of its children. The largest element is at the root of the tree.
- Min Heap: In a min heap, the value of each node is less than or equal to the values of its children. The smallest element is at the root of the tree.
## 2. Structure of a Heap
A heap is a complete binary tree, meaning all levels are fully filled except possibly for the last level, which is filled from left to right.
Complete Binary Tree: A binary tree in which every level, except possibly the last, is completely filled, and all nodes are as far left as possible.
## 3. Operations on a Heap
### Insertion:
- Insert the new element at the end of the tree (as the last node).
- Perform an "up-heap" operation (also known as "heapify up" or "bubble up") to restore the heap property if it's violated.
### Deletion:
- Typically, deletion is performed on the root node (maximum in a max heap, minimum in a min heap).
- Replace the root with the last element in the tree and then remove the last element.
- Perform a "down-heap" operation (also known as "heapify down" or "bubble down") to restore the heap property.
### Heapify:
- A process used to build a heap from an unordered array.
- Two main types: Top-Down Heapify (starts from the root) and Bottom-Up Heapify (starts from the last non-leaf node).
### Peek:
- Retrieves the root element without removing it (max element in a max heap, min element in a min heap).
### Extract:
- Removes and returns the root element of the heap.
## 4. Heap Implementation
- **Array Representation:** Heaps are typically implemented using arrays. The parent-child relationship can be easily calculated using array indices:
  - For a node at index i:
    - Left child is at index 2i + 1.
    - Right child is at index 2i + 2.
    - Parent is at index (i - 1) // 2.
## 5. Types of Heaps
### Binary Heap:
- The most common type of heap, which is a complete binary tree.
- Can be either a max heap or a min heap.
### Binomial Heap:
- A collection of binomial trees, which are used to implement a priority queue.
- Supports faster union operations than binary heaps.
### Fibonacci Heap:
- A collection of trees that are more flexible than binary heaps.
- Has a better amortized running time for decrease key and delete operations, making it efficient for Dijkstra’s and Prim’s algorithms.
### d-ary Heap:
- A generalization of the binary heap, where each node has d children.
- Useful in scenarios where the decrease key operation needs to be fast.

## 6. Heap Applications
- **Priority Queue:** Heaps are often used to implement priority queues, where the highest (or lowest) priority element is always at the front.
- **Heap Sort:**
  - An efficient sorting algorithm that sorts an array in-place.
  - Steps: Build a max heap, and repeatedly extract the maximum element, then heapify the remaining elements.
- **Graph Algorithms:**
  - **Dijkstra’s Algorithm:** Used for finding the shortest path in a graph.
  - **Prim’s Algorithm:** Used for finding the minimum spanning tree of a graph.
- **Median Maintenance:** Heaps are used to maintain the median of a dynamically changing dataset, where a max heap is used for the lower half, and a min heap is used for the upper half.
## 7. Complexity Analysis
- **Insertion: O(log n)** — Inserting an element may require heapify up, which takes O(log n) time.
- **Deletion: O(log n)** — Deleting the root and restoring the heap property with heapify down takes O(log n) time.
- **Peek/Extract: O(1)** — Accessing the root element is O(1) since it's at the top of the heap.
- **Building a Heap: O(n)** — Building a heap from an unsorted array takes linear time due to the efficient bottom-up heapify process.

