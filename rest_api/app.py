#!/user/bin/python3

import sqlite3
from flask import Flask, request, json

app = Flask(__name__)


def initialize_database():
    """
    Creates a new election database and the necessary tables.
    """
    conn = sqlite3.connect('election.db')

    conn.execute('''CREATE TABLE USERS
                    (USER_ID INT PRIMARY KEY NOT NULL,
                     Q1 BOOLEAN NOT NULL,
                     Q2 BOOLEAN NOT NULL,
                     Q3 BOOLEAN NOT NULL,
                     Q4 BOOLEAN NOT NULL,
                     Q5 BOOLEAN NOT NULL,
                     Q6 BOOLEAN NOT NULL,
                     Q7 BOOLEAN NOT NULL,
                     Q8 BOOLEAN NOT NULL,
                     Q9 BOOLEAN NOT NULL,
                     Q10 BOOLEAN NOT NULL);''')

    conn.execute('''CREATE TABLE CANDIDATES
                    (CANDIDATE_ID INT PRIMARY KEY NOT NULL,
                     NAME VARCHAR(50) NOT NULL,
                     POSITION VARCHAR(100) NOT NULL,
                     Q1 BOOLEAN NOT NULL,
                     Q2 BOOLEAN NOT NULL,
                     Q3 BOOLEAN NOT NULL,
                     Q4 BOOLEAN NOT NULL,
                     Q5 BOOLEAN NOT NULL,
                     Q6 BOOLEAN NOT NULL,
                     Q7 BOOLEAN NOT NULL,
                     Q8 BOOLEAN NOT NULL,
                     Q9 BOOLEAN NOT NULL,
                     Q10 BOOLEAN NOT NULL);''')

    conn.execute('''CREATE TABLE QUESTIONS
                    (QUESTION_ID INT PRIMARY KEY NOT NULL,
                     Q1 VARCHAR(100) NOT NULL,
                     Q2 VARCHAR(100) NOT NULL,
                     Q3 VARCHAR(100) NOT NULL,
                     Q4 VARCHAR(100) NOT NULL,
                     Q5 VARCHAR(100) NOT NULL,
                     Q6 VARCHAR(100) NOT NULL,
                     Q7 VARCHAR(100) NOT NULL,
                     Q8 VARCHAR(100) NOT NULL,
                     Q9 VARCHAR(100) NOT NULL,
                     Q10 VARCHAR(100) NOT NULL);''')

    conn.close()

def insert_candidates():
    """
    Inserts test candidates into the database.
    """
    conn = sqlite3.connect('election.db')
    conn.execute('''INSERT INTO CANDIDATES (CANDIDATE_ID, NAME, POSITION, Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10)
                    VALUES
                    (1, "Florence Johnson", "President", 2, 1, 2, 2, 1, 2, 1, 1, 1, 2)''') 
    conn.execute('''INSERT INTO CANDIDATES (CANDIDATE_ID, NAME, POSITION, Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10)
                    VALUES
                    (2, "Edward Vargas", "President", 1, 1, 1, 1, 2, 2, 1, 2, 2, 2)''') 
    conn.execute('''INSERT INTO CANDIDATES (CANDIDATE_ID, NAME, POSITION, Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10)
                    VALUES
                    (3, "Jessica Lee", "Senator", 2, 1, 1, 2, 1, 2, 1, 2, 1, 2)''') 
    conn.execute('''INSERT INTO CANDIDATES (CANDIDATE_ID, NAME, POSITION, Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10)
                    VALUES
                    (4, "Angela Newton", "Senator", 1, 1, 1, 2, 1, 1, 2, 2, 2, 2)''')
    conn.execute('''INSERT INTO CANDIDATES (CANDIDATE_ID, NAME, POSITION, Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10)
                    VALUES
                    (5, "Muhammad Clark", "Representative", 2, 2, 2, 1, 1, 2, 2, 1, 1, 1)''')
    conn.execute('''INSERT INTO CANDIDATES (CANDIDATE_ID, NAME, POSITION, Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10)
                    VALUES
                    (6, "Leon Crawford", "Representative", 1, 1, 2, 2, 2, 1, 2, 1, 2, 1)''')
    conn.execute('''INSERT INTO CANDIDATES (CANDIDATE_ID, NAME, POSITION, Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10)
                    VALUES
                    (7, "Marcus Anderson", "Governor", 2, 2, 1, 1, 1, 2, 2, 2, 1, 2)''')
    conn.execute('''INSERT INTO CANDIDATES (CANDIDATE_ID, NAME, POSITION, Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10)
                    VALUES
                    (8, "Isabella Hughes", "Governor", 1, 1, 1, 1, 1, 1, 1, 2, 2, 2)''')
    conn.commit()
    conn.close()

def insert_questions():
    """
    Inserts questions into the database.
    """
    conn = sqlite3.connect('election.db')
    conn.execute('''INSERT INTO QUESTIONS 
                    (QUESTION_ID, Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10) VALUES 
                    (1,
                     "Should the government subsidize alternative energy?",
                     "Do you think we should legalize marijuana?",
                     "Do you support the government funding space exploration?",
                     "Should government increase spending on public transit?",
                     "Do you support universal healthcare for all citizens?",
                     "Do we need to do more to secure our borders?",
                     "Should we decrease government spending on defense?",
                     "Do you think ISPs should be required to treat all data on the Internet equally? ",
                     "Should there be more restrictions on the purchase of guns?",
                     "Do we need to do more to decrease the influence of corporations in politics?");''')
    conn.commit()
    conn.close()

