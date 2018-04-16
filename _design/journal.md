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
[ ] test that middleware reports to Sauron on requests
[ ] write out Sauron stub tests
