# postTrend-reddit

Reddit bot used to calculate predicted growth for submissions on Reddit.

## Overview/Intended Use

This bot's intended use is to calculate predicted growth for any submission (either comments or posts) on Reddit. Requests are queued by comments in the given format:

> **!trend days:hours:minutes:seconds**

The field elements days, hours, minutes, and seconds represent an arbitrary amount of time in the future where a prediction is requested. It is important to note that these fields must be entered as integer values in order to work. For example, the given command is in a correct format:

> **!trend 6:12:15:0**

When submitted as a comment or reply, any prediction will be six days, twelve hours, and fifteen minutes into the future with respect to the time at which the bot was queued.

## How it works

In order to make predictions, the assumption that growth is proportional to the amount of upvotes at any given time was made. This yields a first order differential equation for exponential growth, which is solved as follows:

![Model for exponential growth](/images/model1.png)

for P represents the amount of upvotes, and dP/dt represents growth. Any submission starts with an initial upvote at time t=0. Using isolation of variables, the given proportionality constant k can be solved directly as follows:

![Finding a particular solution](/images/model2.png)

This function for P can then be used to solve for the amount of predicted upvotes at the requested time. Note that UNIX timestamps were are used in order to make predictions relative to when the bot was queued. Specifically, two UNIX timestamps were used: the period when the target submission was created, and the period when the command was queued. This function is modeled relative to this timeframe, since growth can only occur past the time in which the target submission exists.

## Contributions

Given the limited scope of this project, contributions are currently discouraged. However, if there exists any noteable issues that contradict this bot's intended functionality, please raise a [new issue](https://github.com/NoahT/postTrend-reddit/issues), which will be handled on a case-by-case basis.
