# -*- coding: utf-8 -*-


from xpin import API

import config

import logging

LOG_FORMAT = '\n'.join((
    '/' + '-' * 80,
    '[%(levelname)s][%(asctime)s][%(process)d:%(thread)d][%(filename)s:%(lineno)d %(funcName)s]:',
    '%(message)s',
    '-' * 80 + '/',
))

logger = logging.getLogger('xpin')
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter(LOG_FORMAT))
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)



client = API(config.CLIENT_SECRET, 'http://127.0.0.1:5000/')

print client.create_pin('dantezhu', 1)
