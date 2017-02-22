def tell_sentiment(positive,negative,wordpolarity):
	
	sumpos=0
	sumneg=0
	for i in range(len(positive)):
		sumpos=sumpos+float(wordpolarity[positive[i]])

	for i in range(len(negative)):
		sumneg=sumneg+float(wordpolarity[negative[i]])

	if sumpos+sumneg>0:
		return "positive"
	else :
		return "negative"

	if sumneg!=0 and sumpos+sumneg==0:
		return "Negative"


	'''if sumpos+sumneg==0:
		return "positive statement"
	elif sumpos+sumneg==1:
		return "positive"
	elif sumpos+sumneg in range(2,4):
		return "positive"
	elif sumpos+sumneg>=4:
		return "positive"
	elif sumpos+sumneg==-1:
		return "negative"
	elif sumpos+sumneg in range(-3,-1):
		return "negative"
	elif sumpos+sumneg<-3:
		return "negative"'''
