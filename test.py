def add_score(subject_score, student, subject, score):
    this_dict = subject_score
    this_dict.update({subject : score})
    student_dict = {}
    student_dict.update({student : this_dict}) 
    return student_dict

def calc_average_score(subject_score):
    mean_students = {}
    print(subject_score)
    for student, subject_list in subject_score.items():
        for subject, score in subject_list.items():
            # print(score)
            pass
        mean_students.update({student : '{:.2f}'.format(1)})

subject_score = { }
student = '65010001'
subject = 'python'
score = 50

add_score(subject_score, student, subject, score)
print(subject_score)
print(calc_average_score(subject_score))