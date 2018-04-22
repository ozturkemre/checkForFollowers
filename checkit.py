from steem import Steem
import os


def writeToFile(followers):
    with open("{}.txt".format(account_name), "w+") as w:
        w.write("\n".join(followers))


def getOldFollowers():
    with open("{}.txt".format(account_name), "r") as w:
        result = w.read().splitlines()
        return result


def getNewFollowers(list2):
    old = getOldFollowers()
    return list(set(list2) - set(old))


def getUnfollowers(list2):
    old = getOldFollowers()
    return list(set(old) - set(list2))


def printNewFollowers(new_followers):
    if new_followers:
        print("New followers:")
        for i in new_followers:
            print(i)
    else:
        print("No new followers")


def printUnfollowers(unfollowers):
    if unfollowers:
        print("Unfollowers:")
        for i in unfollowers:
            print(i)
    else:
        print("No unfollowers")

def addToFollowerList(followers, l):
    for i in l:
        followers.append(i['follower'])


account_name = input("Enter account name: ")
s = Steem()
account = s.get_follow_count(account_name)

print("Account: {} has {} follower(s)".format(account_name, account['follower_count']))
info = s.get_followers('{}'.format(account_name), 0, 'blog', account['follower_count'])

followers = []

addToFollowerList(followers, info)

if os.path.isfile(os.getcwd() + "/{}.txt".format(account_name)):
    unfollowers = getUnfollowers(followers)
    new_followers = getNewFollowers(followers)
    printNewFollowers(new_followers)
    printUnfollowers(unfollowers)
else:
    print("First time run")

writeToFile(followers)

