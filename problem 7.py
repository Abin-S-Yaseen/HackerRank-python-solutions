# The included code stub will read an integer,n,from STDIN.
# Without using any string methods, try to print the following:
# 1,2,3...n

from __future__ import print_function

if __name__ == '__main__':
    n = int(raw_input())
lst = []
word = ""
for i in range(1,n+1):
    lst.append(i)
for i in lst:
    word = word + str(i)
print(word)