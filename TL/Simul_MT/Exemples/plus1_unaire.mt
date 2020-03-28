// "plus 1" ; donnée codée en unaire (0 : 'B', 1 : '1', 2 : '11', 3 : '111'...)
// 
// Algo : trivial : on recule (sauf pour 0) et on place un '1' !

& 1

@ q0

$ f

q0 B : f 1 S
q0 1 : f 1 G
f B : f 1 S   // note : on s'arrête sur (f, 1)
