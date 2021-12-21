# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 21:38:13 2021

@author: User
"""

class naive:
    """podem fazer posts de mensagens honestas e falsas, e so podem fazer comentarios positivos (os utilizadores estao sempre de 
    acordo com o post que comentam, independentemente do autor do post e da sua honestidade). """
    
    def __init__(self,userkind,userid):
        self.userkind = userkind
        self.userid = userid
        self.friends = []
        self.posts = []
        self.comments = []
        
    def get_userid(self):
        return self.userid
    
    def get_userid(self):
        return self.userid
    
    def register(self):
        return {"userid":self.userid,"userkind":self.userkind, "friends": [], "posts": [], "comments" : []}