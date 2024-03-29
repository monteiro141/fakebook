# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 21:39:08 2021

@author: 61682_62503_62519
"""

class fanatic:
    
    def __init__(self,userkind,userid):
        self.userkind = userkind
        self.userid = userid
        self.sequence_of_fanaticisms_love = []
        self.sequence_of_fanaticisms_hate = []
        self.friends = []
        self.posts = []
        self.comments = []

    
    def get_userkind(self):
        return self.userkind
    
    def get_userid(self):
        return self.userid

    def class_printUser(self):
        print(self.userid+ " " + "["+self.userkind+ "] " + str(len(self.friends))+ " "+str(len(self.posts)) + " " + str(len(self.comments)))       

    def class_sequenceOfFanaticisms(self):
        sequence = input().split(" ")
        self.sequence_of_fanaticisms_love = []
        self.sequence_of_fanaticisms_hate = []
        for i in sequence:
            if i == "loves":
                previous = "loves"
                continue
            elif i == "hates":
                previous = "hates"
                continue

            if previous == "loves":
                if i not in self.sequence_of_fanaticisms_love:
                    self.sequence_of_fanaticisms_love.append(i)
                else:
                    return False
            else:
                if i not in self.sequence_of_fanaticisms_hate:
                    self.sequence_of_fanaticisms_hate.append(i)
                else:
                    return False        

        for i in self.sequence_of_fanaticisms_love:
            if i in self.sequence_of_fanaticisms_hate:
                return False
        return True

    def class_has_friend(self,second_userid):
        return second_userid in self.friends
    
    def class_add_friend(self,second_userid):
        self.friends.append(second_userid)
    
    def class_friends(self):
        return self.friends 
    
    def class_post_honest_fake(self,userid,sequence_of_hashtags,truthfulness):
        if truthfulness == "honest":
            for i in sequence_of_hashtags:
                if i in self.sequence_of_fanaticisms_hate:
                    return False
        if truthfulness == "fake":
            for i in sequence_of_hashtags:
                if i in self.sequence_of_fanaticisms_love:
                    return False
        return True

    def class_create_post(self,userid,sequence_of_hashtags,truthfulness,message):
        sizePosts = len(self.posts) 
        newPost = {'postid':sizePosts+1,'userid':userid,'truthfulness':truthfulness,'message':message,'sequence_of_hashtags':sequence_of_hashtags,'comments':[]}
        self.posts.append(newPost)

    def class_number_posts(self):
        return self.posts

    def class_comment_fanaticism(self,positiveNegative,comment,userComment, numberOfPost, userPost, fanatic, sequence_of_hashtags,post):
        for hashtag in sequence_of_hashtags:
            if fanatic == 'honest':
                if positiveNegative == 'positive':
                    if hashtag in self.sequence_of_fanaticisms_love:
                        return True
                    elif hashtag in self.sequence_of_fanaticisms_hate:
                        return False   
                elif positiveNegative == 'negative':
                    if hashtag in  self.sequence_of_fanaticisms_love:
                        return False
                    elif hashtag in self.sequence_of_fanaticisms_hate:
                        return True
            elif fanatic == 'fake':
                if positiveNegative == 'positive':
                    if hashtag in self.sequence_of_fanaticisms_love:
                        return False
                    elif hashtag in self.sequence_of_fanaticisms_hate:
                        return True
                elif positiveNegative == 'negative':
                    if hashtag in self.sequence_of_fanaticisms_love:
                        return True
                    elif hashtag in self.sequence_of_fanaticisms_hate:
                        return False
        return True

            

    def class_add_comment(self,positiveNegative,comment,userComment,userPost,numberOfPost,sequence_of_hashtags):
        newComment =  {'userComment':userComment,'userPost':userPost,'numberOfPost':numberOfPost ,'positiveNegative':positiveNegative,'sequence_of_hashtags':sequence_of_hashtags,'comment':comment}
        self.comments.append(newComment)

    def class_add_comment_to_post(self,positiveNegative,comment,userComment,userPost,numberOfPost,sequence_of_hashtags):
        newComment =  {'userComment':userComment,'userPost':userPost,'numberOfPost':numberOfPost ,'positiveNegative':positiveNegative,'sequence_of_hashtags':sequence_of_hashtags,'comment':comment}
        self.posts[numberOfPost-1]['comments'].append(newComment)

    def class_show_posts(self,postid):
        for i in self.posts:
            if i['postid'] == postid:
                return i
        return None
        
    def class_show_comments(self,topic_id):
        comments = []
        for comment in self.comments:
            if topic_id in comment['sequence_of_hashtags']:
                comments.append(comment)
        return comments
    
    def class_topic_posts(self,topic_id):
        listPosts = []
        for post in self.posts:
            if topic_id in post['sequence_of_hashtags']:
                listPosts.append(post)
        return listPosts