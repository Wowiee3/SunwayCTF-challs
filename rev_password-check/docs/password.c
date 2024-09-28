#include <string.h>
#include <stdio.h>

int main() {
    char password[50];
    char x[20] = "ineedscissors61";

    printf("So? What's the password?\n");

    scanf("%s", password);

    for (int i = 0; i < strlen(password); i++){
        if (password[i] != x[i]) {
            printf("Wrong password! Exiting..");
            return 0;
        }
    }

    printf("Your password is correct!\n");
    char *p = "https://youtu.be/68mbFvenlaQ?si=AWEJH3IUusGwLSTn";
    return 0;
}
