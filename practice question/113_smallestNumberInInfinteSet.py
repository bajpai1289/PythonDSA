class SmallestInfiniteSet:
    def __init__(self):
        # infiniteSet = set()
        self.numberNotInSet=[0]

    def popSmallest(self) -> int:

        self.numberNotInSet.append(self.numberNotInSet[-1]+1)

    def addBack(self, num: int) -> None:
        if num in self.numberNotInSet:
            self.numberNotInSet.remove(num)

        