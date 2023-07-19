from flask import Flask,  render_template , jsonify

app = Flask(__name__)

JOBS = [
  {
    'id' : 1,
    'title' : "Data Engineer",
    'location' : "Bengaluru, India",
    'salary' : "10,00,000",
  },
  {
    'id' : 2,
    'title' : "Data Scientist",
    'location' : "Delhi, India",
    'salary' : "20,00,000",
  },
  {
    'id' : 3,
    'title' : "Front End Developer",
    'location' : "Mumabi, India",
    'salary' : "15,00,000",
  },
  {
    'id' : 4,
    'title' : "Backend Developer",
    'location' : "Mumabi, India",
  }
]

@app.route("/")
def hello_world():
    return render_template("home.html", jobs = JOBS , company_name = "Test")

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)

if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
    