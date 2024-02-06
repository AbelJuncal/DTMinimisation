:- dynamic thresholds/2,implicate/2,debug/0,var/2.
input(1,[
  [[0,3],[1,5],[0,5]],
  [[2,6],[3,7],[1,6]]
]).
input(2,[
    [[0,5],[0,10]],
    [[5,10],[3,10]]
  ]).
input(3,[
    [[2,9],[0,1],[5,8],[1,7]],
    [[1,5],[0,1],[8,10],[2,3]],
    [[3,7],[1,2],[2,4],[3,8]],
    [[1,6],[1,2],[2,4],[2,8]],
    [[1,10],[0,2],[1,5],[2,3]],
    [[2,9],[0,1],[5,9],[2,3]]
  ]).
msg(L) :- debug,!,repeat,(member(X,L),write(X),fail;nl,!).
msg(_).

inc_var(X,V) :- retract(var(X,W)),V is W+1,asserta(var(X,V)).
set_var(X,V) :- (retractall(var(X,_)),!;true),asserta(var(X,V)).

interv(A,A,[A]) :- !.
interv(A,B,[A|I]):- A<B, A1 is A+1, interv(A1,B,I).

get_thresholds(Xs,N,Ts) :-
    findall(I,(member(X,Xs),nth0(N,X,I)),Is),
    append(Is,Is2),
    list_to_ord_set(Is2,Ts).

split([A,B],[T|Ts],I) :- T<A, split([A,B],Ts,I).
split([A,B],[A,B|_],[A,B]).
split([A,B],[A,T|_],[A,T]) :- T<B.
split([A,B],[A,T|Ts],I) :- T<B, split([T,B],[T|Ts],I).

unfold(_,[],[]) :- !.
unfold(N,[I|Is],[J|Js]) :- thresholds(N,Ts),split(I,Ts,J),N1 is N+1,unfold(N1,Is,Js).

match_var([A,B],[C,D],[E,F]) :- B>=C, D>=A, sort([A,B,C,D],K),K=[E|_],last(K,F).
match_impl(X,Y,Z) :- append(Pre,[I|Suf],X), append(Pre,[J|Suf],Y), match_var(I,J,K), append(Pre,[K|Suf],Z),!.

add_implicate(X) :-
    implicate(X,_),! ; assertz(implicate(X,prime)).
mark_implicate(X) :-
    (retractall(implicate(X,_)),!;true), assertz(implicate(X,nonprime)).

match_one(_,[],0) :- !.
match_one(X,[Y|Ys],1) :- match_impl(X,Y,Z),!, 
    msg([X,' x ',Y,' -> ',Z]),
    (Z=X,!; mark_implicate(X)),  % if Z=X we don't mark X (Y was subsumed)
    (Z=Y,!; mark_implicate(Y)),  % if Z=Y we don't mark Y (X was subsumed)
    add_implicate(Z),match_one(X,Ys,_).
match_one(X,[_|Ys],N) :- match_one(X,Ys,N).

iteration([],0) :- !.
iteration([_],0) :- !.
iteration([X|Xs],K) :- msg(['Matching ',X]), match_one(X,Xs,N), iteration(Xs,M), K is N+M.

write_implicate([]):-!.
write_implicate([[A,B]|Xs]):-write(A),write(' '),write(B),write(' '),write_implicate(Xs).

min(Xs) :-
    (retractall(thresholds(_,_)),!;true),
    (retractall(implicate(_,_)),!;true),
    member(X0,Xs),!,
    length(X0,NVars),
    msg(['NVars = ',NVars]),
    NV1 is NVars-1,
    interv(0,NV1,Vars),
    repeat, (member(N,Vars), get_thresholds(Xs,N,Ts), assertz(thresholds(N,Ts)), fail; !),
    repeat, (member(X,Xs),unfold(0,X,Y),add_implicate(Y),fail; !),
    (debug,!,repeat, (implicate(W,_), write_implicate(W),nl,fail; !); true),
    repeat, (
        findall(XX,implicate(XX,prime),XXs),msg(['New iteration ---- ']),iteration(XXs,NN),NN=0,!),
    repeat,
    (implicate(YY,prime), write_implicate(YY),nl,fail; !).

% retrieves command line arguments Args and calls main(Args)

main_c :- unix(argv(Argv)),
        ( append(_PrologArgs, [--|AppArgs], Argv), !,
          main(AppArgs)
        ; main(Argv)).

% if no arguments, print help
main([]):- !, 
   write('mindt [-d] filename'),nl,
   write('      -d = debug'),nl,
   halt(0).

main(Args):-
    (Args=['-d',Fname|_],!,assert(debug)
    ;Args=[Fname|_]
    ),
    loadfile(Fname,Xs),
    min(Xs).

loadfile(Fname,L) :-
    open(Fname, read, Fd),
    read_string(Fd,"\n","",_,S1),number_string(N,S1),
    skiplines(Fd,N),
    read_terms(Fd,[],L),
    close(Fd).

read_terms(Fd,Clauses,ClausesN):-
	read_string(Fd,"\n","",End,String),
  normalize_space(string(Str2),String),
  string_length(Str2,SL),
  (SL=0,!,Clauses2=Clauses
  ; split_string(Str2," ","",L),
    maplist(number_string,L1,L),
    topairs(L1,Clause),
    Clauses2=[Clause|Clauses]
  ),
	(End= -1,ClausesN=Clauses2,!; read_terms(Fd,Clauses2,ClausesN)).

skiplines(_,0) :- !.
skiplines(Fd,N) :- read_string(Fd,"\n","",_,_),N1 is N-1, skiplines(Fd,N1).

topairs([],[]).
topairs([X,Y|L],[[X,Y]|L2]):-topairs(L,L2).