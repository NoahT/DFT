import praw
import exponential as exp
import command_parser as parser

user_agent='Windows10:trendBot:v0.2.0 (by /u/tuxedoman23)'

reddit = praw.Reddit('trendBot', user_agent=user_agent)

subreddit = reddit.subreddit('AskReddit') #testingground4bots

for comment in subreddit.stream.comments(skip_existing=True):
  print(comment.body)
  try:
    prediction = exp.calculate_prediction(comment)
    time_output = parser.parse_time_elements(comment.body)
    comment.reply('Hey there %s, this post titled "%s" contains a predicted %d karma %s days, %s hours, %s minutes, %s seconds into the future.'
      % (comment.author.name, comment.submission.title, prediction, time_output[0], time_output[1], time_output[2], time_output[3]))
    print('Post success!')
  except ZeroDivisionError:
    comment.reply('Hey there %s, it seems that it is too soon to predict where this post will be in the future.' % (comment.author.name))
  except ValueError:
    pass
