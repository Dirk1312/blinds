from logger.Logger import logger

import time
import RPi.GPIO as gpio


class Shutter:
    """
    Represents a single shutter

    Attributes
    ---------
    _name: str
        A representative name for the shutter, e.g. Badezimmer
    _state: str
        The current state of the shutter. Possible values: OPEN|STOP|CLOSE
    _gpios: dict
        The gpios to control the shutter. Expected keys are 'OPEN', 'STOP', 'CLOSE' and the values are the pins. E.g.
        {
            'OPEN': 3,
            'STOP': 4,
            'CLOSE': 5
        }
    """

    BUTTON_PRESS_TIME = 0.15

    PIN_OPEN_KEY = 'OPEN'

    PIN_STOP_KEY = 'STOP'

    PIN_CLOSE_KEY = 'CLOSE'

    STATE_OPENED = 'OPENED'

    STATE_STOPPED = 'STOPPED'

    STATE_CLOSED = 'CLOSED'

    _name: str

    _state: str

    _gpios: dict

    def __init__(self, name: str, gpios: dict):
        """
        :param name: str
            The name of the shutter
        :param gpios:
            The pins of the different shutter states
        """
        self._name = name
        self._gpios = gpios

    def open(self):
        """
        Opens the shutter
        :return: void
        """
        pin = self._get_open_pin()
        logger.info('Opening shutter "%s" on pin %d' % (self._name, pin))
        self._change_state(pin, self.STATE_OPENED)
        logger.info('Opened shutter "%s" on pin %d' % (self._name, pin))

    def stop(self):
        """
        Stops the shutter at the current position
        :return: void
        """
        pin = self._get_stop_pin()
        logger.info('Stopping shutter "%s" on pin %d' % (self._name, pin))
        self._change_state(pin, self.STATE_STOPPED)
        logger.info('Stopped shutter "%s" on pin %d' % (self._name, pin))

    def close(self):
        """
        Closes the shutter
        :return: void
        """
        pin = self._get_close_pin()
        logger.info('Closing shutter "%s" on pin %d' % (self._name, pin))
        self._change_state(pin, self.STATE_CLOSED)
        logger.info('Closed shutter "%s" on pin %d' % (self._name, pin))

    def _change_state(self, pin, state: str):
        """
        Resets all pins, changes the pin state to bring the shutter in the expected state and again resets the pins
        :return: void
        """
        logger.info('Changing state for pin %d to %s' %(pin, state))
        self._reset()
        self._change_pin_state(pin, gpio.HIGH)
        time.sleep(self.BUTTON_PRESS_TIME)
        self._reset()
        self._state = state
        logger.info('Changed state for pin %d to %s' %(pin, state))

    @staticmethod
    def _change_pin_state(pin: int, signal: int):
        """
        Sets the given signal HIGH|LOW to the given pin
        :return: void
        """
        gpio.output(pin, signal)

    def _reset(self):
        """
        Resets each of the shutter's assigned gpio pins
        :return: void
        """
        logger.info('Resetting pins for shutter "%s"' % self._name)
        for gpio in self._gpios:
            logger.info('Resetting pin %d for shutter "%s"' % (gpio, self._name))
            self._change_pin_state(gpio, gpio.LOW)
        logger.info('Reset pins for shutter "%s"' % self._name)

    def _get_open_pin(self) -> int:
        """
        Returns the open pin
        :return: int
        """
        return self._gpios.get(self.PIN_OPEN_KEY)

    def _get_stop_pin(self) -> int:
        """
        Returns the stop pin
        :return: int
        """
        return self._gpios.get(self.PIN_STOP_KEY)

    def _get_close_pin(self) -> int:
        """
        Returns the close pin
        :return: int
        """
        return self._gpios.get(self.PIN_CLOSE_KEY)
