from flask import Flask, render_template, request, session, redirect
from surveys import personality_quiz, satisfaction_survey

app = Flask(__name__)

responses = []
questions_answered = 0

@app.route('/')
def index():
    quiz_type = satisfaction_survey.title
    quiz_inst = satisfaction_survey.instructions
    return render_template('Homepage.html', quiz_type=quiz_type, quiz_inst=quiz_inst)

@app.route('/questions')
def qs():
    return 'Question page'

@app.route('/questions/<qnum>')
def show_question(qnum):
    num = int(qnum)
    quiz_qs = satisfaction_survey.questions[num].question
    quiz_answ = satisfaction_survey.questions[num].choices
    
    next_num = int(qnum) + 1
    return render_template('questions.html', quiz_qs=quiz_qs, quiz_answ=quiz_answ, next_num=next_num, num=num)

@app.route('/questions/<qnum>', methods=['POST'])
def posting_questions(qnum):
    num = int(qnum)
    answer = request.form[f'q{num}']
    print(answer)
    responses.append(answer)
    print(responses)
    
    # # quiz_qs = satisfaction_survey.questions[num].question
    # # quiz_answ = satisfaction_survey.questions[num].choices
    next_num = int(qnum) + 1
    question_length = len(satisfaction_survey.questions)
    if next_num == question_length:
        return redirect('/thankyou')
    return redirect(f'/questions/{next_num}')

@app.route('/thankyou')
def thankyou():
    return '<h2>Thank you for completing this Survey</h2>'