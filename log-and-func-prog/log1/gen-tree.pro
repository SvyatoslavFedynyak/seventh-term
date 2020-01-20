% list of members

male(svyatoslav). % me
male(volodymyr_br). % brother
male(roman). % father
male(volodymyr_gr). % grandparent
male(stephan). % grandparent
female(oksana). % mother
female(galyna_gr). % grandparent
female(iryna_gr). % grandparent
female(galyna_au). % aunt
female(iryna_co). % cousin
female(natalia). % cousin

% relationshipp parent (child, parent).

parent(svyatoslav, roman).
parent(volodymyr_br, roman).
parent(svyatoslav, oksana).
parent(volodymyr_br, oksana).

parent(oksana, volodymyr_gr).
parent(oksana, galyna_gr).
parent(roman, stephan).
parent(roman, iryna_gr).

parent(galyna_au, stephan).
parent(galyna_au, iryna_gr).
parent(iryna_co, galyna_au).
parent(natalia, galyna_au).

% rules
child(Parent,Child) :- parent(Child, Parent).

mother(Child, Mother) :- female(Mother), parent(Child, Mother).
father(Child, Father) :- male(Father), parent(Child, Father).
son(Child, Father) :- male(Child), parent(Child, Father).
daughter(Child, Mother) :- female(Child), parent(Child, Mother).

sisOrBrother(Person1, Person2) :- parent(Person1, X), parent(Person2, X), Person1 \= Person2.
sister(Person, Sister) :- female(Sister), sisOrBrother(Person, Sister).
brother(Person, Brother) :- male(Brother), sisOrBrother(Person, Brother).

uncle(Child, Uncle) :- parent(Child, Parent), brother(Parent, Uncle).
aunt(Child, Aunt) :- parent(Child, Parent), sister(Parent, Aunt).

ancestor(Young, Old) :- parent(Parent, Old), parent(Young, Parent).
descendant(Old, Young) :- ancestor(Young, Old).

grandFather(Child, Grand) :- ancestor(Child, Grand), male(Grand).
grandMother(Child, Grand) :- ancestor(Child, Grand), female(Grand).

grandDaughter(Child, Grand) :- ancestor(Child, Grand), male(Child).
grandSon(Child, Grand) :- ancestor(Child, Grand), female(Child).

cousin(Person1, Person2) :- 
    aunt(Person1, X), parent(Person2, X), Person1 \= Person2;
    aunt(Person2, X), parent(Person1, X), Person1 \= Person2;
    uncle(Person2, X), parent(Person2, X), Person1 \= Person2;
    uncle(Person1, X), parent(Person1, X), Person1 \= Person2.

