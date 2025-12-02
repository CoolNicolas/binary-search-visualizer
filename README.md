---
title: Binary Search Visualizer
emoji: 📚
colorFrom: indigo
colorTo: red
sdk: gradio
sdk_version: 6.0.1
app_file: app.py
pinned: false
license: mit
short_description: A Python-based interactive Binary Search visualizer
link: https://huggingface.co/spaces/NYIKANG/binary-search-visualizer
---

Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference


Binary Search

I chose Binary Search because it is an efficient searching algorithm built on a simple but powerful idea: after sorting the list, every comparison allows us to eliminate half of the remaining elements. This repeated halving makes the algorithm much faster than scanning the list one element at a time.


Decomposition

Input Handling

- The program first needs to read the user’s text input, validate it, and convert it into a list of integers. It must also confirm the target value is a valid integer.

Sorting + Binary Search Logic

- The list is sorted, and the binary search algorithm is executed step by step. This includes updating the left pointer, right pointer, middle index, and determining whether the target has been found.

State Tracking

- The program stores the current search state (left, right, mid, result) so each click of the “Next Step” button can continue the algorithm.

Visualization Rendering

- A separate component generates colored bar graphs representing the list.

- The mid index is highlighted in red.

- The searched zones are colored gray.

- If the target is found, that bar turns green.

GUI Management
The interface handles:

- starting the search

- stepping through the algorithm

- resetting the visualization

- updating messages that explain what each step is doing



Pattern Recognition


- Each step compares the target to the middle element and then eliminates either the left half or the right half of the list. 

- The left and right boundaries move inward using the same logic every iteration. After every update, the midpoint is computed again with the same formula: mid=(L+R)/2

- The pattern continues until either the target is found or the search space becomes empty.

- For the visualization, these patterns repeat as well, each step displays a new mid index, updates colors, and narrows the search range.

Abstraction

The key components that need to be shown for users to understand the logic of the algorithm are: 

- The sorted list

- The current search boundaries (left and right)

- The middle element being inspected

- Whether the target is found (eliminate half of the list when the target is not found while running binary search)

The visualization hides unnecessary technical details such as:

- How Gradio internally stores the state

- Python recursion or loops

- HTML/CSS specifics

- Parsing logic (validate input)

- Error-handling




Algorithm Design


Input
- The user enters a space separated list of integers and a target number in the Gradio interface.

- This list of integers would represent different rectangular bars(the width of each bar is constant, but the height of each bar is set from the input). 

Initialization

- The list is validated, converted to integers, and sorted.

- The left and right pointers are set.

- The initial mid index is computed.

- A starting visualization is generated.

Step-by-Step Execution
- Each time the user clicks Next Step:

- The program compares the middle element with the target.

- If equal, target found.

- If smaller,  search moves right.

- If larger,  search moves left.

- The mid index is recomputed.


Output
The GUI displays:

- The bar chart

- Color coded search progress

- Pointer labels (L, M, R)

- Explanation text describing what happened in that step

- A reset button allows the user to restart with new input at any time.



Testing

While testing my binary search visualizer, I noticed that very large or very small input values caused the bars to grow outside the display area. This happened because the bar height was directly tied to the number’s value. To prevent the layout from breaking, I limited the bar heights to a fixed range so they always fit within the output box.


Steps to Run

1. Enter a list of integers 
2. Enter a target integer
3. Click start
4. Click next step (until you find the target or the search is over)
5. Click restart


Author and Acknowledgment

This project was created by Nicolas Lin to visually demonstrate how the Binary Search algorithm works. All Python logic, including the search steps, pointer movement, and state tracking was written and implemented by the author.

The visual GUI elements, such as the arrows and bar displays shown in Gradio, were created with assistance from ChatGPT, which helped design the HTML/CSS formatting used in the interface.




