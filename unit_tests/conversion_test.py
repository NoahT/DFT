import unittest
import sys
sys.path.append('../modules/')
import command_parser as parser
import conversion


'''
Test suite for conversion.py
'''
class TestConversion(unittest.TestCase):
  '''
  Tuple of elements used for testing conversions to seconds.
  '''
  TIME_TUPLES = ((0, 0, 0, 0), (1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1), (7, 12, 30, 15), (1, 25, 61, 61))

  '''
  Tuple of elements containing the conversion to seconds
  '''
  SECONDS_TOTAL = (0, 86400, 3600, 60, 1, 649815, 180121)

  '''
  Test case used to determine whether tuples are converted
  correctly to the number of seconds
  '''
  def test_get_total_seconds(self):
    for case, result in zip(TestConversion.TIME_TUPLES, TestConversion.SECONDS_TOTAL):
      self.assertEqual(conversion.get_total_seconds(case), result, 'Tuple "%s" should be %d seconds!' % (case, result))

if __name__ == '__main__':
  unittest.main()