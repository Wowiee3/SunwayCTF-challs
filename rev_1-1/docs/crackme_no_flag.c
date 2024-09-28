#include <stdio.h>
#include <string.h>

int main() {
    char key[50];
    char flag[100];

    printf("You'll need a valid key to get this flag.\n");
    printf("What's your key?\n");

    fflush(stdout);
    scanf("%s", key);

    int new = 0;
    for (int i = 0; i < strlen(key); i++) {
        new += (int)key[i];
    }

    if (new==407) {
        printf("Valid key!\n");
        printf("Flag: <SEND TO SERVER TO GET THE FLAG.>\n");
    }
    else {
        printf("Wrong key. Exiting...\n");
    }
    return 0;
}
