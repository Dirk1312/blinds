from logger.Logger import logger
from shutter.Shutter import Shutter
from config.handler.MqttConfig import MqttConfig
from mqtt.Mqtt import Mqtt


if __name__ == "__main__":
    mqtt = None
    try:
        mqtt = Mqtt(MqttConfig())
        Shutter()
    except KeyboardInterrupt:
        pass
    finally:
        if mqtt:
            mqtt.destruct()

        # gpio.cleanup()  # this ensures a clean exit
        logger.info('Finishing shutter script')
