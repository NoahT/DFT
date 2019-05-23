import math
import time
import command_parser as parser
import conversion

'''
Get the time difference between a given post
and the current UNIX timestamp.
'''
def get_delta(post):
  return int(time.time() - post.created_utc)


'''
Predict the amount of upvotes a given time
into the future. Uses a first-order ordinary
differential equation for exponential growth
of a population.

@param post comment/submission to predict future growth on
@param time UNIX timestamp containing the time at which the bot
was queued
@param future_time UNIX timestamp containing the time at which the
given post's growth should be predicted
'''
def exponential_growth(post, time, future_time):
  k = math.log(post.score) / time
  return round(math.exp(k * future_time))
  # In the case of zero divison error, the command was called
  # at the time of a post's creation, so we let this error bubble up
  # to indicate that not enough information is given for a prediction

'''
Predict the amoutn of upvotes a
given time into the future. The constant
of integration and proportionality constant
are computed based on the given parameter
@param post comment containing the valid command
'''
def calculate_prediction(post):
  if(not parser.command_parseable(post.body)):
    raise ValueError('Given post is not in a valid format!')

  # Parent of comment upon which prediction should be based on
  parent = post.parent()
  # Time when command was queued
  delta = get_delta(parent)
  # Time from delta where prediction should occur
  time_tup = parser.parse_time_elements(post.body)
  future_time = conversion.get_total_seconds(time_tup)
  return exponential_growth(parent, delta, delta + future_time)
