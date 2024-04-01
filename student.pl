% Define facts for students, teachers, subjects, and corresponding codes
student(john, 101).
student(sarah, 102).
student(mike, 103).

teacher(mary, 201).
teacher(david, 202).
teacher(emily, 203).

subject(math, 301).
subject(science, 302).
subject(english, 303).

% Define facts for student-teacher relationships
teaches(mary, math).
teaches(david, science).
teaches(emily, english).

% Predicate to retrieve the subject code for a given teacher
subject_code_for_teacher(Teacher, SubjectCode) :-
    teacher(Teacher, TeacherCode),
    teaches(Teacher, Subject),
    subject(Subject, SubjectCode).

% Predicate to retrieve the teacher code for a given student
teacher_code_for_student(Student, TeacherCode) :-
    student(Student, StudentCode),
    teaches(Teacher, _),
    teacher(Teacher, TeacherCode),
    teaches(Teacher, Subject),
    student(_, SubjectCode),
    student(Student, SubjectCode).

% Predicate to retrieve the student code for a given subject
student_code_for_subject(Subject, StudentCode) :-
    subject(Subject, SubjectCode),
    student(Student, StudentCode),
    teaches(_, Subject).
