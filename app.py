from flask import Flask, render_template, request

app = Flask(__name__)

# Quiz questions (10 on HTML & CSS)
questions = [
    {
        "id": 1,
        "question": "What does HTML stand for?",
        "options": ["Hyperlinks and Text Markup Language", "Hyper Text Markup Language", "Home Tool Markup Language", "Hyperlinks Text Management Language"],
        "answer": "Hyper Text Markup Language"
    },
    {
        "id": 2,
        "question": "Which HTML tag is used to define an internal style sheet?",
        "options": ["<script>", "<style>", "<css>", "<design>"],
        "answer": "<style>"
    },
    {
        "id": 3,
        "question": "Which property is used to change the background color in CSS?",
        "options": ["color", "bgcolor", "background-color", "background"],
        "answer": "background-color"
    },
    {
        "id": 4,
        "question": "Which HTML element is used for the largest heading?",
        "options": ["<h6>", "<h1>", "<heading>", "<head>"],
        "answer": "<h1>"
    },
    {
        "id": 5,
        "question": "Which CSS property controls the text size?",
        "options": ["font-size", "text-style", "text-size", "font-style"],
        "answer": "font-size"
    },
    {
        "id": 6,
        "question": "How can you make a numbered list in HTML?",
        "options": ["<ul>", "<list>", "<ol>", "<dl>"],
        "answer": "<ol>"
    },
    {
        "id": 7,
        "question": "Which CSS property is used to make text bold?",
        "options": ["font-weight", "bold", "text-bold", "style"],
        "answer": "font-weight"
    },
    {
        "id": 8,
        "question": "Which HTML tag is used to create a hyperlink?",
        "options": ["<a>", "<link>", "<href>", "<hyper>"],
        "answer": "<a>"
    },
    {
        "id": 9,
        "question": "Which CSS property is used to center text?",
        "options": ["align", "text-align", "center", "alignment"],
        "answer": "text-align"
    },
    {
        "id": 10,
        "question": "Which HTML tag is used to display an image?",
        "options": ["<img>", "<picture>", "<image>", "<src>"],
        "answer": "<img>"
    }
]

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/quiz')
def quiz():
    return render_template("quiz.html", questions=questions)

@app.route('/result', methods=['POST'])
def result():
    score = 0
    results = []
    for q in questions:
        selected = request.form.get(str(q["id"]))
        correct = (selected == q["answer"])
        if correct:
            score += 1
        results.append({
            "question": q["question"],
            "selected": selected,
            "correct_answer": q["answer"],
            "is_correct": correct
        })
    return render_template("result.html", score=score, total=len(questions), results=results)

if __name__ == '__main__':
    app.run(debug=True)
