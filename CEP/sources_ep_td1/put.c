#include <stdio.h>

char *x = "abc";
char y[] = "abc";

int main(void)
{
   puts(x);
   puts(y);
   x++;
   puts(x);
#ifdef CODE_FAUX
   y++;
#endif
   puts(y);
   return 0;
}
