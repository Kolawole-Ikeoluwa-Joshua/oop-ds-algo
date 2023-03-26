'''
Given a doubly linked list and a position. The task is to delete a node from given position in a doubly linked list.

'''


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Solution:
    def deleteNode(self,head, x):

        '''
        Time: O(n)
        Space: O(1)
        '''
        # Code here
        
        if head == None or x <=0:
            return None
            
        
        # traverse to the node at given position
        curr = head
        for i in range(1, x):
            if curr == None:
                return None
            curr = curr.next
        
        # if the node to be deleted is the head node
        if curr == head:
            head = curr.next
            
        # if the node to be deleted is not the head node
        if curr.next != None:
            curr.next.prev = curr.prev
        if curr.prev != None:
            curr.prev.next = curr.next
            
        del curr
