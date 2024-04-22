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

void print_histogram_line(int frequency, char symbol){
    char buffer[255];
    int index = 0;
    int maximum_divider = 10000;
    while(frequency / maximum_divider == 0) {
        if(maximum_divider == 1) {
            break;
        }
        maximum_divider /= 10;
    }
    for(int i = frequency; i > 0; i = i % maximum_divider, maximum_divider /= 10){
        int value = i / maximum_divider;
        if(maximum_divider == 10000) {
            for(int j = 0; j < value; j++) {
                buffer[index++] = '#';
            }
        }
        else if(maximum_divider == 1000) {
            for(int j = 0; j < value; j++) {
                buffer[index++] = '$';
            }
        }
        else if(maximum_divider == 100) {
            for(int j = 0; j < value; j++) {
                buffer[index++] = '&';
            }
        }
        else if(maximum_divider == 10) {
            for(int j = 0; j < value; j++) {
                buffer[index++] = '+';
            }
        }
        else {
            for(int j = 0; j < value; j++) {
                buffer[index++] = '!';
            }
        }
        if(maximum_divider == 0) {
            break;
        }
    }
    buffer[index] = '\0';
    printf("%c | %s\n", symbol,buffer);
}

void file_histogram(char *file_name){
    int symbol_freq[93] = {0};
    FILE * file = fopen(file_name,"r");
    char s;
    while((s = fgetc(file)) != EOF ){
        if(s >= '!' && s <= '~') {
            symbol_freq[s-33] = symbol_freq[s-33] + 1;
        }
    }
    fclose(file);
    printf("! = 1 | + = 10 | & = 100 | $ = 1000 | # = 10000\n");
    printf("----------------------\n");
    for(int i = 0; i < 93; i++){
        if(symbol_freq[i] != 0){
            print_histogram_line(symbol_freq[i], i + 33);
        }
    }
    printf("----------------------\n");
}

int main() {
    char filename[] = "input.txt";
    file_histogram(filename);
    return 0;
}