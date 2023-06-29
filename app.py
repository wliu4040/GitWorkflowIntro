from flask import Flask
from flask import render_template


app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/2022")
def cohort_2022():
    return render_template('students_2022.html')

@app.route("/2023")
def cohort_2023():
    return render_template('students_2023.html')

@app.route("/nat_uts")
def team_nat_uts():
    return render_template('teams/nat_uts.html')

@app.route("/james_david")
def team_james_david():
    return render_template('teams/james_david.html')

@app.route("/dong_zach_dar")
def team_dong_zach_dar():
    return render_template('teams/dong_zach_dar.html')

@app.route("/alison_rob_shawn")
def team_alison_rob_shawn():
    return render_template('teams/alison_rob_shawn.html')

@app.route("/nick_val")
def team_nick_val():
    return render_template('teams/nick_val.html')

@app.route("/luke_noah_maya")
def team_luke_noah_maya():
    return render_template('teams/luke_noah_maya.html')
