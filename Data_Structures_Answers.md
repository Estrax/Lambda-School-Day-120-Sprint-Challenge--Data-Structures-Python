Add your answers to the questions below.

1. What is the runtime complexity of your ring buffer's `append` method?

It's **O(1)** because each append just overwrites the element of an internal
array stored in a **current** buffer position.

2. What is the space complexity of your ring buffer's `append` function?

It's **O(1)** based on code, or **O(n)** to be more precise, where **n** is the
length of an input. We do not store any additional data, only overwrite the
array at the specific index with the input data. Can be **O(1)** if we assume
that the input has always the fixed size.

3. What is the runtime complexity of your ring buffer's `get` method?

It's **O(1)** when we do not filter out the data. Then we always return the
entire structure, so the pointer to the very beginning of this structure and we
can do it in constant time. With the required filtering of `None` values (e.g.
when we did not insert enough data to make the buffer full), it's **O(n)**.

4. What is the space complexity of your ring buffer's `get` method?

It's **O(1)**. We only return the buffer that is **n**-elements long, no other
allocated memory there.

5. What is the runtime complexity of the provided code in `names.py`?

It's **O(n^2)** as we have two nested for loops.

6. What is the space complexity of the provided code in `names.py`?

It's **O(n)** memory-wise. We store the data in an array.

7. What is the runtime complexity of your optimized code in `names.py`?

It's **O(n)** for the normal task, **O(n log n)** for stretch.

8. What is the space complexity of your optimized code in `names.py`?

It's **O(n)** where `n` is the length of input.
