try:
    from unittest import mock
except ImportError:
    import mock

m = mock.Mock()
m.some_method.return_value = 42
m.some_method()
def print_hello():
    print "hello world"
    return 43
m.some_method.side_effect = print_hello
print m.some_method()
print m.some_method.call_count
