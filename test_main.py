import unittest.main
from unittest import TestCase
from unittest.mock import Mock

import main

import pytest

from main import (
    ConnectionDatabaseError,
    TestDbError,
    connect_to_db,
    add,
    get_users_list_from_db,
)


class MockDB:
    def get_user(self):
        return [{"username": "name", "birthday": "18/04/96", "role": "tester"}] * 20




class TestMain(TestCase):
    def test_ConnectionDatabaseError(self):
        assert issubclass(ConnectionDatabaseError, Exception)

    def test_TestDbError(self):
        assert issubclass(TestDbError, Exception)

    def test_connect_to_db(self):
        with self.assertRaises(TestDbError):
            connect_to_db("test")
        with self.assertRaises(ConnectionDatabaseError):
            connect_to_db("nottest")

    @staticmethod
    @pytest.fixture
    def input_connection_string():
        return "test"

    def test_get_users_list_from_db(self):
        main.connect_to_db = Mock(return_value=MockDB())
        for dict_user in get_users_list_from_db(self.input_connection_string):
            dict_template = {"username": None, "birthday": None, "role": None}
            assert dict_user.keys() == dict_template.keys()
            for k, v in dict_template.items():
                self.assertIsNotNone(dict_user[k])

    @pytest.mark.parametrize("x", tuple(range(201)))
    @pytest.mark.parametrize("y", tuple(range(201)))
    @pytest.mark.parametrize("z", tuple(range(201)))
    @staticmethod
    def test_add(x, y, z):
        assert add(x, y, z) == x + y + z


if __name__ == "__main__":
    unittest.main()
