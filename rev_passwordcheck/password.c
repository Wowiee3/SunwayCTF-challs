#include <string.h>
#include <stdio.h>

int main() {
    char password[50];

    printf("Welcome to the super secret SunCTF flag giver.\n");
    printf("You will need to enter a password to get the flag.\n");
    printf("So? What's the password?\n");

    scanf("%s", password);

    if(strcmp(password, "ineedscissors61") == 0) {
        printf("Your password is correct!\n");
        printf("https://youtu.be/68mbFvenlaQ?si=AWEJH3IUusGwLSTn");
    }
    else {
        printf("Wrong. Try again.");
    }
    return 0;
}
