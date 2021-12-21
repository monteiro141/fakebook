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
        self.friends1 = []
        self.friends2 = []
    
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
                print("Invalid fanaticism list!")
                return False
                
    def lista_users(self):
        users_registados = []
        sorted_user = sorted(self.user.keys())
        for user in sorted_user:
            users_registados.append(self.user)
        return users_registados
    
    def users(self):
        #for i in lista_users():
            pass
    
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
        
        
            
        