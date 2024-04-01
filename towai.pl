% Define the predicate to solve the Towers of Hanoi problem
hanoi(N) :-
    move(N, left, middle, right).

% Define the base case: moving 0 disks requires no action
move(0, _, _, _) :- !.

% Define the recursive case for moving N disks
move(N, Start, Middle, End) :-
    N > 0,
    N1 is N - 1,
    move(N1, Start, End, Middle),
    write('Move disk '), write(N), write(' from '), write(Start), write(' to '), write(End), nl,
    move(N1, Middle, Start, End).

% Example usage:
% To solve the Towers of Hanoi problem with 3 disks:
% ?- hanoi(3).
