from random import choice
from secrets import token_urlsafe

from flask import Flask, request, render_template_string, redirect, url_for, session
from flask_session import Session


app = Flask(__name__)
app.secret_key = token_urlsafe(32)
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

CORRECT_MESSAGES = (
    "🎉 Ding ding ding! That’s the right answer!",
    "🎯 Bullseye! You nailed it!",
    "✅ Correctamundo! Keep it up!",
    "🏆 You got it! Nice work!",
    "💯 That’s a winner! Way to go!",
    "✨ Correct! You nailed it!",
    "🎊 Perfect! You’re crushing it!",
    "👏 Yes! You’re absolutely right!",
    "🎶 Cha-ching! That’s spot on!",
    "🌟 Bingo! You’ve got the right answer!",
)

WRONG_MESSAGES = (
    "🤔 Not quite! Try again!",
    "❌ Incorrect! Give it another shot!",
    "🚫 Nope! That’s not the answer!",
    "😬 Wrong! Keep trying!",
    "🙅‍♂️ Not the right answer! Try again!",
    "🤨 Incorrect! Give it another go!",
    "🤯 Wrong! Keep at it!",
    "🤭 Not quite! Give it another shot!",
    "🙈 Incorrect! Keep trying!",
    "🤫 Wrong! Try again!",
)

# HTML template for setting the correct answer
SET_ANSWER_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Set Answer</title>
    <style>
        body { font-family: Arial, sans-serif; background-color: #f4f4f9; color: #333; text-align: center; padding: 50px; }
        form { margin-top: 20px; }
        input[type="text"] { padding: 10px; width: 300px; font-size: 16px; }
        button { padding: 10px 20px; font-size: 16px; background-color: #5cb85c; color: white; border: none; cursor: pointer; }
        button:hover { background-color: #4cae4c; }
    </style>
</head>
<body>
    <h1>Set the Correct Answer</h1>
    <form method="POST">
        <label for="correct_answer">Enter the correct answer:</label><br><br>
        <input type="text" id="correct_answer" name="correct_answer" required><br><br>
        <button type="submit">Set Answer</button>
    </form>
</body>
</html>
"""

# HTML template for the main website
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Answer Checker</title>
    <style>
        body { font-family: Arial, sans-serif; background-color: #eef2f3; color: #333; text-align: center; padding: 50px; }
        h1 { color: #007bff; }
        form { margin-top: 20px; }
        input[type="text"] { padding: 10px; width: 300px; font-size: 16px; }
        button { padding: 10px 20px; font-size: 16px; background-color: #007bff; color: white; border: none; cursor: pointer; }
        button:hover { background-color: #0056b3; }
        .result { margin-top: 20px; font-size: 20px; font-weight: bold; }
    </style>
</head>
<body>
    <h1>Did you get the answer right?</h1>
    <form method="POST">
        <label for="answer">Enter your answer:</label><br><br>
        <input type="password" id="answer" name="answer" required><br><br>
        <button type="submit">Submit</button>
    </form>
    {% if result is not none %}
        <div class="result">{{ result }}</div>
        {% if sound_file is not none %}
        <audio autoplay>
            <source src="{{ sound_file }}" type="audio/mpeg">
            Your browser does not support the audio element.
        </audio>
        {% endif %}
    {% endif %}
</body>
</html>
"""

@app.route('/set-answer', methods=['GET', 'POST'])
def set_answer():
    if request.method == 'POST':
        correct_answer = request.form.get('correct_answer')
        session['correct_answer'] = correct_answer
        return redirect(url_for('index'))
    return render_template_string(SET_ANSWER_TEMPLATE)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    sound_file = None

    correct_answer = session.get('correct_answer')
    if not correct_answer:
        return redirect(url_for('set_answer'))

    if request.method == 'POST':
        user_answer = request.form.get('answer')
        if user_answer == correct_answer:
            result = choice(CORRECT_MESSAGES)
            sound_file = "static/success.mp3"
        else:
            result = choice(WRONG_MESSAGES)
            sound_file = "static/fail.mp3"

    return render_template_string(HTML_TEMPLATE, result=result, sound_file=sound_file)

if __name__ == '__main__':
    # Run the app
    app.run(debug=True)
