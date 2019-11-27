import unittest
from domain import DataTable

class DataTableTest(unittest.TestCase):
    def setUp(self):
        self.table = DataTable('A')

    def test_add_column(self):
        self.assertEqual(0, len(self.table._columns))

        self.table.add_column('Bid', 'bigint')
        self.assertEqual(1, len(self.table._columns))

        self.table.add_column('Value', 'numeric')
        self.assertEqual(2, len(self.table._columns))

        self.table.add_column('desc', 'varchar')
        self.assertEqual(3, len(self.table._columns))

    def test_add_column_invalid_type(self):
        with self.assertRaises(Exception):
            self.table.add_column('col', 'invalida')
            