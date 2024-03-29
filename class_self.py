# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 21:37:48 2021

@author: 61682_62503_62519
"""

class Self_centered:
    
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
        newPost = {'postid':sizePosts+1,'userid':userid,'truthfulness':truthfulness,'message':message,'sequence_of_hashtags':sequence_of_hashtags,'comments':[]}
        self.posts.append(newPost)

    def class_number_posts(self):
        return self.posts

    def class_comment_fanaticism(self,positiveNegative,comment,userComment, numberOfPost, userPost, fanatic, sequence_of_hashtags,post):
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