from unittest import TestCase
from safe.safe_dict import SafeDict


class SafeDictTest(TestCase):

    def test_shoud_return_value_from_wrapped_dict_value(self):

        d = dict(a=1, b=2, c='2323')
        s = SafeDict(d, default=0)

        self.assertEqual(s["a"], d["a"])
        self.assertEqual(s["c"], d["c"])

    def test_should_creaate_value(self):
        s = SafeDict()
        s[3] = 4

        self.assertEqual(4, s[3])


    def test_should_update_value_from_wrapped_dict(self):

        d = dict(a=1, b=2, c='2323')
        s = SafeDict(d, default=0)

        self.assertEqual(1, s["a"])

        s["a"] = 2

        self.assertEqual(2, s["a"])

    def test_should_update_value_from_safe_dict(self):

        s = SafeDict(a=1, default=0)

        s["a"] = 2

        self.assertEqual(2, s["a"])

    def test_should_delete_value_from_wrapped_dict(self):
        s = SafeDict(a=1, default=-1)

        s["a"] = 2
        self.assertEqual(2, s["a"])

        del s["a"]
        self.assertEqual(-1, s["a"])

    def test_should_delete_value_from_safe_dict(self):
        d = dict(a=1)
        s = SafeDict(d, default=-1)

        s["a"] = 2
        self.assertEqual(2, s["a"])

        del s["a"]
        self.assertEqual(-1, s["a"])

