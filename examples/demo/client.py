# -*- coding: utf-8 -*-


from xpin import API

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


username = 'dantezhu'
source = 1
client_secret = '13'
base_url = 'http://127.0.0.1:5000/'

client = API(client_secret, 'http://127.0.0.1:5000/')


pin = client.create_pin(username, source)

print 'pin:', pin

print client.verify_pin(username, source, pin)
