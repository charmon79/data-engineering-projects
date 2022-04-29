Raw data is taken from the [PokemonDb data repository](https://github.com/pokemondb/database). Clone that repo into the `database` subdirectory within this directory:

```bash
cd ./database
git clone https://github.com/pokemondb/database.git
```

As noted [here](https://github.com/pokemondb/database/pull/1), the YAML files currently have keys which use a dash (`-`) as a word separator, which is an illegal character in Avro. The simplest workaround for this is to replace all dashes (`-`) with underscores (`_`) in the YAML files to ensure Avro compatibility.
