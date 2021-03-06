import unittest

from hask3 import __


class TestPython(unittest.TestCase):

    def test_builtins(self):
        from hask3.Python.builtins import callable, cmp, delattr, divmod
        from hask3.Python.builtins import getattr, hasattr, hash  # noqa: F401
        from hask3.Python.builtins import hex, isinstance, issubclass, len, oct  # noqa: F401
        from hask3.Python.builtins import repr, setattr, sorted  # noqa: F401

        class Example:
            a = 1

        self.assertTrue(callable(__+1))
        self.assertEqual(1, cmp(10) % 9)
        self.assertEqual(divmod(5)(2), (2, 1))

        with self.assertRaises(TypeError):
            cmp(1, "a")

        with self.assertRaises(TypeError):
            oct(1.0)
        with self.assertRaises(TypeError):
            hex(1.0)
        with self.assertRaises(TypeError):
            hasattr(list)(len)
        with self.assertRaises(TypeError):
            getattr(list)(len)
        with self.assertRaises(TypeError):
            setattr(list)(len)
        with self.assertRaises(TypeError):
            delattr(list)(len)
