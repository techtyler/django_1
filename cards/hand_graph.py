import collections.set
import card_node
import node_set

class hand_graph(object):
    
    def new():
        _sets = (node_set(), node_set())
        size = 0
        
        
        #card values should be [rank,suit] as ints
    def add(card_values):
        nodes = get_nodes(card_values)
        
        nodes[0].add_edge(nodes[1])
        nodes[1].add_edge(nodes[0])
        
        size += 1
        
    def remove(card_values):
        nodes = get_nodes(card_values)
        
        nodes[0].rm_edge(nodes[1])
        nodes[1].rm_edge(nodes[0])
        
        size -= 1
        
        
        
        #Eventually I will want a function to tell me how far away I am from a flush (returns 0 )
        #to do this, try retreiving all node values, sort them, and return max(0, 5 - highest count)
    def has_flush(self):        
        tmp_size = size
        if tmp_size < 5:
            return False
        #do i need a self.sets below this?
        # will self be able to access _sets?
        for n in _sets[1].nodes():
            if n.count > 4:
                return True #TODO Find the highest rank for this flush
            tmp_size -= n.count
            if tmp_size < 5:
                return False
            
        return False
        

    def has_straight(self):
        if _sets[0].size() < 5:
            return False

        values = sorted([v.id fo v in _sets[0].nodes()]) #Sort this (Ace would be low)
        has_ace =  values[0] == 1
        if has_ace:
            values.add(14) #Add ace to end of this tmp values list
        consec = 1
        last = values[0]
        next_value = last + 1
        size = len(values)
        
        for i in range(1, len(values) - 1):
            last = values[i] #is this necessary?
            if values[i] == next_value:
                consec += 1
                next_value = next_value + 1
            else:
                if consec > 4: #found at least 5 consecutive cards already
                    return last #(return values[i-1])
                elif size - i < 5: #not enough cards to satisfy looking for a straight
                    return False
                consec = 1 # Start over looking for consecutive cards
                next_value = values[i] + 1
                
        
    
    def assess_hand(self):
        #This function will return a numerical value for this hand
        #based on the following rules
        #1) cards are given two decimal places for when kickers are necessary. Ex ace is .13 and two is .01
        #Royal Flush         (9)
        #Straight Flush      (8.(highest rank))
        #4 of a Kind         (7.(rank value)(kicker))
        #Full House          (6.(three)(two))
        #Flush               (5.(highest [.05 to .14]))
        #Straight            (4.())
    
    # make below private
    def get_nodes(rank, suit):
        nodes = []
        for i in [0,1]:
            nodes[i] = _sets[i].find_or_add(card_values[i])
        return nodes
        
        #throw exception if r_node doesn't exist. Thats bad code but sometimes inevitable
        #the above will throw an exception if i can't access first element
        # DON'T THROW if we are still using this as a way to check to see if a node is present
        
        
        
        
        
    