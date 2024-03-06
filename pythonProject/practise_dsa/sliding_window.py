# max and min sum subarray of size k
arr = [1, 4, 2, 10, 23, 3, 1, 0, 20]
k = 4
i, j = 0, 0
n = len(arr)
sm = 0
mx = 0
while j < n:
    sm += arr[j]
    if (j - i + 1) == k:
        mx = max(sm, mx)
        sm -= arr[i]
        i += 1
    j += 1
print(mx)

# 1st negative in subarray of size k
arr = [12, -1, -7, 8, -15, 30, 16, 28]
k = 3
i, j = 0, 0
l = []
m = []
n = len(arr)
while j < n:
    if arr[j] < 0:
        l.append(arr[j])
    if (j - i + 1) == k:
        if len(l) == 0:
            m.append(0)
        else:
            m.append(l[0])
            if l[0] == arr[i]:
                l.pop(0)
        i += 1
    j += 1
print(m)

# count anagram occurences
st = "forxxorfxdofr"
s = "for"

# maxm of all subarray of size k
arr = [1, 2, 3, 1, 4, 5, 2, 3, 6]
k = 3
i, j = 0, 0
l = []
m = []
n = len(arr)
while j < n:
    while l and arr[j] > l[0]:
        l.pop(0)
    l.append(arr[j])
    if (j - i + 1) == k:
        if len(l) == 0:
            m.append(0)
        else:
            m.append(l[0])
            if l[0] == arr[i]:
                l.pop(0)
        i += 1
    j += 1
print(m)

# largest subarray of sum k
arr = [-5, 8, -14, 2, 4, 12]
k = 5
i, j = 0, 0
n = len(arr)
sm = 0
mx = 0
while j < n:
    print(sm)
    sm += arr[j]
    if sm == k:
        mx = max((j - i + 1), mx)
    elif sm > k:
        while sm > k:
            sm -= arr[i]
            i += 1
    j += 1
print(mx)

# longest substring with k unique characters
a = "aabbcc"
k = 2
mp = {}
n = len(s)
i, j = 0, 0
mx = 0
while j < n:
    if a[j] not in mp:
        mp[a[j]] = 1
    if len(mp) == k:
        mx = max(j - i + 1)
    elif len(mp) > k:
        while len(mp) > k:
            mp[a[i]] -= 1
            if mp[a[i]] == 0:
                del mp[a[i]]
            i += 1
    j += 1
print(mx)

# minimum window substring



