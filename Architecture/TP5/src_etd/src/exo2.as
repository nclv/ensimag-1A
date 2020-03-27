xor r0,r0
xor r2,r2
li 1,r3

attente:
 ld 0x0010, r0
 and r0,r0 #MAJ du flags z
 jz fonction 
 jmp attente 

fonction:
 add r3,r2
 st r2, 0x0001
 jmp attente
