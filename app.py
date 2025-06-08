from flask import Flask, jsonify

app = Flask(__name__)

# Sample SAT questions data
QUESTIONS = [
    {
        "id": 1,
        "section": "Math",
        "prompt": "What is the value of x in the equation 2x + 3 = 7?",
        "options": ["1", "2", "3", "4"],
        "answer": "B"  # Correct option index 1 (option "2")
    },
    {
        "id": 2,
        "section": "Reading",
        "prompt": "Which choice best describes the main idea of the passage?",
        "options": ["Choice A", "Choice B", "Choice C", "Choice D"],
        "answer": "A"
    }
]

@app.route('/questions')
def get_questions():
    """Return a list of SAT questions in JSON format."""
    return jsonify(QUESTIONS)

if __name__ == '__main__':
    app.run(debug=True)
