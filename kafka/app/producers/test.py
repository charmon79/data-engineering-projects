from classes.pokemon import Pokemon

p = Pokemon()
print(p.get_random())

pokemon = p.generator()
for p in pokemon:
    print(p)
