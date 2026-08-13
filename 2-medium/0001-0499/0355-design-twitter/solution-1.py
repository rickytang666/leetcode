from typing import List
import heapq
from collections import defaultdict

class Twitter:

    def __init__(self):
        self.time = 0
        self.userTweets = defaultdict(list)
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.userTweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        ans = []
        maxHeap = []
        self.following[userId].add(userId)
        for f in self.following[userId]:
            tweets = self.userTweets[f]
            if tweets:
                time, tweetId = tweets[-1]
                idx = len(tweets) - 1
                heapq.heappush(maxHeap, (-time, tweetId, f, idx))
        while maxHeap and len(ans) < 10:
            negTime, tweetId, user, idx = heapq.heappop(maxHeap)
            ans.append(tweetId)
            # push next newest from that user
            if idx - 1 >= 0:
                time, tweetId = self.userTweets[user][idx - 1]
                heapq.heappush(maxHeap, (-time, tweetId, user, idx - 1))
        return ans

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)