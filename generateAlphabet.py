#!/usr/bin/python

def main():
	alphabetFile = open('alphabet.html', 'w')
	alphabetFile.write("<html>")
	alphabetFile.write("<head><title>Women's script</title></head>")
	alphabetFile.write("<body>")
	alphabetFile.write("<table border='0'>")
	alphabetFile.write("<tr>")
	alphabet = [ [ "A", "B", "C", "D", "E" ], [ "F", "G", "H", "I", "J"] , [ "K", "L", "M", "N", "O" ], [ "P", "Q", "R", "S", "T" ], [ "U", "V", "W", "X", "Y" ], [ "Z", "SH", "CH", "TH", "" ] ]
	for letters in alphabet:
		for letter in letters:
			if letter == "C":
				alphabetFile.write("<td align='center' width='200px'><img src='images/{}.svg' width='50%'/><img src='images/{}.svg' width='50%' /></td>".format( "T", "S" ))
			elif letter == "Q":
				alphabetFile.write("<td align='center' width='200px'><img src='images/{}.svg' width='50%'/><img src='images/{}.svg' width='50%' /></td>".format( "K", "U" ))
			elif letter == "W":
				alphabetFile.write("<td align='center' width='200px'><img src='images/{}.svg' width='50%'/></td>".format( "V" ))
			elif letter == "X":
				alphabetFile.write("<td align='center' width='200px'><img src='images/{}.svg' width='50%'/><img src='images/{}.svg' width='50%' /></td>".format( "K", "S" ))
			elif letter == "":
				alphabetFile.write("<td></td>")
			else:
				alphabetFile.write("<td align='center' width='200px'><img src='images/{}.svg' width='50%'/></td>".format( letter ))
		alphabetFile.write("</tr>")
		alphabetFile.write("<tr>")
		for letter in letters:
			alphabetFile.write("<td align='center' valign='top' height='100px'><b>{}</b></td>".format( letter ))
		alphabetFile.write("</tr>")
	alphabetFile.write("<tr><td align='center' colspan=5><a href='https://www.coppermind.net/wiki/Women%27s_script'> Women's script taken from coppermind.net </a></td><tr>")
	alphabetFile.write("</table>")
	alphabetFile.write("</body>")
	alphabetFile.write("</html>")
	alphabetFile.close()

if __name__ == "__main__":
	main()
