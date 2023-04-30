import sys
T = int(sys.stdin.readline())
nums = list(map(int,sys.stdin.readline().split()))
nums.sort()
answer = 0
for idx in range(T):
    temp = nums[:idx] + nums[idx+1:]
    l = 0
    r = len(temp) - 1
    while l < r :
        if nums[idx] == temp[l] + temp[r]:
            answer += 1
            break
        elif nums[idx] > temp[l]+temp[r]:
            l += 1
        else:
            r -= 1

print(answer)