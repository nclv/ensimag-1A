/*
uint32_t age(uint32_t annee_naissance)
{
    uint32_t age;
    age = 2020 - annee_naissance;
    return age;
}
*/

    .text
    .globl age
    /* uint32_t age(uint32_t annee_naissance) */

/* Contexte imposé :
    annee_naissance : registre a0
    uint32_t age    : pile à sp+0
*/

age:
/* A compléter */
    ret
