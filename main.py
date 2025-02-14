import random
def read_questions(file_name):
    questions=[]
    with open(file_name,'r') as file:
        for line in file:
            parts=line.strip().split('|')


