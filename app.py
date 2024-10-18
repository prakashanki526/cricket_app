from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route('/')
def index():
    # Simulating score data
    team_score = random.randint(100, 200)
    strike_rate = round(random.uniform(75, 150), 2)  # Strike rate rounded to 2 decimal places
    run_rate = round(random.uniform(4.0, 7.0), 2)    # Run rate rounded to 2 decimal places
    overs = round(random.uniform(10, 20), 1)         # Simulating overs (10 to 20 overs), rounded to 1 decimal place
    wickets = random.randint(0, 10)                  # Simulating wickets (0 to 10)

    return render_template('score.html', team_score=team_score, strike_rate=strike_rate, 
                           run_rate=run_rate, overs=overs, wickets=wickets)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

