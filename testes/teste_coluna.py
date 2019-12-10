import unittest
from domain import Column

class ColumnTest(unittest.TestCase):
    def test_validate_bigint(self):
        self.assertTrue(Column.validate('bigint', 100))
        self.assertFalse(Column.validate('bigint', 10.1))
        self.assertFalse(Column.validate('bigint', 'Texto'))

    def test_validate_numeric(self):
        self.assertTrue(Column.validate('numeric', 10.1))
        self.assertTrue(Column.validate('numeric', 100))
        self.assertFalse(Column.validate('numeric', 'Texto'))

    def test_validate_varchar(self):
        self.assertTrue(Column.validate('varchar', 'Texto'))
        self.assertFalse(Column.validate('varchar', 100))
        self.assertFalse(Column.validate('varchar', 10.1))

if __name__ == "__main__":
    unittest.main()
    