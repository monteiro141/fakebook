# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 21:37:48 2021

@author: User
"""

class Self_centered:
    """podem publicar mensagens honestas e falsas. 
    Porque sao egocentricos, apenas escrevem comentarios positivos nas suas proprias mensagens, e nunca comentam as mensagens 
    de outros utilizadores. """
    
    def __init__(self,userkind,userid):
        self.userkind = userkind
        self.userid = userid
        self.friends = []
        self.posts = []
        self.comments = []
        
    def get_userkind(self):
        return self.userkind
    
    def get_userid(self):
        return self.userid
    
    def register(self):
        return {"userid":self.userid,"userkind":self.userkind, "friends": [], "posts": [], "comments" : []}