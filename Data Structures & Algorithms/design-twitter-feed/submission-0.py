class Twitter:

    def __init__(self):
        self.time = 0
        self.personalFeed = defaultdict(list)
        self.followeeOf = defaultdict(set)
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.personalFeed[userId].append([self.time, tweetId])
        self.time += 1
        
        

    def getNewsFeed(self, userId: int) -> List[int]:
        newsList = []
        maxHeap = []
        self.followeeOf[userId].add(userId)
        for followeeId in self.followeeOf[userId]:
            if followeeId in self.personalFeed:
                index = len(self.personalFeed[followeeId]) - 1
                time, tweet = self.personalFeed[followeeId][index]
                maxHeap.append([time, followeeId, index - 1, tweet])
        heapq.heapify_max(maxHeap)
        while maxHeap and len(newsList) < 10:
            time, followeeId, index, tweet = heapq.heappop_max(maxHeap)
            newsList.append(tweet)
            if index >= 0:
                time, nextTweet = self.personalFeed[followeeId][index]
                heapq.heappush_max(maxHeap, [time, followeeId, index - 1, nextTweet])
        return newsList

        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followeeOf[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followeeOf[followerId].discard(followeeId)
        
