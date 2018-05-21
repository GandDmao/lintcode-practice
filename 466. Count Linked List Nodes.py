"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: the first node of linked list.
    @return: An integer
    """
    def countNodes(self, head):
        count=0
        pre=head
        while pre:
            count+=1
            pre=pre.next
        return count




if __name__ == "__main__":
    so = Solution()
    print(so.countNodes([1, 5, 3]))