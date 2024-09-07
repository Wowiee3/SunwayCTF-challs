#include <string.h>
#include <stdio.h>

int main() {
    char password[50];

    printf("Welcome to the super secret SunCTF flag giver.\n");
    printf("You will need to enter a password to get the flag.\n");
    printf("So? What's the password?\n");

    scanf("%s", password);

    if(strcmp(password, "ineedscissors61") == 0) {
        printf("Correct! The flag is sunctf{rev4password}");
    }
    else {
        printf("Wrong. Try again.");
    }
    return 0;
}
