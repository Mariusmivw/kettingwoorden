import json
filename = "OpenTaal-210G-basis-gekeurd.txt"

keyboard = {
    "a": ["q", "w", "s", "z"],
    "b": ["v", "g", "h", "n"],
    "c": ["x", "d", "f", "v"],
    "d": ["e", "r", "f", "c", "x", "s"],
    "e": ["w", "s", "d", "r"],
    "f": ["d", "r", "t", "g", "v", "c"],
    "g": ["f", "t", "y", "h", "b", "v"],
    "h": ["g", "y", "u", "j", "n", "b"],
    "i": ["u", "j", "k", "o"],
    "j": ["h", "u", "i", "k", "m", "n"],
    "k": ["j", "i", "o", "l", "m"],
    "l": ["k", "o", "p"],
    "m": ["n", "j", "k"],
    "n": ["b", "h", "j", "m"],
    "o": ["i", "k", "l", "p"],
    "p": ["o", "l"],
    "q": ["a", "w"],
    "r": ["e", "d", "f", "t"],
    "s": ["a", "w", "e", "d", "x", "z"],
    "t": ["r", "f", "g", "y"],
    "u": ["y", "h", "j", "i"],
    "v": ["c", "f", "g", "b"],
    "w": ["q", "a", "s", "e"],
    "x": ["z", "s", "d", "c"],
    "y": ["t", "g", "h", "u"],
    "z": ["a", "s", "x"]
}

with open(filename) as file:
    woorden = file.readlines()

for i in range(len(woorden)):
    woorden[i] = woorden[i].replace("\n", "")


def thingy(char, str):
    str = str.replace(char, "")
    try:
        adj = keyboard[char]
        for i in range(len(adj)):
            if (adj[i] in str):
                str = thingy(adj[i], str)
    except KeyError:
        return str
    return str


def isChain(str):
    return thingy(str[0], str) == ""


chains = []
for i in range(len(woorden)):
    test = isChain(woorden[i].lower())
    # print(test)
    if (test):
        print(woorden[i])
        chains.append(woorden[i])

# print(chains)
with open("chains.txt", "w+") as f:
    for i in range(len(chains)):
        f.write(chains[i] + "\n")

with open("chains.json", "w+") as f:
    json.dump(chains, f)

w = (len(woorden))
c = (len(chains))

print(str(c/w*100)+"%")
print(c/w)
