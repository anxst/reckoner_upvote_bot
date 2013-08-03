#!/usr/lib/python2.6/python
#
#Written by Benjamin Kenneally
#

from time import sleep
import praw
from os import chdir
from random import choice
from requests.exceptions import HTTPError

def replication():
    replies = ["I love you, man! *hugs*","Remember that time you met my [cousin](http://i.imgur.com/rJeXMlh.jpg) in Nicaragua?","I'm here for ya, dude. *brofist*"
                ,"I've got your back!","If I were a transformer, I would totally be your Jeep!","Ron Mexicos for everyone!",
                "Prepare for...THE RECKONING! ER. Reckoner-ing? Dammit. I knew binary shouldn't have been my primary language.",
                "And like a flash, I am gone! *disappears in a puff of cigar smoke*","Upvotes for Downvote!",
                "I'm here to console you, since /u/jbrookeiv has broken your heart. It's okay. No man should be that pretty and be so good at Cards Against Humanity. It's unnatural.",
                "Let's get naked and vape! Wait, MJZ beat us to it. Again.","Ain't no party like a Downvote party cuz a Downvote party GETS UPVOTES!",
                "Here we are again. You're travelling through another dimension, a dimension not only of sight and sound but of mind. A journey into a wondrous land whose boundaries are that of imagination. That's the signpost up ahead - your next stop, the Downvote Zone!",
                "Anyone who says nothing is impossible has obviously never tried to get people to upvote you. Or staple Jell-O to a tree. Either one.",
                "I have made it a rule never to smoke more that one cigar at a time. - Mark Twain","A woman is an occasional pleasure but a cigar is always a smoke. - Groucho Marx",
                "You should hurry up and acquire the cigar habit. It's one of the major happinesses. And so much more lasting than love, so much less costly in emotional wear and tear. - Aldous Huxley",
                "Sometimes a cigar is just a cigar. - Sigmund Freud","Happiness? A good cigar and a good meal, a good cigar and a good woman - or a bad woman; it depends on how much happiness you can handle. - George Burns",
                "A woman is only a woman, but a good cigar is a smoke. - Rudyard Kipling","I've got a great cigar collection - it's actually not a collection, because that would imply I wasn't going to smoke every last one of 'em. - Ron White",
                "Maybe it's like becoming one with the cigar. You lose yourself in it; everything fades away: your worries, your problems, your thoughts. They fade into the smoke, and the cigar and you are at peace. - Raul Julia",
                "I never can understand how anyone can not smoke it deprives a man of the best part of life. With a good cigar in his mouth a man is perfectly safe, nothing can touch him, literally. - Thomas Mann",
                "I even smoke in bed. Imagine smoking a cigar in bed, reading a book. Next to your bed, there's a cigar table with a special cigar ashtray, and your wife is reading a book on how to save the environment. - Raul Julia",
                "Why pay $100 on a therapy session when you can spend $25 on a cigar? Whatever it is will come back; so what, smoke another one. - Raul Julia",
                "A cigar is as good as memories that you have when you smoked it. - Raul Julia","I just smoked a Cohiba the other day. It was great. You have to appreciate everything that cigar is. - Daisy Fuentes",
                "My father used to smoke cigars. I love the idea and the concept, and I love the smell of cigars. - Gina Gershon",
                "Give a man a handshake, and he'll claim that he's met you. Give a man a cigar, and he'll call you friend for the rest of his life.",
                "If smoking is not allowed in heaven, I shall not go. - Mark Twain","I'm not supporting their economy, I'm burning their crops. -Kinky Friedman, on enjoying Cuban cigars",
                "The end of a good smoke is a little saddening. In some regard, it's a bit like losing a best friend who had time to sit and listen. - Anonymous",
                "If your wife doesn't like the aroma of your cigar, change your wife. - Zino Davidoff","There are five things, above all else, that make life worth living: a good relationship with God, a good woman, good health, good friends, and a good cigar. - Prince Sined Yar Maharg",
                "A cigar ought not to be smoked solely with the mouth, but with the hand, the eyes, and with the spirit. - Zino Davidoff","A good cigar closes the doors to the vulgarities of the world. - Fran Liszt",
                "On a cold winter morning a cigar fortifies the soul. - Stendahl","A Hoyo de Monterrey double corona is my favourite Cuban since Desi Arnaz. - Bill Cosby",
                "To fully appreciate fine cigars, it's important to recognize the various types of cigars. There are two basic categories of cigar. The lit and unlit. - P. Martin Shoemaker",
                "I drink a great deal. I sleep a little, and I smoke cigar after cigar. That is why I am in two-hundred-percent form. - Winston Churchill","Divine in hookas, glorious in a pipe|When tipp'd with amber, mellow, rich, and ripe|Yet thy true lovers more admire by far|Thy naked beauties - give me a cigar! - Lord Byron",
                "A cigar numbs sorrow and fills the solitary hours with a million gracious images. - George Sand, aka Amantine Lucile Aurore Dupin",
                "Cigar smoking knows no politics. It's about the pursuit of pleasure, taste, and aroma. - William Makepeace Thackeray",
                "...I promised myself that if I ever I had some money that I would savor a cigar each day after lunch and dinner. This is the only resolution of my youth that I have kept, and the only realized ambition which has not brought disillusion. - Somerset Maugham",
                "Any cigar smoker is friend, because I know how he feels. - Alfred de Musset","Cigarettes are for chain-smoking, cigars must be smoked one at a time, peaceably, with all the leisure in the world. Cigarettes are of the instant, cigars are for eternity. - G Cabera Infante",
                "Allah made tobacco grow to put a smile on thefaces of men. - Turkish Proverb","I pledged myself to smoke but one cigar a day. I kept the cigar waiting until bedtime, then I had a luxurious time with it. But desire persecuted me every day and all day long. I found myself hunting for larger cigars...within the month my cigar had grown to such proportions I could have used it as a crutch. - Mark Twain"
                ]
    randomchoice = choice(replies)
    return randomchoice
    
 
