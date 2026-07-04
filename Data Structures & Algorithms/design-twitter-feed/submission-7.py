class Twitter:

    def __init__(self):
        # each userId has a following list
        self.usersFollowees = defaultdict(set) # user : followee set
        self.usersTweets = defaultdict(list) # user : [ [time, tweet] ]
        self.time = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        # check if user is in class hms
        self.usersTweets[userId].append([self.time, tweetId])
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        # O(nlogn), n = number of userId's followees
        # iterate through user's followees tweets and heapify
        recents = []
        maxheap = []

        followees = self.usersFollowees[userId]
        for f in followees | {userId}:
            if self.usersTweets[f]:
                ftweets = self.usersTweets[f]
                idx = len(ftweets) - 1
                time, tweetId = ftweets[idx]
                heapq.heappush_max(maxheap, [time, tweetId, f, idx])
        
        while maxheap and len(recents) < 10:
            time, tweetId, f, idx = heapq.heappop_max(maxheap)
            if idx > 0:
                recTime, recTweet = self.usersTweets[f][idx-1] 
                heapq.heappush_max(maxheap, [recTime, recTweet, f, idx-1])
            recents.append(tweetId)
        
        return recents

    def follow(self, followerId: int, followeeId: int) -> None:
        # push followeeId into follower's list in O(1) time
        self.usersFollowees[followerId].add(followeeId)


    def unfollow(self, followerId: int, followeeId: int) -> None:
        # remove followeeId from follower's list in O(1) time
        self.usersFollowees[followerId].discard(followeeId)
        
