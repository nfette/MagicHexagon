# -*- coding: utf-8 -*-
"""
Created on Sat Dec 27 00:19:51 2014

@author: nfette
"""

from math import factorial
import itertools

rowSum = sum(range(1,20)) * 3 / 15

def subsetsThatAddUp(aSet, aSum):
    results = set()
    aClone = aSet.copy()
    l = list(aSet)
    for i in l:
        if i > aSum:
            aClone.remove(i)
    while len(aClone) > 0:
        aNum = aClone.pop()
        if aNum == aSum:
            results.update(set([frozenset([aNum])]))
        else:
            moreSets = subsetsThatAddUp(aClone, aSum - aNum)
            results.update(i.union(frozenset([aNum])) for i in moreSets)
    return results

#%%
S = set(range(1,20))
for i in range(rowSum + 1):
    print "What adds up to {}?".format(i)
    ss = subsetsThatAddUp(S,i)
    stats = {i:0 for i in range(1,10)}
    print "... the following {} sets:".format(len(ss))
    for s in ss:
        #print s
        stats[len(s)] += 1
    print stats
print

# 30 of these
threeSets = filter(lambda s: len(s) == 3, ss)
# 147 of these
fourSets = set(filter(lambda s: len(s) == 4, ss))
# 238 of these
fiveSets = set(filter(lambda s: len(s) == 5, ss))

print "Those 3-sets adding to 38:"
print threeSets # 30
#print fourSets # 147
#print fiveSets # 238

#%%

print "6-sets of 3-sets:"
print factorial(30) / (factorial(24) * factorial(6))

print "How many of those are consistent at first glance?"
zero = []
for anOrdering in itertools.combinations(threeSets, 6):
    stats = {i:0 for i in range(1,20)}
    for s in anOrdering:
        for m in s:
            stats[m] += 1
    v = stats.values()
    # First test
    if v.count(1) != 6 or v.count(2) != 6:
        continue
    # slightly better test, but does not eliminate graphs with sub-loops
    if all([sum(map(stats.get, aThree)) == 5 for aThree in anOrdering]):
        zero.append(set(anOrdering))
print len(zero)
# There are 2846 of these.

#%%
print "How many of those form complete edge loop?"

def findNextTriple(aSixByThree, allTuples, stats):
    for aThreeSet in aSixByThree:
        for aThreeTuple in itertools.permutations(aThreeSet):
            if aThreeTuple[0] == allTuples[-1][2] and stats[aThreeTuple[2]] == 2:
                return aThreeTuple
    return None

one = []
for aSixByThree in zero:
    # Construct the edge sequence
    stats = {i:0 for i in range(1,20)}
    for aThree in aSixByThree:
        for m in aThree:
            stats[m] += 1
    allTuples = []
    aThree = aSixByThree.pop()
    for aThreeTuple in itertools.permutations(aThree):
        if stats[aThreeTuple[0]] == 2 and stats[aThreeTuple[2]] == 2:
            allTuples.append(aThreeTuple)
            break
    for i in range(5):
        aThreeTuple = findNextTriple(aSixByThree, allTuples, stats)
        if aThreeTuple:
            allTuples.append(aThreeTuple)
            aSixByThree.remove(set(aThreeTuple))
    if len(allTuples) == 6:
        one.append(allTuples)
print len(one)
# There are 2542 possible edge sequences.

#%%
print "Okay, this is manageable. How about a consistent edge loop plus a single 4-tuple?"

def findNextQuad(aFourSet, allTuples, stats):
    result = []
    for aFourTuple in itertools.permutations(aFourSet):
        if aFourTuple[0] == allTuples[0][1] \
            and stats[aFourTuple[1]] == 0 \
            and stats[aFourTuple[2]] == 0 \
            and aFourTuple[3] == allTuples[2][1]:
                result.append(aFourTuple)
    return result
    
two = []
for allTuples in one:
    stats = {i:0 for i in range(1,20)}
    for aThreeTuple in allTuples:
        for m in aThreeTuple:
            stats[m] += 1
    for aFourSet in fourSets:
        for aFourTuple in findNextQuad(aFourSet, allTuples, stats):
            two.append(allTuples + [aFourTuple])
print len(two) # 4244
print "Examples:"
for i in range(4): print two[i]

