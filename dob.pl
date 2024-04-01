% Define facts for name and date of birth
dob(john, date(1990, 5, 15)).
dob(sarah, date(1985, 10, 25)).
dob(mike, date(1978, 3, 8)).
dob(lisa, date(1995, 8, 12)).

% Predicate to retrieve date of birth for a given name
date_of_birth(Name, DateOfBirth) :-
    dob(Name, DateOfBirth).