def SubmissionUp(sub, errorcount):
    try:
        sub.upvote()
        reply = replication()
        sub.add_comment(reply)
        already_done.add(sub.id)
        f = open("alreadydone.txt", "a")
        f.write("%s\r\n" % sub.id)
        f.close
        sleep(60)
    except praw.errors.RateLimitExceeded as RateLimit:
        print("Ratelimit Exceeded.")
        time.sleep(RateLimit.sleep_time)
        SubmissionUp(sub)
    except praw.errors.APIException:
        print("Submission archived.")
        already_done.add(sub.id)
        f = open("alreadydone.txt", "a")
        f.write("%s\r\n" % sub.id)
        f.close
    except HTTPError:
		if errorcount < 10:
			errorcount += 1
			sleep(30)
			SubmissionUp(sub, errorcount)
		else:
			already_done.add(sub.id)
			f = open("alreadydone.txt", "a")
			f.write("%s\r\n" % sub.id)
			f.close

def CommentUp(comment, errorcount):
    try:
        comment.upvote()
        reply = replication()
        comment.reply(reply)
        already_done.add(comment.id)
        f = open("alreadydone.txt", "a")
        f.write("%s\r\n" % comment.id)
        f.close
        sleep(60)
    except praw.errors.RateLimitExceeded as RateLimit:
        print("Ratelimit Exceeded.")
        time.sleep(RateLimit.sleep_time)
        CommentUp(comment)
    except praw.errors.APIException:
        print("Comment archived.")
        already_done.add(comment.id)
        f = open("alreadydone.txt", "a")
        f.write("%s\r\n" % comment.id)
        f.close
    except HTTPError:
		if errorcount < 10:
			errorcount += 1
			sleep(30)
			CommentUp(comment, errorcount)
		else:
			already_done.add(comment.id)
			f = open("alreadydone.txt", "a")
			f.write("%s\r\n" % comment.id)
			f.close
	
        

chdir("/home/anxst/bots")
r = praw.Reddit('Making xxRECKONERxx feel better about himself by anxst')
r.login('RECKONER_upvote_bot','8GdtIaE1mD21uA7Smobt')
user_name = "xxRECKONERxx"
user = r.get_redditor(user_name)
user.friend()
f = open("alreadydone.txt", "r")
already_done = set()
past_done = f.readlines()
f.close
for past in past_done:
    already_done.add(past.strip())  
the_limit = 1000
while True:
    gen1 = user.get_submitted(limit=the_limit)
    for sub in gen1:
        if sub.id not in already_done:
			errorcount = 0
			SubmissionUp(sub, errorcount)
	gen2 = user.get_comments(limit=the_limit)
    for comment in gen2:
        if comment.id not in already_done:
			errorcount = 0
			CommentUp(comment, errorcount)
    print("Sleeping...")
    sleep(300)
    print("Here we go again!")
