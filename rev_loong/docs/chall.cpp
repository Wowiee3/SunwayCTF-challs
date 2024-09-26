#include <iostream>

using namespace std;

char flag[32] = {
    0x14, 0x1d, 0x7, 0x7, 0x6, 0x7, 0x1c, 0xf, 0x59, 0x54, 0x16, 0x3e, 0x34, 0x1c, 0x5d, 0x16, 0x26, 0x50, 0x9, 0xf,
    0x36, 0x13, 0x43, 0x15, 0x2f, 0x37, 0x11, 0x54, 0x20, 0x33, 0x35, 0x15
};

int main() {
    string input;
    cout << "Tell me the key: ";
    cin >> input;

    if (input.length() != 6) {
        cout << "Wrong key." << endl;
    } else {
        cout << "The flag probably is:" << endl;
        for (int i = 0; i < sizeof flag; i++) {
            cout << static_cast<char>(flag[i] ^ input[i % 6]);
        }
    }

    return 0;
}
