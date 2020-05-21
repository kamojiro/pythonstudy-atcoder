# https://www.slideshare.net/iwiwi/2-12188757
class SelfBalancingBinarySearchTree:
    def __init__(self, value,priority):
        self.value = value
        self.left = None
        self.right = None
        self.size = 1
        self.sum = value
        self.priority = priority

    def getValue(self):
        return self.value
    def getLeftSize(self):
        if self.left == None:
            return 0
        return (self.left).value
    def getRightSize(self):
        if self.right == None:
            return 0
        return (self.right).value
    def getLeftSum(self):
        if self.left == None:
            return 0
        return (self.left).sum
    def getRightSum(self):
        if self.right == None:
            return 0
        return (self.right).sum
    def update(self):
        self.size = self.getLeftSize() + self.getRightSize() + 1
        self.sum = self.getLeftSum() + self.getRightSum() + value
        return self
    def insert(self, k, value, priority):
        if not 


#import sys
#input = sys.stdin.readline
def main():
    x = SelfBalancingBinarySearchTree(3)
    print(x.value)
    
if __name__ == '__main__':
    main()

