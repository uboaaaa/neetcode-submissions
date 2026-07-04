class Twitter:

    def __init__(self):
        # each userId has a following list
        self.usersFollowees = defaultdict(set) # user : followee set
        self.usersTweets = defaultdict(list) # user : [ [time, tweet] ]
        self.time = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        # check if user is in class hms
        if userId not in self.usersFollowees:
            self.usersFollowees[userId] = set()
            self.usersFollowees[userId].add(userId)

        self.usersTweets[userId].append([self.time, tweetId])
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        # O(nlogn), n = number of userId's followees
        # iterate through user's followees tweets and heapify
        recentTweets = []
        if self.usersFollowees[userId]:
            followees = self.usersFollowees[userId]
            for f in followees:
                if self.usersTweets[f]:
                    ftweets = self.usersTweets[f]
                    for tweet in ftweets[-10:]:
                        heapq.heappush(recentTweets, tweet)
                        while len(recentTweets) > 10: heapq.heappop(recentTweets)

        recentTweets.sort(reverse=True)
        return [tweetId for time, tweetId in recentTweets] 
        

    def follow(self, followerId: int, followeeId: int) -> None:
        # push followeeId into follower's list in O(1) time
        self.usersFollowees[followerId].add(followeeId)


    def unfollow(self, followerId: int, followeeId: int) -> None:
        # remove followeeId from follower's list in O(1) time
        if followerId != followeeId:
            self.usersFollowees[followerId].discard(followeeId)
        
