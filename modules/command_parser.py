import re as regex

'''
Compiled regular expression used to parse time in the following format:

%d:%d:%d:%d

where each formmated command stands for Days:Hours:Minutes:Seconds, respectively.
This represents the amount of time past a given comment's UNIX timestamp. For instance,
suppose the following comment was caught in a stream being tracked:

!trend 7:12:0:0

this would signify to base a given post's prediction seven days, twelve hours, zero minutes, and zero seconds
in the future with respect to the UNIX time at which this comment was submitted.
'''
TIME_PATTERN_BASE = '([\s]*[\d]+[\s]*:){3}[\s]*[\d]+[\s]*'
TIME_PATTERN = '^%s$' % (TIME_PATTERN_BASE)
TIME_PATTERN_BASE_COMPILED = regex.compile(TIME_PATTERN_BASE, regex.IGNORECASE)
TIME_PATTERN_COMPILED = regex.compile(TIME_PATTERN, regex.IGNORECASE)

'''
Compiled regular expression used to find commands in the following format:

!trend %d:%d:%d:%d

where %d is the amount of days, hours, minutes, and seconds (respectively) away during
which our prediction should take place.
'''
COMMAND_PATTERN = '^[\s]*![\s]*trend[\s]+%s$' % (TIME_PATTERN_BASE)
COMMAND_PATTERN_COMPILED = regex.compile(COMMAND_PATTERN, regex.IGNORECASE)

'''
Determine whether the given comment is parseable. This
occurs when the given string follows the regular expression
presented for valid commands.
'''
def command_parseable(str):
  return (COMMAND_PATTERN_COMPILED.match(str) is not None)


'''
Determine whether the given string can be parse
into the amount of time specified. In order to
be in the proper time format, TIME_PATTERN should be matched by the
given string.
@precondition str is the component containing the amount of time to wait
(ran through command_parseable beforehand, or matched by COMMAND_PATTERN)
'''
def time_parseable(str):
  return (TIME_PATTERN_COMPILED.match(str) is not None)


'''
Parse the given command into the amount of time specified.
@precondition str is a command
'''
def parse_time(str):
  if(not command_parseable(str)):
    raise ValueError('Command "%s" is not in the proper format.' % (str))
  
  #Note: I initally tried to use str.replace(), but regular expressions were
  #not working well, so .sub was used instead
  return regex.sub('\s+', '', str)[6:]

'''
Parse the given command into the amount of time specified by
the given command.
@precondition str is a command
'''
def parse_time_elements(str):
  return tuple(int(entry) for entry in parse_time(str).split(':'))

