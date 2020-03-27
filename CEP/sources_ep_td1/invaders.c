#define ENV_QEMU
#include "invaders.h"
#include "cep_platform.h"

#include <stdint.h>

#ifdef ENV_QEMU
#include <string.h>
#include <stdio.h>
#endif

/*
 * definition of macros
 * ---------------------------------------------------------------------------
 */
#if 0 /* Inherit display resolution from cep_platform.h */
#define DISPLAY_WIDTH  1920     /* display width resolution */
#define DISPLAY_HEIGHT 1080     /* display height resolution */
#endif
#define N_OBJECTS 7             /* displayed objects (aliens, laser, spaceship) */

// #SCALING
#define DISPLAY_SCALE  4

#define MAX_X 39
/*
 * definition of global variables
 * ---------------------------------------------------------------------------
 */

/* definition of bitmap for each line in the 8x8 pattern */
static uint32_t sprite_sship[8]  = { 0x00, 0x3c, 0x7e, 0xff, 0xff, 0xe7, 0xc3, 0xc3 };
static uint32_t sprite_laser[8]  = { 0x18, 0x18, 0x18, 0x18, 0x18, 0x18, 0x18, 0x18 };
static uint32_t sprite_alien1[8] = { 0xc3, 0x3c, 0x5a, 0xff, 0xff, 0x81, 0x42, 0x24 };
static uint32_t sprite_alien2[8] = { 0xc3, 0x3c, 0x5a, 0xff, 0xff, 0xa5, 0xa5, 0x5a };
static uint32_t sprite_alien3[8] = { 0x42, 0x24, 0x3c, 0x5a, 0xff, 0xbd, 0x81, 0x42 };
static uint32_t sprite_alien4[8] = { 0x81, 0x42, 0x3c, 0x5a, 0x5a, 0x3c, 0x42, 0x81 };
static uint32_t sprite_alien5[8] = { 0x41, 0x22, 0x3e, 0x6b, 0x49, 0x7f, 0x3e, 0x55 };

/* sprite objects */
object_t object[N_OBJECTS] = {
   /* blue spaceship */
   {1, 3, 1, 18, 21,  0, 0, sprite_sship,  0x0000FF, {[0 ... 7]={0}}, 0, 0},
   /* white laser */
   {0, 1, 1, 18,  0,  0, 0, sprite_laser,  0xFFFFFF, {[0 ... 7]={0}}, 0, 0},
   /* green alien */
   {1, 4, 1, 10,  0, -1, 0, sprite_alien1, 0x00FF00, {[0 ... 7]={0}}, 0, 0},
   /* red alien */
   {1, 4, 1, 18,  0, -1, 0, sprite_alien2, 0xFF0000, {[0 ... 7]={0}}, 0, 0},
   /* magenta alien */
   {1, 4, 1, 26,  0, -1, 0, sprite_alien3, 0xFF00FF, {[0 ... 7]={0}}, 0, 0},
   /* yellow alien */
   {1, 4, 1, 14,  2, -1, 0, sprite_alien4, 0xFFFF00, {[0 ... 7]={0}}, 0, 0},
   /* cyan alien */
   {1, 4, 1, 22,  2, -1, 0, sprite_alien5, 0x00FFFF, {[0 ... 7]={0}}, 0, 0}
};

/* Tableau d'états pour la mécanique du jeu */
state_t state[5] = {
   {0, 1, 1},
   {0, 1, 2},
   {1, 0, 3},
   {0, 1, 4},
   {-1, 0, 1}
};

/* pointers to the peripherals base address */
/* Video Memory */
static volatile uint32_t *img = (volatile uint32_t *) VRAM_OFFSET;

/*
 * main program
 * ---------------------------------------------------------------------------
 */
