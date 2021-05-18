from client_server import get_params
from server import create_parser, get_socket
import unittest
import argparse


class TestParamsClient(unittest.TestCase):
    def test_get_params(self):
        self.assertEqual(get_params(), ({'ip_adress': 'localhost', 'port': 7777}))

    def test_get_params_with_param_true(self):
        self.assertEqual(get_params('127.0.0.1', 2222), ({'ip_adress': '127.0.0.1', 'port': 2222}))

    def test_get_params_with_param_false(self):
        self.assertEqual(get_params('127.0.0.1', 2222), ({'ip_adress': 'localhost', 'port': 7777}))


class TestParamsServer(unittest.TestCase):
    def test_create_parser(self):
        parser = argparse.ArgumentParser()
        self.assertEqual(type(create_parser()), type(parser))


if __name__ == "__main__":
    unittest.main()
