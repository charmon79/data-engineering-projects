import yaml
import random
from pathlib import Path
import json

data_path = Path(__file__).parent / './database/data/'


class Base:
    def __init__(self):
        self.data = {}
        self.key_schema = {}
        self.value_schema = {}

    # def _get_data(file_path):
    #     with open(file_path, 'r') as f:
    #         self.data = yaml.safe_load(f)
    #     for k in self.data.keys():
    #         # replace characters that are illegal for Avro
    #         if k.find('-') > 0:
    #             self.data[k.replace('-','_')] = self.data.pop(k)

    def get_random(self):
        """Selects a random datum from the dictionary."""
        self.key = random.choice(list(self.data.keys()))
        self.value = self.data.get(self.key)
        return self.key, self.value


    def generator(self):
        """Iterable of all data, returned in Avro_serializable form."""
        for k in self.data.keys():
            yield {'name': k}, self.data[k]


    def get_key_schema_str(self):
        return json.dumps(self.key_schema)


    def get_value_schema_str(self):
            return json.dumps(self.value_schema)


class Pokemon(Base):
    def __init__(self):
        with open(f'{data_path}/pokemon.yaml', 'r') as f:
            self.data = yaml.safe_load(f)
            print(type(self.data))

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


class PokemonForm(Base):
    def __init__(self):
        with open(f'{data_path}/pokemon-forms.yaml', 'r') as f:
            self.data = yaml.safe_load(f)
            print(type(self.data))

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
                    "name" : "pokemonid",
                    "type" : "string"
                },
                {
                    "name" : "formid",
                    "type" : ["null", "string", "int"]
                },
                {
                    "name" : "formname",
                    "type" : ["null", "string"]
                },
                {
                    "name": "gen",
                    "type": ["null", "int"]
                },
                {
                    "name": "release",
                    "type": ["null", "string"]
                },
                {
                    "name": "type1",
                    "type": ["null", "string"]
                },
                {
                    "name": "type2",
                    "type": ["null", "string"]
                },
                {
                    "name": "stats",
                    "type": {
                        "type": "record",
                        "name": "StatsRecord",
                        "fields": [
                            {"name": "hp", "type": "int"},
                            {"name": "attack", "type": "int"},
                            {"name": "defense", "type": "int"},
                            {"name": "spatk", "type": "int"},
                            {"name": "spdef", "type": "int"},
                            {"name": "speed", "type": "int"}
                        ]
                    }
                },
                {
                    "name": "species",
                    "type": ["null", "string"]
                },
                {
                    "name": "height",
                    "type": ["null", "float"]
                },
                {
                    "name": "weight",
                    "type": ["null", "float"]
                },
                {
                    "name": "gender",
                    "type": ["null", "string", "int"]
                },
                {
                    "name": "catch_rate",
                    "type": ["null", "int"]
                },
                {
                    "name": "base_exp",
                    "type": ["null", "int"]
                },
                {
                    "name": "egg_cycles",
                    "type": ["null", "int"]
                },
                {
                    "name": "friendship",
                    "type": ["null", "int"]
                },
                {
                    "name": "growth_rate",
                    "type": ["null", "string"]
                },
                {
                    "name": "ev_yield",
                    "type": {
                        "type": "record",
                        "name": "EVYieldRecord",
                        "fields": [
                            {"name": "hp", "type": ["null", "int"]},
                            {"name": "attack", "type": ["null", "int"]},
                            {"name": "defense", "type": ["null", "int"]},
                            {"name": "spatk", "type": ["null", "int"]},
                            {"name": "spdef", "type": ["null", "int"]},
                            {"name": "speed", "type": ["null", "int"]}
                        ]
                    }
                }
            ]
        }
