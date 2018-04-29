# CrapCoin
This is going to be a toy cryptocurrency and we're going to be cutting some corners. But our goal is to have a network of full nodes that are achieving consensus on the same blockchain.

# Planning
## Iteration -4: Just Walls, No Sand
`watercooler -x bigloads --sauron` should create `x` number of processes that don't do any communication but I'm able to ping an endpoint and see those requests being reported to `Sauron`

## Iteration -3: Basic Sandbox
This iteration should have watercooler set up to spin up X `BigCrap` nodes with a `Sauron` node to watch for debugging purposes.

`watercooler -x bigcrap --sauron`

## Iteration -2: Complete Sandbox with Little Shits
We should have everything but fully automated behavior for the simulation.

Add in the `Boss` and the `BigLoadofShit` nodes.

## Iteration -1: Automated Sandbox Play
The final iteration should have:
1. `watercooler`, a CLI app to spin up and down nodes, have a `Boss` that randomly fires nodes for fault modeling
2. `sauron` a configurable `AllSeeingEye` as a django middleware that forwards all requests to the given `Sauron` message aggregator

The way these would work together is that `watercooler` bootstraps nodes into the network providing a new node with the name of an existing node as well as (optionally) the hostname of a `Sauron` service for the `watercooler` member to report too.

These two tools will help aid in debugging `CrapCoin`.

Each node spun up by `watercooler` is a `CrapCoin` fullnode, also known as a `BigLoad`. Each node stores each block and fully validates new incoming chains.

In opposition there is also the concept of a `BigLoadofShit` node that acts maliciously, stupidly, or randomly to simulate bad actors in the system.

To recap, using watercooler like `watercooler -x bigloads -y shits --sauron --boss --auto` you would spin up:
- X `BigLoad` nodes automatically transferring money
- Y `BigLoadofShit` nodes randomly misbehaving
- 1 `Sauron` node for reporting
- 1 `Boss` process to fire nodes randomly to simulate stop faults
- 1 `watercooler` process that can terminate children processes or bootstrap more nodes into the network

# Peerage and the Network
Nodes added to the network ask the `Sauron` node--assuming the `SAURON_URL` is properly set in the settings.py file--for peers to gossip with.

## Sauron

## Bootstrapping
This 'bootstrapping' is accomplished via a 'BootstrapService' middleware. It listens for requests and does a lookup on the `peers` table, if it is empty, it then requests a configurable amount of peers from the tracker and stores them.

Nodes will fetch the initial chain from each of it's peers via a GET to `/blockchain`. If the chain is valid, and longer than the new node's chain it will store the chain. It will then fetch another nodes chain and follow the fork-choice rule by accepting the longest valid chain.

## Maintaining Peerage
If the number of peers is less than the configured amount it will query it's peers at `/peers` and add them, if it still has too few, it will fallback to the tracker.

This is good practice because if the node cannot establish a connection to one of it's peers after a configurable timeout it will remove that node from the DB.

## Gossip Protocol
The network follows a purely push based, event driven, gossip protocol in that when a new node is created it broadcasts it to all peers by POSTs to `/block`

Other than that, nodes will assume that peers will inform it of changes in the network, since all blocks are single transaction it is in miners best interest to do so. In this sense CrapCoin nodes can be called 'lazy' subscribers and 'eager' publishers.
