from config.handler.BaseConfig import BaseConfig


class MqttConfig(BaseConfig):
    FILE_NAME = '../mqtt.ini'

    BROKER_CONFIG_KEY = 'broker'

    BROKER_USERNAME_CONFIG_KEY = 'username'

    BROKER_PASSWORD_CONFIG_KEY = 'password'

    BROKER_HOST_CONFIG_KEY = 'host'

    TOKEN_CONFIG_KEY = 'topic'

    TOKEN_COMMAND_TOPIC_CONFIG_KEY = 'command_topic'

    TOKEN_STATE_TOPIC_CONFIG_KEY = 'state_topic'

    def __init__(self):
        super().__init__()

    def get_broker_config(self) -> dict:
        return self._config[self.BROKER_CONFIG_KEY]

    def get_broker_username_config(self) -> str:
        return self.get_broker_config()[self.BROKER_USERNAME_CONFIG_KEY]

    def get_broker_password_config(self) -> str:
        return self.get_broker_config()[self.BROKER_PASSWORD_CONFIG_KEY]

    def get_broker_host_config(self) -> str:
        return self.get_broker_config()[self.BROKER_HOST_CONFIG_KEY]

    def get_topic_config(self) -> dict:
        return self._config[self.TOKEN_CONFIG_KEY]

    def get_command_topic_config(self) -> str:
        return self.get_topic_config()[self.TOKEN_COMMAND_TOPIC_CONFIG_KEY]

    def get_state_topic_config(self) -> str:
        return self.get_topic_config()[self.TOKEN_STATE_TOPIC_CONFIG_KEY]
