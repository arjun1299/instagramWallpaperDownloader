import instaloader
import os

target='memes'
L = instaloader.Instaloader()

#############################################################
usernames=["69possums420","beautyraccoons","beelovespossums","nocturnaltrashposts","the_squirrel_diaries"]
maxNumberOfPicsFromAccounts=2;
#############################################################

for username in usernames:

    posts = instaloader.Profile.from_username(L.context, username).get_posts()
    ind=0
    for i in posts:
        if ind >=maxNumberOfPicsFromAccounts:
            break
        L.download_post(i,target)
        ind+=1

#############################################################
for i in os.listdir(target):
    print(i)
    if("UTC_" in i and "UTC_1" not in i) or (".jpg" not in i):
        os.remove(target+"/"+i)
    
