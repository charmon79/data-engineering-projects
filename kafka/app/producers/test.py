from classes.pokemon import Pokemon
from classes.pokemon import PokemonForm

print('testing Pokemon')
p = Pokemon()
print(p.get_random())

pokemon = p.generator()
for k,v in pokemon:
    print(k)
    print(v)

print('testing PokemonForm')
pf = PokemonForm()
print(pf.get_random())

pokemon_form = pf.generator()
for k,v in pokemon_form:
    print(k)
    print(v)