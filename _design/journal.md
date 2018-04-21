# April 15 1500
If I store blocks in a relational Db then I can verify easily using queries via the django ORM.

All my nodes will want to basically mint a new block whenever they create a transaction, then they want to gossip that transaction.

What if I hear about a block but I'm working on a block? I need some kind of retry? Or does that just get lost? I'll circle back on this.

# April 15 1630: Just Walls, No Sand
Worked backwards through design iterations.

Now, should the watercooler cli be first class part of the django project? Or a libary? It's simpler to have as part of the project as a management command perhaps?

What about Sauron? Should my Sauron node just be a monolith? Or should it be it's own project? Okay, it can be it's own project. It seems separate.

Likewaise, maybe the CLI app should also be separate...

For now, probably simplest to just put in the same app as well.

*iteration -4 checklist*
[x] test that middleware reports to Sauron on requests
[x] write out Sauron stub tests

# April 18 857: Just Walls, No Sand
I guess I've deviated from the plan...? I'm trying to get block validation to work. I should probably focus on Watercooler and Sauron though for debuggability

# April 21 0900:

Okay, what do I need for iteration 0? I have a way to spin up nodes. Now I just need a way to connect messages to Sauron.

Moved everything back into a single app. The split didn't really make sense.

Remember, don't try to break things apart until it is necessary.

The flow I want to test is:
1. spin up x nodes reporting to sauron instance, knowing of a tracker node
2. bootstrap from tracker node
2. create transaction, and see it propogate via gossip

Setup the app using docker so now I can spin up many nodes--each with their own DB isntance. `sudo docker-compose run --service-ports web python manage.py runserver 0.0.0.0:8000`
