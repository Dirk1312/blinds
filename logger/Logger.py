import logging

logging.basicConfig(
    filename='shutter.log',
    level=logging.INFO,
    format="[%(asctime)s] %(levelname)s [%(filename)s (line %(lineno)d)]: %(message)s",
    force=True
)
logger = logging.getLogger()
