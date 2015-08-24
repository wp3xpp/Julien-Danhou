import fixtures
import os

class TestEnviron(fixtures.TestWithFixtures):
    def test_environ(self):
        fixture = self.useFixture(fixtures.EnvironmentVariable("foobar", "42"))
        self.assertEqual(os.environ.get("foobar"), "42")


    def test_environ_no_fixture(self):
        self.assertEqual(os.environ.get("foobar"), None)
