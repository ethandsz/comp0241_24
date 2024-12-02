import numpy as np
# the goal of this routine is to return the minimum cost dynamic programming
# solution given a set of unary and pairwise costs
def dynamicProgram(unaryCosts, pairwiseCosts):

    # count number of positions (i.e. pixels in the scanline), and nodes at each
    # position (i.e. the number of distinct possible disparities at each position)
    nNodesPerPosition = len(unaryCosts)
    nPosition = len(unaryCosts[0])

    # define minimum cost matrix - each element will eventually contain
    # the minimum cost to reach this node from the left hand side.
    # We will update it as we move from left to right
    minimumCost = np.zeros([nNodesPerPosition, nPosition])

    # define parent matrix - each element will contain the (vertical) index of
    # the node that preceded it on the path.  Since the first column has no
    # parents, we will leave it set to zeros.
    parents = np.zeros([nNodesPerPosition, nPosition], dtype=int)

    # FORWARD PASS

    # TODO:  fill in first column of minimum cost matrix
    minimumCost[:, 0] = unaryCosts[:,0]
    # Now run through each position (column)
    for cPosition in range(1,nPosition):
        # run through each node (element of column)
        for cNode in range(nNodesPerPosition):
            print(f"Processing position {cPosition}")
            # now we find the costs of all paths from the previous column to this node
            possPathCosts = np.zeros(nNodesPerPosition)
            for cPrevNode in range(nNodesPerPosition):
                possPathCosts[cPrevNode] = (
                        minimumCost[cPrevNode, cPosition - 1]  # Cost to reach prev node
                        + pairwiseCosts[cPrevNode, cNode]      # Transition cost
                )
               # print(f'{minimumCost[cPrevNode, cPosition - 1]}: ',possPathCosts)
            # Add the unary cost of the current node
            possPathCosts += unaryCosts[cNode, cPosition]
            print(f"    Path costs: {possPathCosts}")

            # Find the minimum cost path to the current node
            minCost = np.min(possPathCosts)
            minInd = np.argmin(possPathCosts)
            print(f"    Min cost = {minCost}, Index = {minInd}")

            # Update the minimum cost matrix
            minimumCost[cNode, cPosition] = minCost

            # Store the index of the parent node
            parents[cNode, cPosition] = minInd

    #BACKWARD PASS

    #we will now fill in the bestPath vector
    bestPath = np.zeros([nPosition,1])
    
    #TODO  - find the index of the overall minimum cost from the last column and put this

    #into the last entry of best path
    minCost = np.min(minimumCost[:, -1])
    minInd = np.argmin(minimumCost[:, -1])
    bestPath[-1] = minInd
    # TODO - find the parent of the node you just found
    bestParent = minInd

    # Trace back through the parents matrix
    for cPosition in range(nPosition - 2, -1, -1):
      #  print(cPosition + 1)
        bestParent = parents[bestParent, (cPosition + 1)]
        bestPath[cPosition] = bestParent

    # TODO: REMOVE THIS WHEN YOU ARE DONE
  #  bestPath = np.floor(np.random.random(nPosition)*nNodesPerPosition)
    print("MinCost: ", minCost)
    return bestPath


def dynamicProgramVec(unaryCosts, pairwiseCosts):
    
    # same preprocessing code
    
    # count number of positions (i.e. pixels in the scanline), and nodes at each
    # position (i.e. the number of distinct possible disparities at each position)
    nNodesPerPosition = len(unaryCosts)
    nPosition = len(unaryCosts[0])

    # define minimum cost matrix - each element will eventually contain
    # the minimum cost to reach this node from the left hand side.
    # We will update it as we move from left to right
    minimumCost = np.zeros([nNodesPerPosition, nPosition])



    # TODO: fill this function in. (hint use tiling and perform calculations columnwise with matricies)

    # TODO: REMOVE THIS WHEN YOU ARE DONE
    bestPath = np.floor(np.random.random(nPosition)*nNodesPerPosition)

    return bestPath