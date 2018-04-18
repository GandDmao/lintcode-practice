"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: a ListNode
    @param val: An integer
    @return: a ListNode
    """
    def removeElements(self, head, val):
        #如果链表为空
        if head is None:
            return None
        #如果第一个node就是我们要删除的值
        while head.val == val:
            head=head.next #删除这个node，即跳向下一个node
            #如果新的node为空，跳出循环
            if (head==None):
                return None
        pre=head
        # 当head的下一个节点不为空
        while pre.next is not None:
            # 当head的下一个节点的值为要删除的值
            if pre.next.val==val:
                # 将head的指针指向下一个node的指针，即删除下一个节点
                pre.next=pre.next.next
            else:
                #指向下一个节点
                pre=pre.next
        return head






if __name__ == "__main__":
    so = Solution()
    print(so.removeElements([1,2,3,3,4,5,3],3))