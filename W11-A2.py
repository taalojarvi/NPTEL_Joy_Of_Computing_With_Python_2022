## SPDX-License-Identifier: GPL-2.0-only

words=[n for n in input().split('#')]
words.sort()
words.reverse()
print('#'.join(words),end="")
