# What is Sauron?
Sauron is the 'all seeing eye' that knows all and sees all. In this case, he doesn't really. If you want to track data in a distributed network you need a way to track that network's activities. The easiest way to do this is publishing to a aggregator object.

That is Sauron. Sauron is a bit of a misnomer, since the app is completely _blind_ and relies and nodes to report to him.

# Usage
Sauron provides a request/response aggregator for visualizing the communication of your distributed system.

Sauron has two parts:
1. Sauron (the aggregator/visualizer)
2. AllSeeingEye that reports to Sauron

You can start up Sauron just like any other Django project with `python manage.py runserver`.

For reporting, Sauron provides a few easy ways to hook into Django projects. If you're project is something else you will need to report to Sauron yourself.

**Vanilla Reporting**
```python
from fullnode import AllSeeingEye

the_eye = AllSeeingEye(config={'url': 'http://some_url'})

# in the method we want to publish...
def some_route():
  # ...
  the_eye.see(some_json)
  return some_json
```

**Wrap Views with Decorator**
```python
from fullnode import all_seeing_eye

@all_seeing_eye
def some_route():
  #...
  return some_json
```

**Django Middleware**
```python
# with package/app installed...
# settings.py
MIDDLEWARE = [
  # ...
  'sauron.AllSeeingEye'
]
```
