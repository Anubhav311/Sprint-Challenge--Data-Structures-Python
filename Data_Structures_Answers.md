Add your answers to the questions below.

1. What is the runtime complexity of your ring buffer's `append` method?
O(1)

2. What is the space complexity of your ring buffer's `append` function?
O(1)

3. What is the runtime complexity of your ring buffer's `get` method?
O(n), where n is the length of self.storage

4. What is the space complexity of your ring buffer's `get` method?
O(n), where n is number of items (excluding None) in self.storage


5. What is the runtime complexity of the provided code in `names.py`?
O(n * m), we can also say it's On(n^2) since both lists are of same size.

6. What is the space complexity of the provided code in `names.py`?
O(n), because of 'duplicates' list.

7. What is the runtime complexity of your optimized code in `names.py`?
O(n), it's O(2n) but we can drop the constant

8. What is the space complexity of your optimized code in `names.py`?
O(n), it's O(2n) but we can drop the constant