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

        followees = self.usersFollowees[userId]
        all_targets = followees | {userId}
        for f in all_targets:
            ftweets = self.usersTweets[f][-10:]
            for tweet in ftweets:
                heapq.heappush(recents, tweet)
                while len(recents) > 10: heapq.heappop(recents)
        
        recents.sort(reverse=True)
        return [tweetId for time, tweetId in recents] 
        

    def follow(self, followerId: int, followeeId: int) -> None:
        # push followeeId into follower's list in O(1) time
        self.usersFollowees[followerId].add(followeeId)


    def unfollow(self, followerId: int, followeeId: int) -> None:
        # remove followeeId from follower's list in O(1) time
        self.usersFollowees[followerId].discard(followeeId)
        
