from arrays import Array2D
# Open the text file for reading.
grade_file = open( "grade.txt", "r" )
# Extract the first two values which indicate the size of the array.
num_students = int( grade_file.readline() )
num_exams = int( grade_file.readline() )

# Create the 2 -D array to store the grades.
exam_grades = Array2D( num_students, num_exams )
# Extract the grades from the remaining lines.
i = 0
for student in grade_file :
    grades = student.split()
    for j in range( num_exams ):
        exam_grades[i,j] = int( grades[j] )
    i += 1
# Close the text file.
grade_file.close()

# Compute each student's average exam grade.
for i in range( num_students ) :
# Tally the exam grades for the ith student.
    total = 0
    for j in range( num_exams ) :
        total += exam_grades[i,j]
# Compute average for the ith student.
    exam_avg = total / num_exams
    print( "{:2d}: {:6.2f}".format(i+1, exam_avg) )

# Add 2 points to every grade.
for row in range(exam_grades.num_rows()):
    for col in range(exam_grades.num_cols()):
        grade = exam_grades[row,col]
        grade = grade + 2
        exam_grades[row,col] = grade