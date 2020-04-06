import csv
import os

inputFileName = "responses.csv"
outputFileName = os.path.splitext(inputFileName)[0] + "-renamed.csv"
qfile = 'questions.csv'


with open(inputFileName, newline='') as inFile, open(outputFileName, 'w', newline='') as outfile:
    r = csv.reader(inFile)
    w = csv.writer(outfile)

    old_header = next(r, None)  # skip the first row from the reader, the old header
    # convert column names below
    new_header = ['time', 'email', 'name', 'school', 'year', 'programme', 'origin']
    # for the rest, rename to q1, q2, ... 
    questions = []
    for i, qs in enumerate(old_header[len(new_header):], start=1):
        new_header.append(f'q{i}')
        questions.append((f'q{i}', qs))

    # write new header
    w.writerow(new_header)

    # copy the rest
    for row in r:
        try:
          w.writerow(row)
        except:
            print(row)

    # keep question name mappings in a separate csv file
    with open(qfile, 'w', newline='') as qf:
        qw = csv.writer(qf)
        # header
        qw.writerow(['id', 'question'])
        for qrow in questions:
            qw.writerow([qrow[0], qrow[1]])

