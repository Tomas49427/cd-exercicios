#include <stdio.h>

int file_symbol_freq(char *file_name, char symbol){
    FILE * file = fopen(file_name,"r");
    int symbol_count = 0;
    char s;
    while((s = fgetc(file)) != EOF ){
        if(s == symbol){
            symbol_count++;
        }
    }
    fclose(file);
    return symbol_count;
}

int main() {
    char symbol = 'o';
    char filename[] = "input.txt";
    printf("The number of times %c appeared in %s was %d\n", symbol, filename, file_symbol_freq(filename,symbol));
    return 0;
}