% Facts about family relationships
parent(john, mary).
parent(john, steve).
parent(anne, mary).
parent(anne, steve).
parent(mary, lisa).
parent(steve, jacob).

% Rules to define different relationships
father(Father, Child) :-
    parent(Father, Child),
    male(Father).

mother(Mother, Child) :-
    parent(Mother, Child),
    female(Mother).

grandparent(Grandparent, Grandchild) :-
    parent(Grandparent, Parent),
    parent(Parent, Grandchild).

ancestor(Ancestor, Descendant) :-
    parent(Ancestor, Descendant).
ancestor(Ancestor, Descendant) :-
    parent(Ancestor, Parent),
    ancestor(Parent, Descendant).

% Facts about genders
male(john).
male(steve).
male(jacob).

female(anne).
female(mary).
female(lisa).
