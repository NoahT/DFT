import unittest
import sys
sys.path.append('../modules/')
import command_parser as parser

'''
Test suite for parser.py
'''
class TestParser(unittest.TestCase):
  '''
  Tuple of elements that are in the general
  format of valid time.
  '''
  VALID_TIME = ('0:0:0:0', '  10:42:54:20 ', ' 5 : 4  :3: 2', '6:   9:6   :9')

  '''
  Tuple of elements that are in the general
  format of invalid time.
  '''
  INVALID_TIME = ('0000', ':42:54:20', 'not whitespace 5:4:3:2', '-6:   -9:-6   :-9', '1.1:2.2:3.3:4.4')

  '''
  Tuple of elements that are in the general format of a
  valid command.
  '''
  VALID_COMMANDS = ('!trend 0:0:0:0', '  !trend   7:12:0:0  ', ' !tReNd 10:25:61:61', '  !trend 1 : 2:  3 : 4   ')

  '''
  Tuple of elements that are in the general format of an
  invalid command.
  '''
  INVALID_COMMANDS = ('!trend 1:1:1:1 !trend 1:1:1:1','!tend 1:1:1:1', 'efef43 !trend 1:2:3:4 ', '!trend 100', '!trend -1:-1:-2:-5', '!!trend 0:1:70:10', '!trend10:20:30:40')

  '''
  Tuple of elements containing each component for time
  in a valid command. Uses VALID_COMMANDS tuple for
  parsing.
  '''
  TIME_SPLIT = ((0, 0, 0, 0), (7, 12, 0, 0), (10, 25, 61, 61), (1, 2, 3, 4))

  '''
  Unit test for determining if a given time is
  in the valid format. In general, time is in
  a valid format if it is in the following form:
  %d:%d:%d:%d
  '''
  def test_time_parseable_true(self):
    for case in TestParser.VALID_TIME:
      self.assertEqual(parser.time_parseable(case), True, 'Entry "%s" should pass as valid format for time!' % (case))

  
  '''
  Unit test for determining if a given time is
  in an invalid format. This test is essentially
  the negation of the preceding test, where all
  invalid times should not be in the following form
  %d:%d:%d:%d
  '''
  def test_time_parseable_false(self):
    for case in TestParser.INVALID_TIME:
      self.assertEqual(parser.time_parseable(case), False, 'Entry "%s" should not pass as a valid format for time!' % (case))

  '''
  Unit test for determining if a command is
  in the valid format. In general, a command is
  in a valid format if it follows the following form:
  !trend %d:%d:%d:%d
  '''
  def test_command_parseable_true(self):
    for case in TestParser.VALID_COMMANDS:
      self.assertEqual(parser.command_parseable(case), True, 'Command "%s" should pass as a valid command!' % (case))

  '''
  Unit test for determining if a command is
  in an invalid format. This test is essentially
  the negation of the preceding test, where all
  invalid commands should not be in the following form:
  !trend %d:%d:%d:%d
  '''
  def test_command_parseable_false(self):
    for case in TestParser.INVALID_COMMANDS:
      self.assertEqual(parser.command_parseable(case), False, 'Command "%s" should pass as an invalid command!' % (case))

  '''
  Unit test for determining if a valid command is
  able to parse time components correctly.
  '''
  def test_parse_time_elements(self):
    for case, result in zip(TestParser.VALID_COMMANDS, TestParser.TIME_SPLIT):
      self.assertEqual(parser.parse_time_elements(case), result, 'Command "%s" should parse its time components as "%s"!' % (case, result))



if __name__ == '__main__':
  unittest.main()