import sys

a, b = map(int, sys.stdin.readline().split())

pokemon = {}

for i in range(a):
    poke = sys.stdin.readline().strip()
    pokemon[poke] = (i+1)
    pokemon[i+1] = poke

for j in range(b):
    a = sys.stdin.readline().strip()
    try :
        a = int(a)
    except ValueError:
        a = a
    ans = pokemon[a]
    print(ans)