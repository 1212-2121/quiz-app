import random
def read_questions(file_name):
    questions=[]
    with open(file_name,'r') as file:
        for line in file:
            parts=line.strip().split('|')
            if parts<3:
                continue
            question=parts[o]
            correct_answer=parts[1].lower()
            options=parts[2:]
            questions.append(question,correct_answer,options)


    return questions