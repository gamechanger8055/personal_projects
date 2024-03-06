from cron_parser_service import define_string,handle_lists,handle_range,handle_intervals

import unittest


class TestCronFunctions(unittest.TestCase):

    def test_define_string(self):
        # Test cases for define_string function
        self.assertEqual(define_string("*", 'minute'), "0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59")
        self.assertEqual(define_string("?", 'hour'), "Not Specified")
        # Add more test cases for other scenarios

    def test_handle_lists(self):
        # Test cases for handle_lists function
        self.assertEqual(handle_lists("1,2,3", [1, 2, 3], 'hour'), "1 2 3")
        self.assertEqual(handle_lists("JAN,FEB,MAR", ['JAN', 'FEB', 'MAR'], 'month', sub=['JAN', 'FEB', 'MAR']), "JAN FEB MAR")
        # Add more test cases for other scenarios

    def test_handle_range(self):
        # Test cases for handle_range function
        self.assertEqual(handle_range("5-1", [],'week',[1,2,3,4,5,6,7]), "5 6 7 1 ")
        #self.assertEqual(handle_range("MON-WED", ['MON', 'TUE', 'WED'], 'week'), "MON TUE WED")
        # Add more test cases for other scenarios

    def test_handle_intervals(self):
        # Test cases for handle_intervals function
        self.assertEqual(handle_intervals("*/5", list(range(0, 60)), 'minute'), "0 5 10 15 20 25 30 35 40 45 50 55")
        self.assertEqual(handle_intervals("*/2", list(range(1, 13)), 'month'), "2 4 6 8 10 12")
        # Add more test cases for other scenarios

if __name__ == '__main__':
    unittest.main()
