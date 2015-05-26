# Naive Bayes classifier as a Bayesian network

import numpy as np
from pomegranate import *

# Passengers on the Titanic either survive or perish
passenger = DiscreteDistribution( { 'survive': 0.5, 'perish': 0.5 } )

# Gender, given survival data
# gender = ConditionalProbabilityTable(
#             [[ 'survive', 'male',   0.0 ],
#              [ 'survive', 'female', 1.0 ],
#              [ 'perish', 'male',    1.0 ],
# 	       [ 'perish', 'female',  0.0]], [passenger] )
gender = ConditionalDiscreteDistribution({
      'survive' : DiscreteDistribution({ 'male' : 0.0, 'female' : 1.0 }),
      'perish' : DiscreteDistribution({ 'male' : 1.0, 'female' : 0.0 })
      }, [passenger])


# Class of travel, given survival data
# tclass = ConditionalProbabilityTable(
#             [[ 'survive', 'first',  0.0 ],
#              [ 'survive', 'second', 1.0 ],
#              [ 'survive', 'third',  0.0 ],
#              [ 'perish', 'first',  1.0 ],
#              [ 'perish', 'second', 0.0 ],
# 	         [ 'perish', 'third',  0.0]], [passenger] )
tclass =  ConditionalDiscreteDistribution({
      'survive' : DiscreteDistribution({ 'first' : 0.0, 'second' : 1.0, 'third' : 0.0 }),
      'perish' : DiscreteDistribution({ 'first' : 1.0, 'second' : 0.0, 'third' : 0.0 })
      })


# State objects hold both the distribution, and a high level name.
s1 = State( passenger, name = "passenger" )
s2 = State( gender, name = "gender" )
s3 = State( tclass, name = "class" )

# Create the Bayesian network object with a useful name
network = BayesianNetwork( "Titanic Disaster" )

# Add the three nodes to the network
network.add_nodes( [ s1, s2, s3 ] )

# Add transitions which represent conditional depesndencies, where the second
# node is conditionally dependent on the first node (Monty is dependent on both guest and prize)
network.add_edge( s1, s2 )
network.add_edge( s1, s3 )
network.bake()

# The first observation is that the interpreter is not working
#first_observation = { 'interpreter' : 'nw' }

# beliefs will be an array of posterior distributions or clamped values for each state, indexed corresponding to the order
# in self.states.
#beliefs = network.forward_backward( first_observation )

# Convert the beliefs into a more readable format
#beliefs = map( str, beliefs )

# Print out the state name and belief for each state on individual lines
# What is the probability of the code being buggy ?
#print "\n".join( "{}\t{}".format( state.name, belief ) for state, belief in zip( network.states, beliefs ) )


# Repeat above steps for second observation
# Now what is the probability of the code being buggy ?
#second_observation = { 'interpreter' : 'nw', 'cursor' : 'w' }
#beliefs = network.forward_backward( second_observation )
#beliefs = map( str, beliefs )
#print "\n".join( "{}\t{}".format( state.name, belief ) for state, belief in zip( network.states, beliefs ) )