int main(void)
{
   /* declaration of local variables */
   uint32_t i;
   uint32_t push_state, led_state, alien_state, edge_reached;
   uint32_t n_aliens;
   object_t *spaceship, *laser;

 init:
   /* initialization stage */
   push_state = 0;              /* no button pressed at beginning */
   led_state = 0;               /* initial value displayed on leds */
   alien_state = 0;             /* state of alien in a line */
   edge_reached = 0;            /* no edge reached at beginning */
   n_aliens = N_OBJECTS - 2;    /* number of displayed aliens */
   spaceship = &object[0];      /* spaceship is the first declared object */
   laser = &object[1];          /* laser is the second declared object */
   initialize();

   /* display stage */
   while (1) {
      edge_reached = 0;

      /* decrease deadline of alive objects */
      for (i = 0; i < N_OBJECTS; i++) {
         if (object[i].alive)
            object[i].deadline--;
      }

      /* display all alive objects */
      for (i = 0; i < N_OBJECTS; i++) {
         if (object[i].alive)
            display_sprite(&object[i]);
      }

      /* determine new positions of all alive objects */
      for (i = 0; i < N_OBJECTS; i++) {
         /* update object state when deadline is reached */
         if (object[i].alive && object[i].deadline == 0) {
            /* reinitialize the object deadline to period */
            object[i].deadline = object[i].period;
            /* determine new position and manage screen edges */
            object[i].x += object[i].dx;
            if (object[i].x < 0)
               object[i].x = 0;
            if (object[i].x > MAX_X)
               object[i].x = MAX_X;
            object[i].y += object[i].dy;
            /* test if an edge of the screen was reached by an alien */
            if (i >= 2 && (object[i].x == 0 || object[i].x == MAX_X))
               edge_reached = 1;
            /* store background of the next position */
            if (i > 1 && object[i].y >= spaceship->y) {
               clear_screen(0xFF);                                                                                                                                                                      /* blue screen */
               timer_set_and_wait(TIMER_FREQ, 1000);
               initialize();
            }
         }
      }

      /* test if alien is hit by an alive laser */
      if (laser->alive) {
         for (i = 2; i < N_OBJECTS; i++) {
            if (object[i].alive && laser->x == object[i].x && laser->y == object[i].y) {
               n_aliens--;
               object[i].alive = 0;
               laser->alive = 0;
               if (n_aliens == 0) {
                  /* no more aliens */
                  spaceship->alive = 0;
                  clear_screen(0xFF00);                                                                                                                                                                 /* yellow screen */
                  timer_set_and_wait(TIMER_FREQ, 1000);
                  clear_screen(0xFF0000);                                                                                                                                                               /* red screen */
               } else {
                  display_sprite(&object[i]);
                  display_sprite(laser);
               }
            }
         }
      }

      /* when an alien reaches a screen edge, the group of aliens is moved */
      if (edge_reached) {
         for (i = 2; i < N_OBJECTS; i++) {
            object[i].dx = state[alien_state].dx;
            object[i].dy = state[alien_state].dy;
         }
         alien_state = state[alien_state].next_state;

      }

      /* laser disappears when it reaches the screen top */
      if (laser->alive && laser->y == 0) {
         laser->alive = 0;
         display_sprite(laser);
      }

      /* manage push buttons */
      push_state = push_button_get();
      // if we won, press fire to restart
      if ((n_aliens == 0)
          && (push_state & 0x4)) {
         goto init;
      }
      if ((spaceship->deadline == 1)
          || (n_aliens == 0)) {
         spaceship->dx = 0;
         if (push_state & 0x1)
            /* to the right */
            spaceship->dx = 1;
         if (push_state & 0x2)
            /* to the left */
            spaceship->dx = -1;
         if (push_state & 0x4) {
            /* fire a laser */
            if (!laser->alive) {
               laser->alive = 1;
               laser->dx = 0;
               laser->dy = -1;
               laser->x = spaceship->x;
               laser->y = spaceship->y - 1;
               laser->deadline = laser->period;
            }
         }
      }

      /* manage leds' state */
      led_set(led_state);
      led_state++;
      timer_set_and_wait(TIMER_FREQ, 4);
   }
}

/*
 * definition of functions
 * ---------------------------------------------------------------------------
 */