def get_user(user_id):
    """
    Gets user from the database using the `user_id`.
    """
    conn = sqlite3.connect('election.db')
    sql_query = "SELECT USER_ID, Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10 from USERS where USER_ID = {}".format(user_id)
    cursor = conn.execute(sql_query)
    user = {}
    for row in cursor:
        user['user_id'] = row[0]
        user['q1'] = row[1]
        user['q2'] = row[2]
        user['q3'] = row[3]
        user['q4'] = row[4]
        user['q5'] = row[5]
        user['q6'] = row[6]
        user['q7'] = row[7]
        user['q8'] = row[8]
        user['q9'] = row[9]
        user['q10'] = row[10]
    conn.close()
    return user

def set_user_answer(user_id, answer):
    """
    Sets the user's answer.
    """
    def _set_user_question(user_id, answer, question):
        """
        Updates the user's answer for the specified question.
        """
        conn = sqlite3.connect('election.db')
        question = 'Q{}'.format(question)
        sql_query = "UPDATE USERS set {} = {} where USER_ID = {}".format(question, answer, user_id)
        conn.execute(sql_query)
        conn.commit()
        conn.close()

    user = get_user(user_id)
    updated_q = None
    for q in range(1, len(user)):
        question = 'q{}'.format(q)
        if not user[question]:
            updated_q = q
            break

    if not updated_q:
        return user
    else:
        _set_user_question(user_id, answer, updated_q)
        user = get_user(user_id)
        return user

def create_user():
    """
    Creates and returns a new user.
    """
    conn = sqlite3.connect('election.db')
    sql_query = "SELECT COUNT(*) FROM USERS"
    cursor = conn.execute(sql_query)
    user_id = None
    for row in cursor:
        user_id = row[0] + 1
    sql_query = '''INSERT INTO USERS (USER_ID, Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10) 
                   VALUES 
                   ({}, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)'''.format(user_id)
    conn.execute(sql_query) 
    conn.commit()
    conn.close()
    return get_user(user_id)

def get_next_question(user):
    """
    Gets the next question to ask the user. If there are no questions
    left to answer, then this function returns None.
    """
    next_q = None
    for q in range(1, len(user)):
        question = 'q{}'.format(q)
        if not user[question]:
            next_q = q
            break

    if not next_q:
        return None

    conn = sqlite3.connect('election.db')
    sql_query = 'SELECT QUESTION_ID, Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10 from QUESTIONS'
    cursor = conn.execute(sql_query)
    for row in cursor:
        return row[next_q]

def generate_results(user):
    """
    Compares the user's answers with the canidate's answers and returns
    how much they agree with each candidates on the issues.
    """
    conn = sqlite3.connect('election.db')
    sql_query = "SELECT CANDIDATE_ID, Name, Position, Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10 from CANDIDATES"
    cursor = conn.execute(sql_query)

    results = []
    for row in cursor:
        agree = 0
        for q in range(3, len(row)):
            question = 'q{}'.format(q-2)
            if row[q] == user[question]:
                agree += 1
        results.append({'name': row[1], 'position': row[2], 'score': agree})

    conn.close()

    num_q = len(row) - 3
    str_results = 'This is how much you agree with each candidate on this issues...\n'
    for p in results:
        str_results += '{} ({}): {:.0%}\n'.format(p['name'], p['position'], p['score'] / num_q)

    str_results += 'Thanks for taking the time to figure out how you want to vote. We hope this was helpful!\n'

    return str_results

@app.route('/users', methods = ['POST'])
def conversation_action():
    """
    Sets the answer for the current question and gets the next question.
    If all questions have been answered, then it calculates and returns
    the ballot profile of the user.
    """
    user_id = request.json['user_id']
    answer = request.json['answer']
    
    if user_id:
        user = set_user_answer(user_id, answer)
    else:
        user = create_user()
  
    print(user)

    next_q = get_next_question(user)
    if next_q:
        return json.dumps({"user_id": user['user_id'], "response": next_q})
    else:
        profile = generate_results(user)
        return json.dumps({"user_id": user['user_id'], "response": profile})

@app.route('/candidates/<int:candidate_id>/<int:question_num>', methods = ['GET'])
def question_action(candidate_id, question_num):
    """
    Returns whether or not a candidate supports an issue.
    """
    conn = sqlite3.connect('election.db')
    sql_query = "SELECT Q{} FROM CANDIDATES WHERE CANDIDATE_ID = {}".format(question_num, candidate_id)
    cursor = conn.execute(sql_query)
    for row in cursor:
        answer = row[0]
    return json.dumps({"answer": answer})

if __name__ == '__main__':
    # initialize_database()
    # insert_candidates()
    # insert_questions()
    app.run(host="0.0.0.0", port=80)
