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

Okay, the next step is passing requests to Sauron node. I need all the nodes to agree, that the Sauron node is 8999, I've hardcoded this value in the settings file, but I shoudl fetch it from env.

# April 21 2035
Okay, now I have web access to all the nodes, with their own db--just copied the sqlite3 DB into each node instead of using `ADD /app/` alone.

The next step I need to take is from the point of a single node, I need to bootstrap myself into the network.

The first node has some special conditions; there are no other nodes that the tracker will know of. So, I need the first node, to get into the network, it will just hang out--zero peers.

What happens when I add a second node? It knows about the first node, and asks for it's chain.

Okay, need to write the bootstrapping middleware to query Sauron for known nodes. I also need the Sauron service to recognize and add new nodes to the registry. Then Sauron can just be queried via the `/peers` endpoint like any regular node.

1. bootstrap middleware
2. add filtering to the 'requests' endpoint such that it recognizes new processes

Wow! That's amazing, I can just use `network_mode=host` to just use the hsot network. I can also pass that as a flag on the command line.

# April 22
Okay, I need to create a django service. What can I do here?

If I run migrations when I run docker-compose up then I won't get everything I need.

Finally got docker working. I also had an issue where Sauron was infinitely making requests to itself. I should really just have Sauron be a separate app. But anyway. I'll leave it for now.

Now, I'm getting a CSRF cookie issue.

QUESTION: what is CSRF?

# April 23
Alright, got sauron working. Stopped the infinite loop of request where sauron was reporting to itself--should really have it be its own service.

Now. Next I need to work on my request logging. Make sure useful invormation is being passed to Sauron and make it decent looking.
