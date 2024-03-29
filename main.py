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
BYUSER = "commentsbyuser"
TOPICFANATICS = "topicfanatics"
POSTS = "topicposts"
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
POST_USER = "%s posts:"
INVALID_HASHTAG = "Invalid hashtags list!"
INADEQUATE_STANCE = "Inadequate stance!"
NO_POST = "%s has no post %s!"
NO_ACCESS = "%s has no access to post %s by %s!"
NO_COMMENT = "%s cannot comment on this post!"
INVALID_STANCE = "Invalid comment stance!"
NO_COMMENTS = "No comments!"

NO_FANATICISM = "Oh please, who would be a fanatic of %s?"
NO_TOPIC = "Oh please, who would write about %s?"
MESSAGE = "%s sent a %s post to %s friends. Post id = %s."
COMMENT_ADDED = "Comment added!"


def next_command():
    user_input = input().split(" ")
    command = user_input[0].lower()
    args = user_input[1:]
    return command, args

def help_io():
    #Shows the available commands
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
    

def users_io(fakebook):
    if not fakebook.get_user():
        print (NO_USERS)
    else:
        fakebook.users()
   
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
    
def userposts_io(fakebook,args):
    userid = " ".join(args[0:])
    if not fakebook.has_user(userid):
        print(USER_NOT_EXISTS % (userid))
    else:
        posts = fakebook.number_posts(userid)
        if posts == []:
            print(NO_POSTS % (userid))
        else:
            #print(userid + " posts:")
            print(POST_USER % (userid))
            print('\n'.join("{}. [{}] {} [{} comments]".format(post['postid'],post['truthfulness'],post['message'],len(post['comments'])) for post in posts))
    
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
    elif not fakebook.has_friend(userComment,userPost) and userPost != userComment:
        print(NO_ACCESS % (userComment, numberOfPost, userPost))
    else:
        if fakebook.get_user()[userComment].userkind == SELF_CENTERED and userPost != userComment:
            print(NO_COMMENT % (userComment))
        elif fakebook.get_user()[userComment].userkind == FANATICS and not fakebook.comment_fanaticism(positiveNegative,comment,userComment, numberOfPost, userPost):
            print(INVALID_STANCE)
        else:
            sequence_of_hashtags = fakebook.get_user()[userPost].posts[numberOfPost-1]['sequence_of_hashtags']
            fakebook.add_comment(positiveNegative,comment,userComment,userPost,numberOfPost,sequence_of_hashtags)
            print(COMMENT_ADDED)



def readpost_io(fakebook,args):
    userid = " ".join(args[0:])
    postid = int(input())
    if not fakebook.has_user(userid):
        print(USER_NOT_EXISTS % (userid))
    else:
        userpost = fakebook.show_posts(userid,postid)
        if userpost == None:
            print(NO_POST % (userid, postid))
        else:
            post = "[{id} {truthfulness}] {message}" \
                    .format(id = userid,truthfulness = userpost['truthfulness'],message = userpost['message'])
            print(post)
            if userpost['comments'] == []:
                print(NO_COMMENTS)
            else:
                print('\n'.join("[{} {}] {}" \
                    .format(comment['userComment'],comment['positiveNegative'],comment['comment']) for comment in userpost['comments']))
    
     
def commentsbyuser_io(fakebook,args):
    userid = " ".join(args[0:])
    topic_id = input()
    if not fakebook.has_user(userid):
        print(USER_NOT_EXISTS % (userid))
    else:
        comments = fakebook.show_comments(userid,topic_id)
        if comments == []:
            print(NO_COMMENTS)
        else:
            print('\n'.join("[{} {} {} {}] {}" \
                .format(comment['userPost'],fakebook.show_posts(comment['userPost'],comment['numberOfPost'])['truthfulness'],comment['numberOfPost'],comment['positiveNegative'], comment['comment']) for comment in comments))
    """
    if userid nao fez comments
    print("No comments!")
    """
    
def topicfanatics_io(fakebook,args):
    #sorted()
    fanatism_id = " ".join(args[0:])    
    fanatics = sorted(fakebook.topic_fanatics(fanatism_id))
    if fanatics == []:
        print(NO_FANATICISM % (fanatism_id))
    else:
        print(*fanatics, sep = ", ", end=".\n")
    """if fanatismid desconhecido
    print(NO_FANATICISM, fanatismid)"""
    pass
    
def topicposts_io(fakebook,args):
    topic_id = " ".join(args[0:])
    posts = fakebook.topic_posts(topic_id)
    if posts == []:
        print (NO_TOPIC % (topic_id))
    else:   
        print('\n'.join("{} {} {}: {}" \
                .format(post['userid'],post['postid'],len(post['comments']),post['message']) for post in posts))
    
    """if topicid desconhecido
    print (NO_TOPIC, topicid)
    userpost postid numberOfComments: postmessage
    """
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