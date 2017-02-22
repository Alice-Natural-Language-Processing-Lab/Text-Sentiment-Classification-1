import csv
import random
import processing_data_set
import preprocessing
import string_match



def Main():
	fp = csv.reader(open('../../DataSet/Tweets_sample2.csv','rb'),delimiter=',',quotechar='"')
	
	data_list = processing_data_set.data_list(fp)
	
	random.shuffle(data_list)
	
	#reading the stopwords file

	stopword_file=open('../../utils/stopwords','r')

	stopwords=[]
					#reading stopwords line by line

	'''s=stopword_file.readline()

	while s:
		stopwords.append(s[:-1])
		s=stopword_file.readline()'''

	

					#stopwords file created and stored in dictionary

					#wordpolarity dictionary to store polarities of words

	wordpolarity={}

	polarword_file=open('positive_words_without_polarity','rb')

	s=polarword_file.readline()

	while s:
		s=s+"	2"
		ele=s.split()
		#print ele[0],ele[1]
		wordpolarity[ele[0]]=ele[1]
		s=polarword_file.readline()

	polarword_file=open('negative_words_without_polarity','r')

	s=polarword_file.readline()
	
	while s:
		s=s+"	-2"
		ele=s.split()
		#print ele[0],ele[1]
		wordpolarity[ele[0]]=ele[1]
		s=polarword_file.readline()

					#reading from first wordpolarity file 

	polarword_file=open('word_polarity1','r')

	s=polarword_file.readline()

	while s:
		ele=s.split()
		wordpolarity[ele[0]]=ele[1]
		s=polarword_file.readline()


					#reading from second wordpolarity file

	polarword_file=open('word_polarity2','r')

	s=polarword_file.readline()

	while s:
		ele=s.split()
		wordpolarity[ele[0]]=ele[1]
		s=polarword_file.readline()


					#making narrowwords dictionary to store short forms

	narrowwords={}
					#reading the narrowwords file(opening and reading line by line)

	narrow_word=open('../../utils/narrow_words','r')

	s=narrow_word.readline()

	while s:
		ele=s.split()
		element=''
		for x in range(1,len(ele)):
			element=element+' '+ele[x]
		narrowwords[ele[0].lower()]=element.lower()
		s=narrow_word.readline()

	#print narrowwords

					#dictionary for storing smileys and their meanings

	smileys={}
					#reading from 1st file of smileys line by line

	smiley=open('../../utils/smileys','r')

	s=smiley.readline()

	while s:
		ele=s.split()
		element=''
		for x in range(len(ele)-1):
			element=element+" "+ele[x]
		smileys[ele[len(ele)-1]]=element.lower()
		s=smiley.readline()


					#second file of smileys to be processed

	smiley=open('../../utils/smiley2','r')

	s=smiley.readline()

	while s:
		ele=s.split()
		element=''
		for x in range(1,len(ele)):
			element=element+" "+ele[x]
		smileys[ele[0]]=element.lower()
		s=smiley.readline()

	#print smileys
	
	count = 0

	for i in data_list :
		
		i[0] = preprocessing.preprocess(i[0])
		
		result=string_match.string_match(i[0],stopwords,wordpolarity,narrowwords,smileys)
		if result==i[1]:
			count=count+1;
	print "Average polarity : ",2
	print "Correct results : ",count
	print "Total queries : ",len(data_list)
	print "Efficiency : ",100*count/float(len(data_list))


Main()
