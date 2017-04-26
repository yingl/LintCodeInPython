# coding: utf-8

class MiniTwitter:

    def __init__(self):
        # initialize your data structure here.
        self.tweets = []
        self.follows = {}

    # @param {int} user_id
    # @param {str} tweet
    # @return {Tweet} a tweet
    def postTweet(self, user_id, tweet_text):
        # Write your code here
        t = Tweet.create(user_id, tweet_text)
        self.tweets.append(t)
        return t

    # @param {int} user_id
    # return {Tweet[]} 10 new feeds recently
    # and sort by timeline
    def getNewsFeed(self, user_id):
        # Write your code here
        cnt = 0
        ret = []
        for i in range(len(self.tweets) - 1, -1, -1):
            # 这里复杂一点，要确定是不是自己或者是follow的用户
            if self.tweets[i].user_id == user_id:
                ret.append(self.tweets[i])
                cnt += 1
            elif user_id in self.follows:
                if self.tweets[i].user_id in self.follows[user_id]:
                    ret.append(self.tweets[i])
                    cnt += 1
            if cnt == 10:
                break
        return ret

    # @param {int} user_id
    # return {Tweet[]} 10 new posts recently
    # and sort by timeline
    def getTimeline(self, user_id):
        # Write your code here
        cnt = 0
        ret = []
        for i in range(len(self.tweets) - 1, -1, -1):
            if self.tweets[i].user_id == user_id:
                ret.append(self.tweets[i])
                cnt += 1
                if cnt == 10:
                    break
        return ret

    # @param {int} from user_id
    # @param {int} to_user_id
    # from user_id follows to_user_id
    def follow(self, from_user_id, to_user_id):
        # Write your code here
        if from_user_id in self.follows:
            if to_user_id not in self.follows[from_user_id]:
                self.follows[from_user_id].append(to_user_id)
        else:
            self.follows[from_user_id] = [to_user_id]

    # @param {int} from user_id
    # @param {int} to_user_id
    # from user_id unfollows to_user_id
    def unfollow(self, from_user_id, to_user_id):
        # Write your code here
        if from_user_id in self.follows:
            if to_user_id in self.follows[from_user_id]:
                self.follows[from_user_id].remove(to_user_id)

# medium: http://lintcode.com/zh-cn/problem/mini-twitter/
