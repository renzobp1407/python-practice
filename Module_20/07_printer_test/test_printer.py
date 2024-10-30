from printer import Printer, PrinterError
from unittest import TestCase


class TestPrinter(TestCase):
    def setUp(self):
        self.Printer = Printer(pages_per_s=2.0, capacity=300)

    def test_print_within_capacity(self):
        self.Printer.print(25)

    def test_print_outside_capacity(self):
        with self.assertRaises(PrinterError):
            self.Printer.print(301)

    def test_print_exact_capacity(self):
        self.Printer.print(self.Printer._capacity)        

    def test_printer_speed(self):
        pages = 10
        expected = 'Printed 10 pages in 5.00 seconds.'

        result = self.Printer.print(pages)
        self.assertEqual(result, expected)

    def test_speed_always_two_decimals(self):
        fast_printer = Printer(pages_per_s=3.0, capacity=300)
        pages = 11
        expected = 'Printed 11 pages in 3.67 seconds.'

        result = fast_printer.print(pages)
        self.assertEqual(result, expected)

    def test_multiple_print_runs(self):
        self.Printer.print(25)
        self.Printer.print(50)
        self.Printer.print(225)
    
    def test_multiple_runs_end_up_error(self):
        self.Printer.print(25)
        self.Printer.print(50)
        self.Printer.print(225)

        with self.assertRaises(PrinterError):
            self.Printer.print(1)  