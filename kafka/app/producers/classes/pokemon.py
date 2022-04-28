import yaml
import random
from pathlib import Path

data_path = Path(__file__).parent / './database/data/'

class Pokemon:
    def __init__(self):
        with open(f'{data_path}/pokemon.yaml', 'r') as f:
            self.all_pokemon = yaml.safe_load(f)
            print(type(self.all_pokemon))

        # Avro schema as Python dict
        self.key_schema = {
            "type": "record",
            "name": "keySchema",
            "namespace": "trainingwheels",
            "fields" : [
                {
                    "name" : "name",
                    "type" : "string"
                }
            ]
        }

        self.value_schema = {
            "type": "record",
            "name": "valueSchema",
            "namespace": "trainingwheels",
            "fields" : [
                {
                    "name" : "national",
                    "type" : "int"
                },
                {
                    "name" : "name",
                    "type" : "string"
                },
                {
                    "name" : "gen",
                    "type" : "int"
                }
            ]
        }


    def get_random(self):
        """Selects a random Pokemon from the dictionary."""
        self.key = random.choice(list(self.all_pokemon.keys()))
        self.value = self.all_pokemon.get(self.key)
        return self.key, self.value

    def generator(self):
        """Iterable of all Pokemon."""
        for k in self.all_pokemon.keys():
            yield k, self.all_pokemon[k]
