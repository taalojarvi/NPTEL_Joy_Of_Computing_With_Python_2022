words=[n for n in input().split('#')]
words.sort()
words.reverse()
print('#'.join(words),end="")
