from collections import defaultdict
from collections import Counter

if __name__ == '__main__':
    words = defaultdict(list)
    for i,word in enumerate(input() for x in range(int(input()))):
        words[word].append([i+1])

    count = Counter()
    print(len(words.keys()))

    for k in words:
        if len(words[k]) > 1:
            print(len(words[k]),end=' ')
        else:
            count[k] += 1

    for c in count.values(): print(c,end=' ')
