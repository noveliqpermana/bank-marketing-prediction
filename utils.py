def cardinality(X):
    '''Fungsi ini berguna untuk melakukan handling cardinality serta sekaligus menambah indikator untuk kolom pdays dan mengubah nilai -1'''
    # lakukan copy agar tidak mempengaruhi data asli
    X = X.copy()

    # buat list untuk menampung data
    job_list = []

    # lakukan for looping untuk kategorisasi job
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

    # masukkan data ke kolom job
    X['job'] = job_list

    # buat indikator untuk leads yang tidak dihubungi 
    X['was_contacted'] = (X['pdays'] != -1).astype(int)

    # ganti nilai -1 menjadi 0
    X['pdays'] = X['pdays'].where(X['pdays'] != -1, 0) 

    # return data baru yang sudah di-handling
    return X