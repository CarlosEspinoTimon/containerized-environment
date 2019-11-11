#!/usr/bin/env python
# coding=utf-8

import unittest
import jwt

import pathmagic

from server import create_app, db
from server.models.dish import Dish


class BaseTestClass(unittest.TestCase):
    def setUp(self):
        self.app = create_app('config.Test')
        self.tester_app = self.app.test_client()
        self._ctx = self.app.test_request_context()
        self._ctx.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        db.get_engine(self.app).dispose()
        self._ctx.pop()
