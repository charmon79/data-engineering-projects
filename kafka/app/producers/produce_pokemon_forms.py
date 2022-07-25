from confluent_kafka import avro
from confluent_kafka.avro import AvroProducer
from classes.pokemon import PokemonForm
import config

pokemon = PokemonForm()

value_schema = avro.loads(pokemon.get_value_schema_str())
key_schema = avro.loads(pokemon.get_key_schema_str())

def delivery_report(err, msg):
    """ Called once for each message produced to indicate delivery result.
        Triggered by poll() or flush(). """
    if err is not None:
        print('Message delivery failed: {}'.format(err))
    else:
        print('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))

avroProducer = AvroProducer(
    {
        **config.kafka,
        'on_delivery': delivery_report
    },
    default_key_schema=key_schema,
    default_value_schema=value_schema
)

for key, value in pokemon.generator():
    avroProducer.produce(topic='pokemon_form', key=key, value=value)
    avroProducer.flush()
