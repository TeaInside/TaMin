import os, unittest
from flask import current_app
from flask_testing import TestCase
from src import app


class TestDevelopmentConfig(TestCase):
    def create_app(self):
        app.config.from_object("config.application.DevelopmentConfig")
        return app

    def test_app_is_development(self):
        self.assertTrue(app.config["SECRET_KEY"] == "development_key")
        self.assertFalse(current_app is None)
        self.assertTrue(app.config["DEBUG"])


class TestTestingConfig(TestCase):
    def create_app(self):
        app.config.from_object("config.application.TestingConfig")
        return app

    def test_app_is_testing(self):
        self.assertTrue(app.config["SECRET_KEY"] == "testing_key")
        self.assertTrue(app.config["TESTING"])
        self.assertFalse(app.config["PRESERVE_CONTEXT_ON_EXCEPTION"])


class TestProductionConfig(TestCase):
    def create_app(self):
        app.config.from_object("config.application.ProductionConfig")
        return app

    def test_app_is_production(self):
        self.assertFalse(app.config["TESTING"])
        self.assertFalse(app.config["DEBUG"])
        self.assertTrue(app.config["ENV"] == "production")


if __name__ == "__main__":
    unittest.main()
