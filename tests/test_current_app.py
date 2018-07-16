import unittest
from tests.base import BaseTestCase
from flask import current_app
from src import db


class TestCurrentApp(BaseTestCase):
    def test_shell_context(self):
        self.assertFalse(current_app is None)
        self.assertFalse(db is None)
