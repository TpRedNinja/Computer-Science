#include <cstring>
#include <iostream>

int main()
{
    for (int i = 1; i <= strlen("Hello");i++)
        printf("%.*s\n",i, "Hello");
    return 0;
}