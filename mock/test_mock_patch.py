import requests
import unittest
import mock

class WhereIsPythonError(Exception):
    pass


def is_python_still_a_programming_language():
    try:
        r = requests.get("http://python.org")
    except IOError:
        pass
    else:
        if r.status_code == 200:
            return "python is a programming language" in r.content
    raise WhereIsPythonError("something bad happended")

def get_fake_get(status_code, content):
    m = mock.Mock()
    m.status_code = status_code
    m.content = content
    def fake_get(url):
        return m
    return fake_get

def raise_get(url):
    raise IOError("unable to fetch url %s" % url)

class TestPython(unittest.TestCase):
    @mock.patch('requests.get', get_fake_get(
        200, 'python is a programming language for sure'))
    def test_python_is(self):
        self.assertTrue(is_python_still_a_programming_language())

    @mock.patch('requests.get', get_fake_get(
        200, 'python is no more a programming language'))
    def test_python_is_not(self):
        self.assertFalse(is_python_still_a_programming_language())

    @mock.patch('requests.get', get_fake_get(
        404, 'Whatever'))
    def test_bad_status_code(self):
        self.assertRaises(WhereIsPythonError, is_python_still_a_programming_language)

    @mock.patch('requests.get', raise_get)
    def test_ioerror(self):
        self.assertRaises(WhereIsPythonError, is_python_still_a_programming_language)
