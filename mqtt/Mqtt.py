from config.handler.MqttConfig import MqttConfig
from logger.Logger import logger

import paho.mqtt.client as mqtt
import json


class Mqtt:
    BROKER_ADDRESS = 'house.lan'
    MQTT_COMMAND_TOPIC = 'house/shutters'
    MQTT_SHUTTER_STATE_TOPIC = 'house/shutters/shutter-{}-state'

    _client: mqtt.Client

    _config: MqttConfig

    def __init__(self, config: MqttConfig):
        logger.info('Initializing shutter mqtt client')
        self._config = config
        self._client = mqtt.Client('shutter')
        self._client.username_pw_set('shutter', 'HcGsEUvJ1zdCAmwLUjNV')
        self._client.on_connect = self._on_connect
        logger.info('Connected to mqtt broker and topic %s' % self.MQTT_COMMAND_TOPIC)
        self._client.on_message = self._on_message
        self._client.connect(self.BROKER_ADDRESS)
        print('Successfully connected 1')
        self._client.loop_forever()
        print('Successfully connected')

    def destruct(self):
        self._client.loop_stop()
        self._client.unsubscribe(self.MQTT_COMMAND_TOPIC)
        self._client.disconnect()
        # gpio.cleanup()  # this ensures a clean exit
        logger.info('Finishing irrigation script')

    def _on_connect(self, client, userdata, flags, rc):
        logger.info('Connecting to mqtt broker topic %s' % self.MQTT_COMMAND_TOPIC)
        client.subscribe(self.MQTT_COMMAND_TOPIC, 0)
        logger.info('Connected to mqtt broker topic %s' % self.MQTT_COMMAND_TOPIC)

    def _on_message(self, client, userdata, message):
        logger.info('Message received %s' % message)
        msg = str(message.payload.decode("utf-8"))
        command = json.loads(msg)
        logger.info('Received command %s from broker' % command)
        # ON = Open  |  OFF = Close
        # if 'ON' == command['state']:
        #     open(command['pin'])
        #     publishShutterState(client, command['shutter'], 'ON')
        # elif 'OFF' == command['state']:
        #     close(command['pin'])
        #     self._publish_shutter_state(client, command['shutter'], 'OFF')
        logger.info('Message handling ended')

    @staticmethod
    def _publish_shutter_state(self, client, shutter, state):
        logger.info('Publishing status %s for shutter %s' % (state, shutter))
        mqtt_shutter_state_topic = self._create_mqtt_shutter_state_topic(shutter)
        logger.info('Publishing shutter state %s to topic %s' % (state, mqtt_shutter_state_topic))
        client.publish(mqtt_shutter_state_topic, state)
        logger.info('Published Status')

    @staticmethod
    def _create_mqtt_shutter_state_topic(self, shutter):
        return self.MQTT_SHUTTER_STATE_TOPIC.format(shutter)
