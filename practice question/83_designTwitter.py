from collections import OrderedDict
class Twitter:
    def __init__(self):
        self.tweet=OrderedDict()
        self.user=OrderedDict()
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId in self.tweet:
            self.tweet[userId].append(tweetId)
        else:
            self.tweet[userId]=[tweetId]
        

    def getNewsFeed(self, userId: int) -> list[int]:
        return self.tweet[userId]
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.user:
            self.user[followerId].append(followeeId)
        else:
            self.user[followerId]=[followeeId]
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        pass