# The provided code stub reads two integers,a and b,from STDIN.
# Add logic to print two lines.
# The first line should contain the result of integer division,a//b.
# The second line should contain the result of float division,a/b.

from __future__ import division

if __name__ == '__main__':
    a = int(raw_input())
    b = int(raw_input())
print(int(a/b))
print(a/b)
