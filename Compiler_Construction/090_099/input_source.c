/* Sample program to test the lexical analyzer
   This comment spans multiple lines */

int main() {
    int count = 10;
    float avg = 3;
    char grade = 'A';
    char *name = "Ahmed";

    if (count >= 5 && avg != 0) {
        count = count + 1;
    }

    int bad@name = 5;
    char c = 'AB';
    char *msg = "unterminated string;
    int y = 5x;
    int z = ~5;
    int w = #5;

    return 0;
}

/* this comment never closes
int x = 5;