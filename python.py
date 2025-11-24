from flask import Flask, request, render_template_string

app = Flask(__name__)

question = {
    "index": 1,
    "text": "Hồ Lê Anh Pháp có yêu Phùng Thị Anh Thư không?",
    "special": False,
    "answers": {
        "A": "Không",
        "B": "Thỉnh thoảng",
        "C": "Yêu rất nhiều",
        "D": "Có"
    },
    "correct": "C"
}

html_template = """
<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<title>Câu hỏi trắc nghiệm</title>
<style>
    body { font-family: Arial; margin: 40px; }
    .answer-btn {
        display: block;
        width: 250px;
        padding: 10px;
        margin: 8px 0;
        border: 1px solid #888;
        background: #f0f0f0;
        border-radius: 6px;
        cursor: pointer;
        text-align: left;
        font-size: 16px;
    }
    .answer-btn:hover { background: #ddd; }
    .correct { color: green; font-weight: bold; }
    .wrong { color: red; font-weight: bold; }
</style>
</head>
<body>
<h2>
    {% if question.special %}
        Câu hỏi đặc biệt: {{ question.text }}
    {% else %}
        Câu hỏi {{ question.index }}: {{ question.text }}
    {% endif %}
</h2>
<form method="POST">
    {% for key, value in question.answers.items() %}
        <button class="answer-btn" type="submit" name="answer" value="{{ key }}">
            {{ key }}. {{ value }}
        </button>
    {% endfor %}
</form>
{% if result == "correct" %}
    <p class="correct">✔ Bạn đã trả lời đúng!</p>
{% elif result == "wrong" %}
    <p class="wrong">✘ Bạn đã trả lời sai, hãy thử lại!</p>
{% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def quiz():
    result = None
    if request.method == "POST":
        answer = request.form.get("answer")
        if answer == question["correct"]:
            result = "correct"
        else:
            result = "wrong"
    return render_template_string(html_template, question=question, result=result)

if __name__ == "__main__":
    app.run(debug=True)
