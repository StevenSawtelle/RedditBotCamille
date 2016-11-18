import praw
import re

def camille_misspelled(c):
	text = c.body
	wordsList = text.split
	if "camile" in wordsList or "camilie" in wordsList:
		return True

def correct_spelling(c, reply=True):
	if reply:
		text = "Actually, it's Camille. Here's what your comment shoud look like:\n"
		fixedComment = re.sub(r'Camil?li?e',r'Camille',c.body)
		c.reply(text+fixedComment)

if __name__ is '__main__':
    
	r = praw.Reddit(user_agent='Camille Spellchecker for r/lol 1.0 by u/baconologist')

	r.login()

	for c in praw.helpers.comment_stream(r, 'leagueoflegends'):
		if(camille_misspelled(c)):
			correct_spelling(c)
