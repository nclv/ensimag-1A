/*
struct rect_t double_rect(struct rect_t r)
{
    return (struct rect_t){r.x, r.y, r.dx * 2, r.dy * 2};
}
*/
    .text
    .globl double_rect
/* Contexte :
    Fonction feuille : rien à faire sur la pile, ra non modifié
    Agrégat > 64 en valeur de retour => appelante a réservé une place dans sa pile
                                        et a0 (paramètre implicite) pointe dessus
    Agrégat > 64 en paramètre        => appelante a réservé une place dans sa pile
                                        et a1 (et non a0 car réservé pour la valeur
                                        de retour) pointe dessus
*/
double_rect:
    lhu  a4, 10(a1)
    lhu  a3,  8(a1)
    lw   a2,  4(a1)
    lw   a1,  0(a1)
    slli a3, a3, 1
    slli a4, a4, 1
    sh   a4, 10(a0)
    sh   a3,  8(a0)
    sw   a2,  4(a0)
    sw   a1,  0(a0)
    ret
