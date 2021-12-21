# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 19:28:14 2021

@author: 61682_62503_62519
"""


from classfakebook import Fakebook

EXIT = "exit"
HELP = "help"
HELP_MSG = """register - registers a new user
users - lists all users
addfriend - adds a new friend
friends - lists the user friends
post - posts a new message
userposts - lists all posts by a user
comment - user comments on a post
readpost - prints detailed info on a post
commentsbyuser - shows all the comments by a user on a given post
topicfanatics - shows a list of fanatic users on a topic
topicposts - shows a list of posts on a given topic
help - shows the available commands
exit - terminates the execution of the program"""
SELF_CENTERED = "selfcentered"
NAIVE = "naive"
FANATICS = "fanatic"
REGISTER = "register"
USERS = "users"
ADDFRIEND = "addfriend"
FRIENDS = "friends"
POST = "post"
USERPOSTS = "userposts"
COMMENT = "comment"
READPOST = "readpost"
BYUSER = "byuser"
TOPICFANATICS = "topicfanatics"
POSTS = "posts"
UNKNOWN = "Unknown command. Type help to see available commands."
BYE = "Bye!"
USER_REGISTERED = "%s registered."
INVALID_FANATICISM = "Invalid fanaticism list!"
USER_EXISTS = "%s already exists!"
INVALID_KIND = "%s is an invalid user kind!"
NO_USERS = "There are no users!"
IS_FRIEND = "%s is friend of %s."
USER_NOT_EXISTS = "%s does not exist!"
SAME_USER = "%s cannot be the same as %s!"
ADMIRE = "%s must really admire %s!"
NO_POSTS = "%s has no posts!"
NO_FRIENDS = "%s has no friends!"
INVALID_HASHTAG = "Invalid hashtags list!"
INADEQUATE_STANCE = "Inadequate stance!"
NO_POST = "%s has no post %s!"
NO_ACCESS = "%s has no access to post %s by %s!"
NO_COMMENT = "%s cannot comment on this post!"
INVALID_STANCE = "Invalid comment stance!"
NO_COMMENTS = "%s\nNo comments!"
NO_FANATICISM = "Oh please, who would be a fanatic of %s"
NO_TOPIC = "Oh please, who would write about %s"
MESSAGE = "%s sent a %s post to %s friends. Post id = %s."
COMMENT_ADDED = "Comment added!"


def next_command():
    user_input = input().split(" ")
    command = user_input[0].lower()
    args = user_input[1:]
    return command, args

def help_io():
    print(HELP_MSG)


def register_io(fakebook,args):
    userkind = args[0]
    userid = " ".join(args[1:])
    if userkind != SELF_CENTERED and userkind != NAIVE and userkind != FANATICS:
        print (INVALID_KIND % (userkind))
    else:
        if not fakebook.has_user(userid):
            if fakebook.register(userkind,userid):
                print(USER_REGISTERED % (userid))
            else:
                print(INVALID_FANATICISM)
        else:
            print(USER_EXISTS % (userid))
    
        
####

def users_io(fakebook):
    if not fakebook.get_user():
        print (NO_USERS)
    else:
        fakebook.users()
            
    
    """sorted()
    print (userid, "[",userkind,"]", friendscount, postscount, commentscount)"""
   
def addfriend_io(fakebook,args):
    first_userid = " ".join(args[0:])
    second_userid = input()
    #ana
    #bob
    if not fakebook.has_user(first_userid):
        print(USER_NOT_EXISTS % (first_userid))
    elif not fakebook.has_user(second_userid):
        print(USER_NOT_EXISTS % (second_userid))
    else:
        if fakebook.has_friend(first_userid,second_userid):
            print(ADMIRE % (first_userid, second_userid))
        elif first_userid == second_userid:
                print(SAME_USER % (first_userid, second_userid))
        else:
            fakebook.add_friend(first_userid,second_userid)
            print(IS_FRIEND % (first_userid, second_userid))



def friends_io(fakebook,args):
    userid = " ".join(args[0:])
    if fakebook.has_user(userid):
        friends = sorted(fakebook.friends(userid))
        if friends == []:
            print(NO_FRIENDS % (userid))
        else:
            print(*friends, sep = ", ", end=".\n")
    else:
        print(USER_NOT_EXISTS % (userid))
    
''' 
PETE loves #red hates #green
post PETE
#red
honest

if hates X cant honest X
if loves Y cant fake Y
'''
def post_io(fakebook,args):
    userid = " ".join(args[0:])
    sequence_of_hashtags = input().split(" ")
    fullmessage = input()
    truthfulness = fullmessage.split(" ")[0]
    message = fullmessage.split(" ")[1:]
    message = " ".join(message)
    if not fakebook.has_user(userid):
        print(USER_NOT_EXISTS % (userid))
    elif sequence_of_hashtags == [] or not fakebook.post_hashtags(userid,sequence_of_hashtags):
        print(INVALID_HASHTAG)
    elif not fakebook.post_honest_fake(userid,sequence_of_hashtags,truthfulness):
        print(INADEQUATE_STANCE)
    else:
        fakebook.create_post(userid,sequence_of_hashtags,truthfulness,message)
        print(MESSAGE % (userid, truthfulness, len(fakebook.friends(userid)), len(fakebook.number_posts(userid))))

    """id userid desconhecido
    print(USER_NOT_EXISTS, userid)
    if list de hastags vazia ou alguma hastag repetida
    print(INVALID_HASHTAG)
    ..
    print(INADEQUATE_STANCE)"""
    pass
    
def userposts_io(fakebook,args):
    userid = " ".join(args[0:])
    if not fakebook.has_user(userid):
        print(USER_NOT_EXISTS % (userid))
    else:
        posts = fakebook.number_posts(userid)
        if posts == []:
            print(NO_POSTS % (userid))
        else:
            print('\n'.join("{}. [{}] {}. [{} comments]".format(post['postid'],post['truthfulness'],post['message'],len(post['comments'])) for post in posts))
    """if userid no posts print(NO_POSTS, userid)"""
    
def comment_io(fakebook,args):
    userComment = " ".join(args[0:])
    userPost = input()
    fullmessage = input()
    numberOfPost = int(fullmessage.split(" ")[0])
    positiveNegative = fullmessage.split(" ")[1]
    comment = fullmessage.split(" ")[2:]
    comment = " ".join(comment)
    #userid1,userid2,commentid,stance,comment1
    if not fakebook.has_user(userComment):
        print(USER_NOT_EXISTS % (userComment))
    elif not fakebook.has_user(userPost):
        print(USER_NOT_EXISTS % (userPost))
    elif numberOfPost > len(fakebook.number_posts(userPost)):
        print(NO_POST %  (userPost, numberOfPost))
    elif not fakebook.has_friend(userComment,userPost):
        print(NO_ACCESS % (userComment, numberOfPost, userPost))
    else:
        if fakebook.get_user()[userComment].userkind == "selfcentered" and userPost != userComment:
            print(NO_COMMENT % (userComment))
        elif fakebook.get_user()[userComment].userkind == 'fanatic' and not fakebook.comment_fanaticism(positiveNegative,comment,userComment, numberOfPost, userPost):
            print(INVALID_STANCE)
        else:
            fakebook.add_comment(positiveNegative,comment,userComment,userPost,numberOfPost)
            print(COMMENT_ADDED)



    
    """if userid1 or userid2 desconhecido
    print(USER_NOT_EXISTS, userid)
    if nenhum existir
    print (USER_NOT_EXISTS, userid1)
    if id nao existe para esse autor
    print(NO_POST, userid, commentid)
    if userid1 not friend userid2
    print(NO_ACCESS, userid1, commentid userid2)
    if userid1 tiver acesso à postagem, mas não tiver permissão para comentar nela (por exemplo, porque ele é egocêntrico)
    print(NO_COMMENT, userid1)
    if stance invalido para userid
    print(INVALID_STANCE)"""

def readpost_io(fakebook,args):
    userid = " ".join(args[0:])
    postid = int(input())
    if not fakebook.has_user(userid):
        print(USER_NOT_EXISTS % (userid))
    else:
        userpost = fakebook.show_posts(userid,postid)
        post = "{id}. [{truthfulness}] {message}. [{sizeComments} comments]" \
            .format(id = userpost['postid'],truthfulness = userpost['truthfulness'],message = userpost['message'],sizeComments = len(userpost['comments']))
        print(post)
        print('\n'.join("{} [{}] {}." \
            .format(comment['userComment'],comment['positiveNegative'],comment['comment']) for comment in userpost['comments']))
    
    """if userid desconhecido
    print(USER_NOT_EXISTS, userid)
     If userid has no message with the given id 
     print(NO_POST, userid, id)
     if no comments
     print(NO_COMMENTS,message)"""
     
def commentsbyuser_io(fakebook,args):
    userid = args[0]
    #topicid
    if not fakebook.has_user(userid):
        print(USER_NOT_EXISTS % (userid))
    """if userid desconhecido
    print(USER_NOT_EXISTS,userid)
    if userid nao fez comments
    print("No comments!")
    """
    pass
    
def topicfanatics_io(fakebook,args):
    #sorted()
    fanatism_id = args[0]
    """if fanatismid desconhecido
    print(NO_FANATICISM, fanatismid)"""
    pass
    
def topicposts_io(fakebook,args):
    topic_id = args[0]
    """if topicid desconhecido
    print (NO_TOPIC, topicid)"""
    pass

    
    
def main():
    command,args = next_command()
    fakebook = Fakebook()
    while command != EXIT:
        if command == HELP:
            help_io()
        elif command == REGISTER:
            register_io(fakebook,args)
        elif command == USERS:
            users_io(fakebook)
        elif command == ADDFRIEND:
            addfriend_io(fakebook,args)
        elif command == FRIENDS:
            friends_io(fakebook,args)
        elif command == POST:
            post_io(fakebook,args)
        elif command == USERPOSTS:
            userposts_io(fakebook,args)
        elif command == COMMENT:
            comment_io(fakebook,args)
        elif command == READPOST:
            readpost_io(fakebook,args)
        elif command == BYUSER:
            commentsbyuser_io(fakebook,args)
        elif command == TOPICFANATICS:
            topicfanatics_io(fakebook,args)
        elif command == POSTS:
            topicposts_io(fakebook,args)
        else:
            print(UNKNOWN)
        command,args = next_command()
    print(BYE)
    
main()