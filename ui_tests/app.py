from flask import Flask, request, render_template
from solution import Solution

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def min_window_form():
    result = ""
    if request.method == 'POST':
        s = request.form['s']
        t = request.form['t']
        solution = Solution()
        result = solution.minWindow(s, t)
    return render_template('form.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)