/* function to read a pixel from a (x,y) position of video framebuffer */
int read_pixel(int x, int y)
{
   unsigned int real_y = y * DISPLAY_WIDTH * DISPLAY_SCALE;
   unsigned int real_x = x * DISPLAY_SCALE;
   return img[real_y + real_x];
}

void write_pixel_scaling(int pixel, int x, int y)
{
   unsigned int i, j;

   for (i = 0; i < DISPLAY_SCALE; ++i) {
      for (j = 0; j < DISPLAY_SCALE; ++j) {
         unsigned int real_y = y * DISPLAY_SCALE + i;
         unsigned int real_x = x * DISPLAY_SCALE + j;

         img[real_y * DISPLAY_WIDTH + real_x] = pixel;
      }
   }
}

void *memset_32b(volatile uint32_t * dest, uint32_t c, uint32_t n)
{
   volatile uint32_t *p = dest;
   while (n-- > 0) {
      *(volatile uint32_t *) dest++ = c;
   }
   return (void *) p;
}

/* function to clear entire screen to the selected color */
void clear_screen(uint32_t color)
{
   memset_32b(img, color, DISPLAY_WIDTH * DISPLAY_HEIGHT);
}

/* function to initialize all objects */
void initialize()
{
   uint32_t i, dx, dy;
   clear_screen(0x0);           /* black screen */
   for (i = 0; i < N_OBJECTS; i++) {
      if (i == 1) {
         /* laser */
         object[i].alive = 0;
         object[i].period = 1;
      } else {
         /* spaceship or aliens */
         object[i].alive = 1;
         if (i == 0)
            /* spaceship */
            object[i].period = 3;
         else
            /* aliens */
            object[i].period = 4;
      }
      object[i].deadline = 1;
      if (i > 1) {
         /* aliens */
         if (i > 4) {
            /* alien4 or alien5 */
            object[i].y = 3;    /* 3rd line */
            object[i].x = 6 + (i - 4) * 8;
         } else {
            /* alien1, alien2 or alien3 */
            object[i].y = 1;    /* 1st line */
            object[i].x = 10 + (i - 2) * 8;
         }
         object[i].dx = -1;
         object[i].dy = 0;
      }
      object[i].ax = -1;
      object[i].ay = -1;

      /* initialization of object background considering the last one */
      for (dx = 0; dx < 8; dx++)
         for (dy = 0; dy < 8; dy++)
#ifdef ENV_QEMU
            object[i].bg[dx][dy] = read_pixel(((object[i].x) << 3) + dx, ((object[i].y) << 3) + dy);
#else
            object[i].bg[dx][dy] = 0;
#endif
   }
}

/* function to display the 8 pixels of a pattern line */
void display_pattern_line(uint32_t m, int x, int y, uint32_t color)
{
   int i;

   for (i = 0; i < 8; i++) {
      int new_color = ((m & 1) == 1) ? color : 0;
      m = m >> 1;
      write_pixel_scaling(new_color, x + i, y);
   }
}

/* function to display an 8x8 object considering the last background */
void display_pattern(uint32_t pattern[8], int x, int y, uint32_t color)
{
   int i;

   for (i = 0; i < 8; i++)
      display_pattern_line(pattern[i], x, y + i, color);
}

/* function to display an 8x8 object (spaceship, laser or alien) */
void display_sprite(object_t * object)
{
   int dx, dy;

   if ((object->ax > -1 && object->ay > -1) && (object->x != object->ax || object->y != object->ay || !object->alive)) {
      for (dx = 0; dx < 8; dx++) {
         for (dy = 0; dy < 8; dy++) {
            write_pixel_scaling(object->bg[dx][dy], ((object->ax) << 3) + dx, ((object->ay) << 3) + dy);
            if (!object->alive)
#ifdef ENV_QEMU
               object->bg[dx][dy] = read_pixel(((object->x) << 3) + dx, ((object->y) << 3) + dy);
#else
               object->bg[dx][dy] = 0;
#endif
         }
      }
   }

   object->ax = object->x;
   object->ay = object->y;

   if (object->alive)
      display_pattern(object->pattern, (object->x) << 3, (object->y) << 3, object->color);
}
