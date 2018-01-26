import sys
from collections import Counter

# equalizing array list
n = int(raw_input())
a = map(int, raw_input().split())
cnt = Counter(a)
dup = cnt.most_common(1)[0][0]
count = 0
for i in a:
    if i != dup:
        count += 1
print count
