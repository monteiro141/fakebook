# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 16:37:47 2021

@author: 61682_62503_62519
"""
from class_fanatic import fanatic
from class_self import Self_centered
from class_naive import naive

class Fakebook:
    def __init__(self):
        self.user = {}
    
    def get_user(self):
        '''
        get_user: -> dict[object]
        Devolve um dicionario com varios objectos das classes self, naive e/ou fanatic
        '''
        return self.user

    def has_user(self,userid):
        '''
        has_user: String -> Boolean
        Devolve true, caso exista o user no dicionario de objectos e falso caso contrário
        '''
        if userid not in self.user.keys():
            return False
        else:
            return True
    
    
    def register(self,userkind,userid):
        if userkind == "selfcentered":
            self.user[userid] = Self_centered(userkind,userid)
            return True
        elif userkind == "naive":
            self.user[userid] = naive(userkind,userid)
            return True
        elif userkind == "fanatic":
            fanaticUser = fanatic(userkind,userid)
            if fanaticUser.class_sequenceOfFanaticisms():
                self.user[userid] = fanaticUser
                return True
        return False
    
    def users(self):
        sorted_user = sorted(self.user.items())
        for key, value in sorted_user:
            value.class_printUser()


    def has_friend(self,first_userid,second_userid):
        return self.user[first_userid].class_has_friend(second_userid)
    
    def add_friend(self,first_userid,second_userid):
        self.user[first_userid].class_add_friend(second_userid)
        self.user[second_userid].class_add_friend(first_userid)
            
    def friends(self,first_userid):
        return self.user[first_userid].class_friends()
            
    def post_hashtags(self,userid, sequence_of_hashtags):
        for i in range(0,len(sequence_of_hashtags)):
            if sequence_of_hashtags[i] in sequence_of_hashtags[i+1:]:
                return False
        return True
    
    def post_honest_fake(self,userid,sequence_of_hashtags,truthfulness):
        return self.user[userid].class_post_honest_fake(userid,sequence_of_hashtags,truthfulness)

    def create_post(self,userid,sequence_of_hashtags,truthfulness,message):
        self.user[userid].class_create_post(userid,sequence_of_hashtags,truthfulness,message)
        
    def number_posts(self,userid):
        return self.user[userid].class_number_posts()

    def comment_fanaticism(self,positiveNegative,comment,userComment, numberOfPost, userPost):
        fanatic = self.user[userPost].posts[numberOfPost-1]['truthfulness']
        sequence_of_hashtags = self.user[userPost].posts[numberOfPost-1]['sequence_of_hashtags']
        return self.user[userComment].class_comment_fanaticism(positiveNegative,comment,userComment, numberOfPost, userPost, fanatic,sequence_of_hashtags,self.user[userPost].posts[numberOfPost-1])

    def add_comment(self,positiveNegative,comment,userComment,userPost,numberOfPost,sequence_of_hashtags):
        self.user[userComment].class_add_comment(positiveNegative,comment,userComment,userPost,numberOfPost,sequence_of_hashtags)
        self.user[userPost].class_add_comment_to_post(positiveNegative,comment,userComment,userPost,numberOfPost,sequence_of_hashtags)
    
    def show_posts(self,userid,postid):
        return self.user[userid].class_show_posts(postid)
        
    def show_comments(self,userid,topic_id):
        return self.user[userid].class_show_comments(topic_id)

    def topic_fanatics(self,fanaticism):
        listFanatics = []
        for userid in self.user:
            if self.user[userid].userkind == "fanatic" and (fanaticism in self.user[userid].sequence_of_fanaticisms_love or fanaticism in self.user[userid].sequence_of_fanaticisms_hate):
                listFanatics.append(userid)
        return listFanatics

    def topic_posts(self,topic_id):
        listUserPost = []
        for userid in self.user:
            posts = self.user[userid].class_topic_posts(topic_id)
            if posts != []:
                for i in posts:
                    listUserPost.append(i)

        finalList = sorted(listUserPost, key = lambda i: (len(i['comments']),i['userid']))
        return finalList 
        
            
        