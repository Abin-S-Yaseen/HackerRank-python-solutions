# Given the participants' score sheet for your University Sports Day, 
# you are required to find the runner-up score.
# You are given n scores.
# Store them in a list and find the score of the runner-up.

if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
arr.sort()
for i in range(1,n):
    if arr[-i] != arr[-i-1]:
        print(arr[-i-1])
        break