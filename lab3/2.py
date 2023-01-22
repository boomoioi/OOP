def add_score(subject_score, student, subject, score):
    if subject_score.get(student):
        subject_score[student].update({subject : score})
    else:
        subject_score.update({student: {subject : score}})
    return subject_score

def calc_average_score(subject_score):
    ans = {}
    for student, stat in subject_score.items():
        count = 0
        sum = 0
        for val in stat.values():
            count += 1
            sum += val 
        ans.update({student : "{:.2f}".format(sum/count)})
    return ans
subject_score = { '65010001' : { 'python' : 50 } }
subject = 'cal'
score = 60
student = '65010001'

print(add_score(subject_score, student, subject, score))
print(calc_average_score(subject_score))