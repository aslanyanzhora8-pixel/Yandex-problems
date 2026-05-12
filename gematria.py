import sys

barer = [line.rstrip("\n") for line in sys.stdin]
gematria = {}
for bar in barer:
    value = 0
    for tar in bar.upper():
        value += ord(tar) - 65
    gematria[value] = bar
keyer = sorted(list(gematria.keys()))


def sorting(key):
    global gematria
    result = []
    for arjeq in key:
        if key.count(arjeq) == 1:
            result.append(gematria[arjeq])
    for arjek in key:
        if key.count(arjek) > 1:
            i = key.index(arjeq)
            ayb = sorted(result[i:i + key.count(arjeq)])
            del result[i:i + key.count(arjeq)]
            result.insert(i, ayb)
    return result


print(*sorting(keyer), sep="\n")