# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
# 

def deleteNode(node):
	node.val = node.next.val
	node.next = node.next.next
	#return nothing, delete in place 