#include <string.h>
#include <stdio.h>

int coins = 20;
int main() {
    printf("Welcome to the store! Feel free to buy and sell whatever you like!");
}

int menu() {
    int choice = 0;

    printf("You have %d coins", coins);
    printf("-----------------");
    printf("[1] Buy apples (10 coins)");
    printf("[2] Buy Reimu fumo plush (20 coins)");
    printf("[3] Buy flag (100 coins)");
    printf("[4] Sell an item");
    printf("Enter your choice: ");

    scanf("%d", choice);
}
