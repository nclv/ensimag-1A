/*
uint8_t val_binaire(uint8_t b15, uint8_t b14, uint8_t b13, uint8_t b12,
                    uint8_t b11, uint8_t b10, uint8_t b9, uint8_t b8,
                    uint8_t b7, uint8_t b6, uint8_t b5, uint8_t b4,
                    uint8_t b3, uint8_t b2, uint8_t b1, uint8_t b0)
{
    return
      (b15 << 15) | (b14 << 14) | (b13 << 13) | (b12 << 12) | (b11 << 11) | (b10 << 10) | (b9 << 9) | (b8 << 8)
      | (b7 << 7) | (b6 << 6) | (b5 << 5) | (b4 << 4) | (b3 << 3) | (b2 << 2) | (b1 << 1) | b0;
}
*/

    .text
    .globl val_binaire
/* uint8_t val_binaire(uint8_t b7, uint8_t b6, uint8_t b5, uint8_t b4,
     uint8_t b3, uint8_t b2, uint8_t b1, uint8_t b0); */
val_binaire:
/*
Contexte ??
*/
    ret

