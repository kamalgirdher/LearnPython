import re

from collections import Counter

x = Counter(re.findall('\w+',open('input.txt').read().lower()))

print(x.most_common(3))
