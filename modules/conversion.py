'''
TIME CONSTANTS
'''
DAYS_SECONDS = 86400
HOURS_SECONDS = 3600
MINUTES_SECONDS = 60


'''
Get the total number of seconds into the future with which to base
the predicted outcome.
@preconditon tup is a tuple with 4 elements
'''
def get_total_seconds(tup):
  return sum(e1*e2 for e1,e2 in zip((DAYS_SECONDS, HOURS_SECONDS, MINUTES_SECONDS, 1), tup))
