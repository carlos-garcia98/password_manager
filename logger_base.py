import logging as log

log.basicConfig(
    level=log.DEBUG,
    format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s',
    datefmt='%I,%M,%S %p',
    handlers=[
        log.FileHandler('data.log'),
        log.StreamHandler()
    ]
)