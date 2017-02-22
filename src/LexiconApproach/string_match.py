import re
import tell_sentiment

def string_match(string,stopwords,wordpolarity,narrowwords,smileys):
	
	#print string
					

					#performing operation split on string passed,
					  # to identify narrowwords and smileys involved
					  # and reforming string with values of narrow
					  #words and smileys placed 

	words=string.split();

	string=''
	for i in range(len(words)):
		if words[i] in narrowwords:
			string=string+' '+narrowwords[words[i]]

		elif words[i] in smileys:
			string=string+' '+smileys[words[i]]

		else :
			string=string+' '+words[i]
		#print string

					# now in string we have string with proper values
					# of narrowwords and smileys 

					# removing punctuation marks from string
					# as follows
	words=re.split('[,!:_\-;?\s]\s*',string)
	
	#print words

	# positive and negative lists to store positive and negative words 
	 # contained in string

	positive=[]
	negative=[]

		#finding positive and negative words and also stopwords
		 # from words, which has string without narrowwords,smileys
		 # and puntuation marks

	for i in range(len(words)):
		if words[i] not in stopwords and words[i] in wordpolarity:
			if float(wordpolarity[words[i]])>0:
				positive.append(words[i])

			elif float(wordpolarity[words[i]])<0:
				negative.append(words[i])

	#print positive
	#print negative

	# tell sentiment called to identify polarities of words and decide 
	# the positivity or negativity of sentences.. 

	return tell_sentiment.tell_sentiment(positive,negative,wordpolarity)