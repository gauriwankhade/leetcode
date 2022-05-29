use start, end and size as pointers.
​
conditions
​
Recursion(start, end, size)
1. when start >= size or end >= size
return
2.  when start >= end:
add start to result
return
​
3. when end - start >= size
add start to result
increament start
end = start + 1
end += 1