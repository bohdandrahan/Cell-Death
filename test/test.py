import unittest

import cell
import field

class FieldTestCase(unittest.TestCase):
    def setUp(self):
        self.field = Field(3,3)

    def test_get_width():
        self.assertEqual(self.field.get_width(), 3)

    def test_get_height(self):
        self.assertEqual(self.field.get_height(), 3)

    def test_get_cell(self):
        cell = self.field.get_cell(0,1)
        self.assertIs(type(cell), Cell)
        self.assertEqual(list(cell.get_location()), [0,1])

    def test_get_cells(self):
        self.assertEqual(len(self.field.get_cells()), 9)
        self.assertIs(type(self.field.get_cells()[0]), Cell)

    def test_get_alive_cells(self):
        self.assertEqual(len(self.field.get_alive_cells()), 9)

        self.assertIs(type(self.field.get_alive_cells[0]), Cell)

    def test_get_dead_cells(self):
        self.assertEqual(len(self.field.get_dead_cells()), 0)

        self.field.kill_cell()
        self.assertEqual(len(self.field.get_dead_cells()), 1)
        self.assertIs(type(self.field.get_dead_cells())[0], Cell)

    def test_wipe(self):
        self.field.wipe()
        self.assertEqual(len(self.field.get_alive_cells()), 0)
        self.assertEqual(len(self.field.get_dead_cells()), 9)

    def test_ressurect(self):
        self.field.wipe()
        self.field.ressurect()

        self.assertEqual(len(self.field.get_alive_cells()), 9)
        self.assertEqual(len(self.field.get_dead_cells()), 0)

    def test_kill_cell(self):
        self.field.kill_cell(0,1)
        self.assertFalse(self.field.get_cell(0,1).is_alive())

        self.field.kill_cell()
        self.assertEqual(len(self.field.get_dead_cells()), 2)

        self.field.wipe()
        self.field.kill_cell()
        self.assertEqual(len(self.field.get_dead_cells()), 0)

    def test_restore_cell(self):
        self.field.wipe()
        self.field.restore_cell(0, 1)
        self.assertTrue(self.field.get_cell(0,1).is_alive())

        self.field.restore_cell()
        self.assertEqual(len(self.field.get_alive_cells()), 2)

        self.field.ressurect()
        self.field.restore_cell()
        self.assertEqual(len(self.field.get_dead_cells()),  0)



















