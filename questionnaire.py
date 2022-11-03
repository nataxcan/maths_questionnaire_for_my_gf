# y = 15x + b
# in year 5 there are 50 mushrooms

# number * 0 = ?
# number * 1 = ?
# number + 0 = ?
# number - 1 = ?
# number * -1 = ? *!
# number * 0 + number = ?
# number + 0 * number = ? *!
# number / 10 = ?
# number * 10 = ?
# number + number / number = ?

# y = ax + b what is a, what is b in the graph
import random
import streamlit as st

def dummy(n1, n2):
    return "still no answer"

if 'question_string' not in st.session_state:
    st.session_state['question_string'] = ''
if 'answer_function' not in st.session_state:
    st.session_state['answer_function'] = dummy
if 'answer_state' not in st.session_state:
    st.session_state['answer_state'] = "no answer yet"
if 'ans_f_info' not in st.session_state:
    st.session_state['ans_f_info'] = None
if 'answer' not in st.session_state:
    st.session_state['answer'] = None

def ranum():
    return random.randint(2, 15)
def rach():
    return random.choice([True, False])
def rali(eli):
    random.shuffle(eli)
    return eli

def q1():
    # number * 0 = ?
    li = [ranum(), 0]
    us = str("what is {} x {}? : ".format(*rali(li)))
    def ansfun(us, n):
        return int(us) == 0
    return us, ansfun, 0
def q2():
    # number * 1 = ?
    n = ranum()
    li = [n, 1]
    us = str("what is {} x {}? : ".format(*rali(li)))
    def ansfun(us, n):
        return n == int(us)
    return us, ansfun, n

def q3():
    # number + 0 = ?
    n = ranum()
    li = [n, 0]
    us = str("what is {} + {}? : ".format(*rali(li)))
    def ansfun(us, n):
        return n == int(us)
    return us, ansfun, n
def q4():
    # number - 1 = ?
    n = ranum()
    li = [n, -1]
    random.shuffle(li)
    us = str("what is {} - {}? : ".format(*li))
    def ansfun(us, li):
        return int(us) == li[0] - li[1]
    return us, ansfun, li
def q5():
    # number * -1 = ? *!
    n = ranum()
    li = [n, -1]
    us = str("what is {} x {}? : ".format(*li))
    def ansfun(us, li):
        return int(us) == li[0] * li[1]
    return us, ansfun, li
def q6():
    # number * 0 + number = ?
    pass
def q7():
    # number + 0 * number = ? *!
    pass
def q8():
    # number / 10 = ?
    pass
def q9():
    # number * 10 = ?
    pass
def q10():
    # number + number / number = ?
    pass

def main():
    questions = []
    questions.append(q1)
    questions.append(q2)
    questions.append(q3)
    questions.append(q4)
    questions.append(q5)

    # print('you have {} right answers out of {}'.format(len([x for x in scores if x]), len(scores)))
    
    st.title("The Maths Questionnaire")
    st.text("Random questions are generated every time you ask for a new question. This is basic practice for some maths reflexes you should have.")

    def change_question():
        question_text, answer_function, ans_f_info = random.choice(questions)()
        st.session_state['question_string'] = question_text
        st.session_state['answer_function'] = answer_function
        st.session_state['ans_f_info'] = ans_f_info
        st.session_state['answer_state'] = "no answer yet"
        st.session_state['answer'] = None
    if st.button('new question'):
        change_question()

    # now load the current question
    # st.text_area('question:', value=st.session_state['question_string'])
    ans_str = st.text_input(st.session_state['question_string'])
    
    but = st.button("press here to submit")
    if but:
        print(ans_str)
        st.session_state['answer_state'] = 'to compute'
        st.session_state['answer'] = int(ans_str)

    if st.session_state['answer_state'] != 'no answer yet':
        print("boom")
        answer_correct = st.session_state['answer_function'](st.session_state['answer'], st.session_state['ans_f_info'])
        corranss = ['Correct! Well done, cutie.', 'Correct! Well done.', 'Correct! Well done.', 'Correct! Well done.', 'Correct! Well done.', 'Correct! Well done.', 'Correct! Well done.', 'Correct! Well done.', 'Correct! Well done.', 'Correct! Well done.', 'Correct! Well done.']
        st.session_state['answer_state'] = random.choice(corranss) if answer_correct else 'Incorrect. Try again.'
    st.text_area('your answer is:', value=st.session_state['answer_state'])


if __name__ == "__main__":
    main()