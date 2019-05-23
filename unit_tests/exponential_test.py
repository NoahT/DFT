import unittest
import sys
sys.path.append('../modules/')
import exponential as exp
import time

'''
Class used for running unit tests involving posts.
'''
class DummyPost():
  '''
  Constructor invocation used to set a posts' UNIX timestamp,
  score, current time, and future time
  '''
  def __init__(self, created_utc, score, time, future_time):
    self.created_utc = int(created_utc)
    self.score = score
    self.time = time
    self.future_time = future_time

'''
Test suite used for exponential.py
'''
class TestExponential(unittest.TestCase):
  '''
  Tuple of DummyPost objects containing different UNIX
  timestamps, offset with the current time to stay constant.
  '''
  POST_DICT = (DummyPost(time.time(), 1, 0, 120), DummyPost(time.time() - 300, 5, 300, 600), DummyPost(time.time() - 1800, 10, 1800, 2000))

  '''
  Tuple containing the proper difference between the given timestamp and
  time post was submitted.
  '''
  TIME_DELTA_RESULT = (0, 300, 1800)

  '''
  Tuple containing the predicted growth for each dummy post created.
  '''
  FUTURE_GROWTH_RESULT = (-1, 25, 13)

  '''
  Unit test determining whether the difference
  in time is being calculated correctly for different
  posts
  '''
  def test_get_delta(self):
    for case, result in zip(TestExponential.POST_DICT, TestExponential.TIME_DELTA_RESULT):
      self.assertEqual(exp.get_delta(case), result, 'Test case "%s" should have a difference of %d!' % (case, result))

  '''
  Unit test for determining whether calculations for
  predicted growth are correct.
  '''
  def test_exponential_growth(self):
    for case, result in zip(TestExponential.POST_DICT, TestExponential.FUTURE_GROWTH_RESULT):
      self.assertEqual(exp.exponential_growth(case, case.time, case.future_time), result, 'Post "%s" should have a predicted growth of %d!' % (case, result))


if __name__ == '__main__':
  unittest.main()