from FDADrug import FDADrugAdv
from FDADrug import FDADrugEasy

import praw
import time


#Reddit Login
reddit = praw.Reddit(user_agent="Drug Information v0.1")
print("Attempting to login...")
reddit.login("USERNAME", "PASSWORD", disable_warning=True)
print("Logged In.")
subreddit = "SUBREDDIT"


#Find matches
def find_all(a_string, sub):
    result = []
    indexes = []
    matches = []

    k = 0

    while k < len(a_string):

        k = a_string.find(sub, k)


        indexes.append(k)

        if k == -1:
            break

        k += 1


    for i in indexes:
        spaceIndex = 0
        tempString = a_string[i:]


        ending_list = [" ", "\n", ".", ",", ":", ";", "[", "]", '"', "'", "/", "?", "-",  "+", "=", "_", "|", "\\"]

        for t in ending_list:
            if (tempString.find(t) != -1):
                spaceIndex = tempString.find(t)
                tempString = tempString[:-(len(tempString) - spaceIndex)]


        if (tempString[1:].find("!") != -1):

            spaceIndex = tempString[1:].find("!")

            tempString = tempString[:-(len(tempString) - spaceIndex -1)]

        if tempString != "!":
            if tempString != "":
                matches.append(tempString[1:])



        for m in matches:
            if(len(m) == 0):
                matches.remove(m)



    return matches


#Search and make comments
while (1 == 1):
    try:

        print("Refreshed Comments")

        check = open("checked_comments.txt", "r")
        checked = check.readlines()

        check.close()

        subreddit_comments = reddit.get_comments(subreddit)

        for comment in subreddit_comments:

            comment_to_make = ""

            if comment.id + "\n" not in checked:

                file = open("checked_comments.txt", "a")
                file.write(comment.id + "\n")
                file.close()

                for match in find_all(comment.body, "!"):

                    fda = FDADrugEasy(str(match))

                    comment_to_make += "#" + fda.getName()

                    comment_to_make += "\n\n"

                    comment_to_make += "**Description:** " + fda.getLabel("description")



                    comment_to_make += "\n\n"

                    comment_to_make += "**Usage:** " + fda.getLabel("indications_and_usage")


                    comment_to_make += "\n\n"

                if comment_to_make != "":
                    comment_to_make += "*^^I ^^am ^^a ^^bot, ^^bleep-bloop. ^^Drug ^^information ^^compiled ^^from ^^the ^^FDA ^^API. ^^Contact ^^/u/USERNAME ^^for ^^bug ^^reports.* ***^^DO ^^YOUR ^^OWN ^^RESEARCH.***"


                    comment.reply(comment_to_make)
                    print(comment_to_make)
    except:
        pass

    time.sleep(5)
