#!/usr/bin/env python
# encoding: utf-8
import sys

from sapi import app

host=app.config['HOST']
debug=app.config['DEBUG']
port=app.config['PORT']

app.run(host=host, debug=debug, port=port)
