    .text
/*
uint32_t x, y;
*/
/*

uint32_t mult_simple(void)
{
    res = 0;
    while (y != 0) {
        res = res + x;
        y--;
    }
    return res;
}
*/
    .globl mult_simple
mult_simple:
    ret

/*
uint32_t mult_egypt(void)
{
    uint32_t res = 0;
    while (y != 0) {
        if (y % 2 == 1) {
            res = res + x;
        }
        x = x << 1 ;
        y = y >> 1;
    }
    return res;
}
*/
    .globl mult_egypt
mult_egypt:
/* Contexte : ??*/
    ret

/*
uint32_t mult_native(void)
{
    return x*y;
}
*/
    .globl mult_native
mult_native:
    ret


    .data
/* uint32_t res; */
