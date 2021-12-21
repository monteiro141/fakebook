# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 16:37:47 2021

@author: User
"""
from class_fanatic import fanatic
from class_self import Self_centered
from class_naive import naive

class Fakebook:
    def __init__(self):
        self.user = {}
    
    def get_user(self):
        return self.user

    def has_user(self,userid):
        #return userid in self.user
        if userid not in self.user.keys():
            return False
        else:
            return True
    
    
    def register(self,userkind,userid):
        if userkind == "selfcentered":
            self.user[userid] = Self_centered(userkind,userid).register()
            return True
        elif userkind == "naive":
            self.user[userid] = naive(userkind,userid).register()
            return True
        elif userkind == "fanatic":
            fanaticUser = fanatic(userkind,userid)
            if fanaticUser.sequenceOfFanaticisms():
                self.user[userid] = fanaticUser.register()
                return True
            else:
                return False
    
    def users(self):
        sorted_user = sorted(self.user.keys())
        for user in sorted_user:
            print(self.user[user]['userid']+ " " + "["+self.user[user]['userkind']+ "] " + str(len(self.user[user]['friends']))+ " "+str(len(self.user[user]['posts'])) + " " + str(len(self.user[user]['comments'])))
    
    def has_friend(self,first_userid,second_userid):
        return second_userid in self.user[first_userid]['friends']
    
    def add_friend(self,first_userid,second_userid):
        self.user[first_userid]['friends'].append(second_userid)
        self.user[second_userid]['friends'].append(first_userid)
            
    def friends(self,first_userid):
        return self.user[first_userid]['friends']        
            
    def post_hashtags(self,userid, sequence_of_hashtags):
        for i in range(0,len(sequence_of_hashtags)):
            if sequence_of_hashtags[i] in sequence_of_hashtags[i+1:]:
                return False
        return True
    
    def post_honest_fake(self,userid,sequence_of_hashtags,truthfulness):
        if self.user[userid]['userkind'] == "fanatic":
            if truthfulness == "honest":
                for i in sequence_of_hashtags:
                    if i in self.user[userid]['sequence_of_fanaticisms_hate']:
                        return False
            if truthfulness == "fake":
                for i in sequence_of_hashtags:
                    if i in self.user[userid]['sequence_of_fanaticisms_love']:
                        return False
        return True

    def create_post(self,userid,sequence_of_hashtags,truthfulness,message):
        sizePosts = len(self.user[userid]['posts']) 
        newPost = {'postid':sizePosts+1,'truthfulness':truthfulness,'message':message,'sequence_of_hashtags':sequence_of_hashtags,'comments':[]}
        self.user[userid]['posts'].append(newPost)
        
    def number_posts(self,userid):
        return self.user[userid]['posts']

    def comment_fanaticism(self,positiveNegative,comment,userComment, numberOfPost, userPost):
        if positiveNegative == 'postive':
            if self.user[userPost]['posts'][numberOfPost-1]['truthfulness'] == 'honest':
                for i in self.user[userComment]['sequence_of_fanaticisms_hate']:
                    word = i[1:]
                    if word in comment:
                        return False
            elif self.user[userPost]['posts'][numberOfPost-1]['truthfulness'] == 'fake':
                for i in self.user[userComment]['sequence_of_fanaticisms_love']:
                    word = i[1:]
                    if word in comment:
                        return False
        elif positiveNegative == 'negative':
            if self.user[userPost]['posts'][numberOfPost-1]['truthfulness'] == 'honest':
                for i in self.user[userComment]['sequence_of_fanaticisms_love']:
                    word = i[1:]
                    if word in comment:
                        return False
            elif self.user[userPost]['posts'][numberOfPost-1]['truthfulness'] == 'fake':
                for i in self.user[userComment]['sequence_of_fanaticisms_hate']:
                    word = i[1:]
                    if word in comment:
                        return False
        return True

    def add_comment(self,positiveNegative,comment,userComment,userPost,numberOfPost):
        newComment =  {'userComment':userComment,'positiveNegative':positiveNegative,'comment':comment}
        self.user[userPost]['posts'][numberOfPost-1]['comments'].append(newComment)
        self.user[userComment]['comments'].append(newComment)
    
        
        
            
        