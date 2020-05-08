#include <stdio.h>
#include <inttypes.h>

struct rect_t {
   int32_t   x,  y;
   uint16_t dx, dy;
};

extern struct rect_t double_rect(struct rect_t);

int main(void)
{
   struct rect_t rin = {-56, 912, 666, 13};
   struct rect_t rout;
   rout = double_rect(rin);
   printf("x:%" PRId32 ", y:%" PRId32 ", dx:%" PRIu16 ", dy:%" PRIu16 "\n", rout.x, rout.y, rout.dx, rout.dy);
   return 0;
}
