# What is Sauron?
Sauron is the 'all seeing eye' that knows all and sees all. In this case, he doesn't really. If you want to track data in a distributed network you need a way to track that network's activities. The easiest way to do this is publishing to a aggregator object.

That is Sauron. Sauron is a bit of a misnomer, since the app is completely _blind_ and relies and nodes to report to him.

# Usage
```python
from sauron import AllSeeingEye

the_eye = AllSeeingEye(config={'url': 'http://some_url'})

# in the method we want to publish...
def some_route():
  # ...
  the_eye.see(some_json)
  return some_json