#%%
print "Add a second single 4-tuple."
def findNextQuad2(aFourSet, allTuples, stats):
    result = []
    for aFourTuple in itertools.permutations(aFourSet):
        if aFourTuple[0] == allTuples[1][1] \
            and aFourTuple[1] == allTuples[6][2] \
            and stats[aFourTuple[2]] == 0 \
            and aFourTuple[3] == allTuples[3][1]:
                result.append(aFourTuple)
    return result
    
three = []
for allTuples in two:
    stats = {i:0 for i in range(1,20)}
    for aTuple in allTuples:
        for m in aTuple:
            stats[m] += 1
    for aFourSet in fourSets:
        for aFourTuple in findNextQuad2(aFourSet, allTuples, stats):
            three.append(allTuples + [aFourTuple])
print len(three) # 1139
print "Examples:"
for i in range(4): print three[i]

#%%
print "Add a third single 4-tuple."
def findNextQuad3(aFourSet, allTuples, stats):
    result = []
    for aFourTuple in itertools.permutations(aFourSet):
        if aFourTuple[0] == allTuples[2][1] \
            and aFourTuple[1] == allTuples[7][2] \
            and stats[aFourTuple[2]] == 0 \
            and aFourTuple[3] == allTuples[4][1]:
                result.append(aFourTuple)
    return result
    
four = []
for allTuples in three:
    stats = {i:0 for i in range(1,20)}
    for aTuple in allTuples:
        for m in aTuple:
            stats[m] += 1
    for aFourSet in fourSets:
        for aFourTuple in findNextQuad3(aFourSet, allTuples, stats):
            four.append(allTuples + [aFourTuple])
print len(four) # 160, it's getting easier!
print "Examples:"
for i in range(4): print four[i]
    
#%%
print "Add a fourth single 4-tuple."
def findNextQuad4(aFourSet, allTuples, stats):
    result = []
    for aFourTuple in itertools.permutations(aFourSet):
        if aFourTuple[0] == allTuples[3][1] \
            and aFourTuple[1] == allTuples[8][2] \
            and stats[aFourTuple[2]] == 0 \
            and aFourTuple[3] == allTuples[5][1]:
                result.append(aFourTuple)
    return result
    
five = []
for allTuples in four:
    stats = {i:0 for i in range(1,20)}
    for aTuple in allTuples:
        for m in aTuple:
            stats[m] += 1
    for aFourSet in fourSets:
        for aFourTuple in findNextQuad4(aFourSet, allTuples, stats):
            five.append(allTuples + [aFourTuple])
print len(five) # , almost done!
print "Examples:"
for i in range(4): print five[i]
    
#%%
print "Add a fifth single 4-tuple."
def findNextQuad5(aFourSet, allTuples, stats):
    result = []
    for aFourTuple in itertools.permutations(aFourSet):
        if aFourTuple[0] == allTuples[4][1] \
            and aFourTuple[1] == allTuples[9][2] \
            and stats[aFourTuple[2]] == 0 \
            and aFourTuple[3] == allTuples[0][1]:
                result.append(aFourTuple)
    return result
    
six = []
for allTuples in five:
    stats = {i:0 for i in range(1,20)}
    for aTuple in allTuples:
        for m in aTuple:
            stats[m] += 1
    for aFourSet in fourSets:
        for aFourTuple in findNextQuad5(aFourSet, allTuples, stats):
            six.append(allTuples + [aFourTuple])
print len(six) # , almost done!
print "Examples:"
for i in range(min(4,len(six))): print six[i]
    
#%% The thing is completely determined at this point, so print it pretty
for allTuples in six:
    stats = {i:0 for i in range(1,20)}
    for aTuple in allTuples:
        for m in aTuple:
            stats[m] += 1
    center = [m for m in stats if stats[m] == 0][0]
sequence = () + allTuples[0][0:2] + allTuples[1][0:2] + allTuples[2][0:2] \
    + allTuples[3][0:2] + allTuples[4][0:2] + allTuples[5][0:2] \
    + allTuples[6][1:2] + allTuples[7][1:2] + allTuples[8][1:2] \
    + allTuples[9][1:2] + allTuples[10][1:3] + (center,)
print sequence

print """
    {8:^2}  {7:^2}  {6:^2}
  {9:^2}  {15:^2}  {14:^2}  {5:^2}
{10:^2}  {16:^2}  {18:^2}  {13:^2}  {4:^2}
  {11:^2}  {17:^2}  {12:^2}  {3:^2}
    {0:^2}  {1:^2}  {2:^2}
""".format(*sequence)
