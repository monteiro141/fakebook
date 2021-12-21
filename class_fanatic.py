# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 21:39:08 2021

@author: User
"""

class fanatic:
    """tem uma lista de topicos sobre os quais sao fanáticos e so podem fazer posts e comentar
mensagens sobre assuntos sobre os quais sao fanaticos. Estes topicos sao definidos atraves
de hashtags (e.g., 7flatearth, 7cutecat, ...). Um fanatico tem sempre uma posicao em
relacao aos temas(s) sobre os quais e fanatico. Se o fanatico tem uma opiniao positiva sobre
um topico(s), so pode fazer comentarios positivos sobre o mesmo, se o post for honesto, ou
comentarios negativos, se o post for falso. Inversamente, se o fanatico tiver uma posicao negativa
sobre esse topico, so podera fazer comentarios negativos em mensagens honestas e comentarios positivos em mensagens falsas.
"""
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
                if i in self.user[userid]['sequence_of_fanaticisms_hate']:
                    return False
        if truthfulness == "fake":
            for i in sequence_of_hashtags:
                if i in self.user[userid]['sequence_of_fanaticisms_love']:
                    return False
        return True

    def class_create_post(self,userid,sequence_of_hashtags,truthfulness,message):
        sizePosts = len(self.posts) 
        newPost = {'postid':sizePosts+1,'truthfulness':truthfulness,'message':message,'sequence_of_hashtags':sequence_of_hashtags,'comments':[]}
        self.posts.append(newPost)

    def class_number_posts(self):
        return self.posts

    def class_comment_fanaticism(self,positiveNegative,comment,userComment, numberOfPost, userPost):
        if positiveNegative == 'postive':
            if self.posts[numberOfPost-1]['truthfulness'] == 'honest':
                for i in self.sequence_of_fanaticisms_hate:
                    word = i[1:]
                    if word in comment:
                        return False
            elif self.posts[numberOfPost-1]['truthfulness'] == 'fake':
                for i in self.sequence_of_fanaticisms_love:
                    word = i[1:]
                    if word in comment:
                        return False
        elif positiveNegative == 'negative':
            if self.posts[numberOfPost-1]['truthfulness'] == 'honest':
                for i in self.sequence_of_fanaticisms_love:
                    word = i[1:]
                    if word in comment:
                        return False
            elif self.posts[numberOfPost-1]['truthfulness'] == 'fake':
                for i in self.sequence_of_fanaticisms_hate:
                    word = i[1:]
                    if word in comment:
                        return False
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
        