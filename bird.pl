% Facts about birds and their ability to fly
bird(canary).
bird(sparrow).
bird(ostrich).
bird(penguin).

can_fly(canary).
can_fly(sparrow).

% Rules to determine if a bird can fly
flies(Bird) :-
    bird(Bird),
    can_fly(Bird).

% Queries
% Example query to check if a canary can fly
% ?- flies(canary).
