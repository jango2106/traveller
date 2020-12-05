import unittest

from parameterized import parameterized

from traveller_app.constants.modifiers import CHARACTERISTIC_MODIFIERS
from traveller_app.models.character_personal import Characteristic

modifier_parameterized_list = []
for group in CHARACTERISTIC_MODIFIERS:
    modifier_parameterized_list += [(value, CHARACTERISTIC_MODIFIERS[group]) for value in group]


class MyTestCase(unittest.TestCase):
    def test_level_validator(self):
        self.assertRaises(ValueError, Characteristic, "test", -1)
        self.assertRaises(ValueError, Characteristic, "test", 19)
        self.assertTrue(Characteristic("test", 0))
        self.assertTrue(Characteristic("test", 18))

    @parameterized.expand(modifier_parameterized_list)
    def test_get_modifier_returns_as_expected(self, level, expected_mod):
        self.assertEqual(expected_mod, Characteristic("test", level).get_modifier())


if __name__ == '__main__':
    unittest.main()
