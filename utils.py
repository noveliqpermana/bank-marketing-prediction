def cardinality(X):
    X = X.copy()
    job_list = []

    for i in X['job']:
        if i in ['unemployed', 'student', 'retired']:
            job_list.append('not_working')
        elif i in ['admin.', 'management', 'technician']:
            job_list.append('white_collar')
        elif i in ['blue-collar', 'services', 'housemaid']:
                    job_list.append('blue_collar')
        elif i in ['entrepreneur', 'self-employed']:
                            job_list.append('self_employed')
        else:
            job_list.append(i)

    X['was_contacted'] = (X['pdays'] != -1).astype(int)
    X['pdays'] = X['pdays'].where(X['pdays'] != -1, 0) 
    X['job'] = job_list

    return X