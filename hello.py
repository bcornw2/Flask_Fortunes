from flask import Flask, request
from fortune import fortune
from datetime import datetime

app = Flask(__name__)
app.config["DEBUG"] = True
@app.route("/", methods=["GET", "POST"])
#d = datetime.datetime.now().strftime("%I:%Mp on %B %d, %Y")
def runFortune():
	d = datetime.now()
	errors = ""
	if request.method =="POST":
#		date_time = datetime.strptime(date_time_string, '%Y-%m-%d %H:%M')
		#question = None
		#try:
		question = request.form.get('question')
		#except:
		#	errors += "<p>{!r} is a broken value.</p>\n".format(request.form["question"])
		if question is not None:
			result = fortune()
			f=open("audit.txt", "a+")
			f.write(str(d) + " - " + question + "\n")
			print(question)
			question = str(question)
#			question = request.form.get("question")
		#	question = str(question)
			return '''
				<html>
					<body>
						<p>Your Question:  {question}</p>
						<p>Your Fortune: </p>
						<p>ºø,,øº`ºø,,øºø,,øº`ºø,</p>
						<h1>  {result}   </h1>
						<p>ºø,,øº`ºø,,øºø,,øº`ºø,</p>
						<p><a href="/">Click here to ask another question</p>
					</body>
				</html>
			'''.format(result=result, question=question)
	return '''
		<html>
			<body>
				<h3>Welcome to Ben's Crystal Ball!</h3>
				<p>Ask a question if ye dare</p>
				<form method="post" action=".">
					<p><input name="question" /></p>
					<p><input type="submit" value = "Seek Fortune" /></p>
				</form>
			</body<
		</html>
	'''.format(errors=errors)

if __name__ == '__main__':
	app.run(debug=True, port=8080, host = '0.0.0.0')
