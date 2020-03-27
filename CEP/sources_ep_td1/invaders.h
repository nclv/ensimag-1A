#ifndef __SPRITE_H__
#define __SPRITE_H__

#include <stdint.h>

/* object type definition used for aliens, spaceship and laser */
typedef struct object_t {
   uint32_t alive;
   uint32_t period;
   uint32_t deadline;
   int x, y;
   int dx, dy;
   uint32_t *pattern;
   uint32_t color;
   uint32_t bg[8][8];           /* background */
   int ax, ay;
} object_t;

/* Type Etat pour implementer la mécanique du jeu sous forme de machine à états */
typedef struct state_t {
   int dx;
   int dy;
   int next_state;
} state_t;

/*
 * definition of functions' prototype
 * ---------------------------------------------------------------------------
 */
int  read_pixel(int x, int y);
void write_pixel_scaling(int pixel, int x, int y);
void clear_screen(uint32_t color);
void initialize(void);
void display_pattern_line(uint32_t m, int x, int y, uint32_t color);
void display_pattern(uint32_t pattern[8], int x, int y, uint32_t color);
void display_sprite(object_t *object);
void display_timer(void);           // DEBUG function

#endif                          /* __SPRITE_H__ */
