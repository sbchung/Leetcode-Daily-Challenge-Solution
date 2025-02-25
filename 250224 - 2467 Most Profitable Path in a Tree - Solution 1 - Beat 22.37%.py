# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 17:29:03 2025

@author: KC Cheuk

2467 Most Profitable Path in a Tree

There is an undirected tree with n nodes labeled from 0 to n - 1, rooted at node
 0. You are given a 2D integer array edges of length n - 1 where edges[i] = 
 [ai, bi] indicates that there is an edge between nodes ai and bi in the tree.

At every node i, there is a gate. You are also given an array of even integers 
amount, where amount[i] represents:

the price needed to open the gate at node i, if amount[i] is negative, or,
the cash reward obtained on opening the gate at node i, otherwise.
The game goes on as follows:

Initially, Alice is at node 0 and Bob is at node bob.
At every second, Alice and Bob each move to an adjacent node. Alice moves towards
 some leaf node, while Bob moves towards node 0.
For every node along their path, Alice and Bob either spend money to open the 
gate at that node, or accept the reward. Note that:
If the gate is already open, no price will be required, nor will there be any 
cash reward.
If Alice and Bob reach the node simultaneously, they share the price/reward for
 opening the gate there. In other words, if the price to open the gate is c, 
 then both Alice and Bob pay c / 2 each. Similarly, if the reward at the gate 
 is c, both of them receive c / 2 each.
If Alice reaches a leaf node, she stops moving. Similarly, if Bob reaches node 
0, he stops moving. Note that these events are independent of each other.
Return the maximum net income Alice can have if she travels towards the optimal 
leaf node.
"""

"""
                    *** THIS SOLUTION BEATS 22.37% ****
        //Running time = 0 ms
        
        The idea is to create a dict (self.dict) to store what node can go from 
        the current node. I am hoping to use query in dictionary (O(1)) to save 
        time. But this approach will introduce looping problem. 
        i.e. if 1 connect 2, self.dict[1] = [2] and 
        self.dict[2] = [1]. require additional checking to prevent looping.
        
        use BFS for bob and alice:
        
        
        This solution is not ideal, beats 22.37% only.
        
        Improvement:
        1. May implement 2D array for path lookup
        2. update self.dict so that it contain child only
"""

class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        self.path = dict()
        self.bob_path = []           # Find Bob's Shortest Path to Node 0
        self.bob_dic = dict()
        
        # Convert given "edges" into dictionary
        for x, y in edges:
            for i in range(2):
                if x in self.path:
                    self.path[x].append(y)
                else:
                    self.path[x] = [y]
                x, y = y, x

        prev = {bob : None}
        queue = deque( [bob] )
        #mmin_step = math.inf
        while queue:
            curr_node = queue.popleft()
            # if leaf
            #if len(self.path[curr_node])==1 and self.path[curr_node][0] in visited:
            if curr_node ==  0:# and step<mmin_step:
                break
            else:
                for x in self.path[curr_node]:
                    if x not in prev:
                        prev[x] = curr_node
                        queue.append(x)
        
        node = 0
        while node is not None:
            self.bob_path.append(node)
            node = prev[node]
        self.bob_path.reverse()
        
        # Convert self.bob_path to dictionary for faster lookup
        self.bob_dic={x:i for i, x in enumerate(self.bob_path)}
            

        # DFS non-recursive
        mmax = -math.inf
        parent = {0:None}
        curr_sum = amount[0]
        step = 0
        queue = deque( [(0, curr_sum, step)] )
        
        while queue:
            curr_node, curr_sum, step = queue.popleft()
            
            for next_node in self.path[curr_node]:
                
                
                if len(self.path[curr_node])==1 and curr_node != 0: #leaf node
                    mmax = max(mmax, curr_sum)
                else:
                    if (curr_node, next_node) in parent.items(): # Do not go back
                        continue
                    
                    parent[next_node] = curr_node
                    if next_node not in self.bob_dic:
                        
                        queue.append((next_node, curr_sum+amount[next_node], step+1))
                    else:
                        if step+1<self.bob_dic[next_node]: #Alice visit first
                            extra = amount[next_node]
                        elif step+1 == self.bob_dic[next_node]: #same time
                            extra = amount[next_node]//2
                        else:
                            extra = 0
                        queue.append((next_node, curr_sum+extra, step+1))

        return mmax
