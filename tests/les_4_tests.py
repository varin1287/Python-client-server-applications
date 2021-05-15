from client_server import get_params
import unittest


class TestParamsClient(unittest.TestCase):
    def test_get_params(self):
        self.assertEqual(get_params(), ({'ip_adress': 'localhost', 'port': 7777}))

    def test_get_params_with_param_true(self):
        self.assertEqual(get_params('127.0.0.1', 2222), ({'ip_adress': '127.0.0.1', 'port': 2222}))

    def test_get_params_with_param_false(self):
        self.assertEqual(get_params('127.0.0.1', 2222), ({'ip_adress': 'localhost', 'port': 7777}))


if __name__ == "__main__":
    unittest.main()
