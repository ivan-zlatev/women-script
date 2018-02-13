#!/usr/bin/python

import argparse
import re

parser = argparse.ArgumentParser( description='convert latin letters to women\'s script' )
parser.add_argument('string', metavar='sentence', type=str, help='sentence to be converted')
args = parser.parse_args()

def main():
	sentence = args.string.upper()
	for number in range(0, 9, 1):
		sentence = sentence.replace( str(number), "")
	for symbol in ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "-", "+", "=", ".", ",", ":", "'" ]:
		sentence = sentence.replace( symbol, " " )
	original = sentence
	sentence = sentence.replace( "SH", "1" )
	sentence = sentence.replace( "CH", "2" )
	sentence = sentence.replace( "TH", "3" )
	sentence = re.sub(' +', ' ', sentence).split(" ")
	output = open('sentence.html', 'w')
	output.write("<html>\n\t<head>\n\t\t<title>Women's script custom sentence</title>\n\t</head>\n\t<body>\n")
	output.write("\t\t<table border='0'>\n")
	output.write("\t\t\t<tr>\n")
	for word in sentence:
		for letter in word:
			output.write("\t\t\t\t<td>")
			output.write(translateLetter(letter))
			output.write("</td>\n")
	output.write("\t\t\t</tr>\n\t\t\t<tr>\n\t\t\t\t<td align='center' colspan='{}'><b>{}</b></td>\n\t\t\t</tr>\n\t\t</table>\n".format( len("".join(sentence)), original))
	output.write("&nbsp;")
	for word in sentence:
		output.write("\t\t<table border='0'>\n")
		output.write("\t\t\t<tr>\n")
		for letter in word:
			output.write("\t\t\t\t<td>")
			output.write(translateLetter(letter))
			output.write("</td>\n")
		output.write("\t\t\t</tr>\n\t\t\t<tr>\n\t\t\t\t<td align='center' colspan='{}'><b>{}</b></td>\n\t\t\t</tr>\n\t\t</table>\n".format( len(word), word.replace("1", "SH").replace("2", "CH").replace("3", "TH")))
		output.write("&nbsp;")
	output.close()

def translateLetter( letter ):
	if letter == "C":
		return "<img src='images/{}.svg' height='50%'/><img src='images/{}.svg' height='50%'/>".format( "T", "S" )
	elif letter == "Q":
		return "<img src='images/{}.svg' height='50%'/><img src='images/{}.svg' height='50%'/>".format( "K", "U" )
	elif letter == "W":
		return "<img src='images/{}.svg' height='50%'/>".format( "V" )
	elif letter == "X":
		return "<img src='images/{}.svg' height='50%'/><img src='images/{}.svg' height='50%'/>".format( "K", "S" )
	elif letter == "1":
		return "<img src='images/{}.svg' height='50%'/>".format( "SH" )
	elif letter == "2":
		return "<img src='images/{}.svg' height='50%'/>".format( "CH" )
	elif letter == "3":
		return "<img src='images/{}.svg' height='50%'/>".format( "TH" )
	else:
		return "<img src='images/{}.svg' height='50%'/>".format( letter )

if __name__ == "__main__":
	main()
