from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def index_page():
    # Return this as a strange
    # return "<html><body>This is the homepage.</body></html>"

    # Alternately, we could make this a Jinja template in `templates/`
    # and return that result of rendering this, like:
    #
    return render_template("index.html")

@app.route("/application_home")
def application_page():
	return render_template("application-form.html")


@app.route("/application" methods=['POST'])
def application_return():
	first_name = request.args.get("firstname")
	last_name = request.args.get("lastname")
	salary_requirements = request.args.get("salaryreq")
	job_title = request.args.get("jobtitle")

	return render_template("confirm.html", first_name=firstname, 
		last_name=lastname, salary_requirements=salaryreq, 
		job_title=jobtitle)


if __name__ == "__main__":
    app.run(debug=True)