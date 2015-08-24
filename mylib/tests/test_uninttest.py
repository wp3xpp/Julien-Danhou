import unittest

try:
    import mylib
except ImportError:
    mylib = None

class TestKey(unittest.TestCase):
    def test_key(self):
        a = ['a', 'b']
        b = ['b']
        self.assertEqual(a, b)

class TestFail(unittest.TestCase):
    def test_range(self):
        for x in range(6):
            if x > 4:
                self.fail("range returned a too big value: %d" % x)
                
class TestSkipped(unittest.TestCase):
    @unittest.skip("Do not run this")
    def test_fail(self):
        self.fail("This should not be run")

    @unittest.skipIf(mylib is None, "mylib is not avalable")
    def test_mylib(self):
        self.assertEqual(mylib.foobar(), 42)

    def test_skip_at_runtime(self):
        if True:
            self.skipTest("Finally I don't want wo tun it")

class TestMe(unittest.TestCase):
    def setUp(self):
        self.list = [1, 2, 3]

    def test_length(self):
        self.list.append(4)
        self.assertEqual(len(self.list), 4)

    def test_has_one(self):
        self.assertEqual(len(self.list), 3)
        self.assertIn(1, self.list)
