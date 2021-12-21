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

    def class_printUser(self):
        print(self.userid+ " " + "["+self.userkind+ "] " + str(len(self.friends))+ " "+str(len(self.posts)) + " " + str(len(self.comments)))       

    def class_has_friend(self,second_userid):
        return second_userid in self.friends

    def class_add_friend(self,second_userid):
        self.friends.append(second_userid)

    def class_friends(self):
        friends = self.friends
        return friends

    def class_post_honest_fake(self,userid,sequence_of_hashtags,truthfulness):
        return True

    def class_create_post(self,userid,sequence_of_hashtags,truthfulness,message):
        sizePosts = len(self.posts) 
        newPost = {'postid':sizePosts+1,'truthfulness':truthfulness,'message':message,'sequence_of_hashtags':sequence_of_hashtags,'comments':[]}
        self.posts.append(newPost)

    def class_number_posts(self):
        return self.posts

    def class_comment_fanaticism(self,positiveNegative,comment,userComment, numberOfPost, userPost):
        return True
    
    def class_add_comment(self,positiveNegative,comment,userComment,userPost,numberOfPost):
        newComment =  {'userComment':userComment,'positiveNegative':positiveNegative,'comment':comment}
        self.comments.append(newComment)

    def class_add_comment_to_post(self,positiveNegative,comment,userComment,userPost,numberOfPost):
        newComment =  {'userComment':userComment,'positiveNegative':positiveNegative,'comment':comment}
        self.posts[numberOfPost-1]['comments'].append(newComment)

    def class_show_posts(self,postid):
        for i in self.posts:
            if i['postid'] == postid:
                return i
        return None
