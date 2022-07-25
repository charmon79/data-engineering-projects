kafka = {
    # Required connection configs for Kafka producer, consumer, and admin
    'bootstrap.servers': 'pkc-xxxxx.us-east-2.aws.confluent.cloud:9092',
    'security.protocol': 'SASL_SSL',
    'sasl.mechanisms': 'PLAIN',
    'sasl.username': '${username}',
    'sasl.password': '${password}',

    # Best practice for higher availability in librdkafka clients prior to 1.7
    'session.timeout.ms': 45000,

    # Required connection configs for Confluent Cloud Schema Registry
    'schema.registry.url': 'https://${username}:${password}@psrc-qjmzd.us-east-2.aws.confluent.cloud',
}
