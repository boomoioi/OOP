def add_score(subject_score, subject, score):
    subject_score.update({subject: score})
    return subject_score

def calc_average_score(subject_score):
    count = 0
    sum = 0
    for val in subject_score.values():
        count += 1
        sum += val 
    return "{:.2f}".format(sum/count)