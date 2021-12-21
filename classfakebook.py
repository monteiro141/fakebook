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
        first_userid in self.friends1 and second_userid in self.friends2
    
    def add_friend(self,first_userid,second_userid):
        #self.friends[friend.get_userid()] = friend
        if not self.has_friend(first_userid,second_userid):
            self.friends1.append(second_userid)
            self.friends2.append(first_userid)
            
            
    def friendsprint (self):
        return self.friends1
            
    def post(self,userid,sequence_of_hashtags,truthfulness,message):
        sequence_of_hashtags = []
        
    def userposts(self):
        lista = []
        
        
            
        