#include <stdio.h>
#include <stdlib.h>

void reverse_file(char *input_file_name, char *output_file_name) {
    // Open the input file for reading
    FILE *input_file = fopen(input_file_name, "r");
    if (input_file == NULL) {
        perror("Failed to open input file");
        return;
    }

    // Go to the end of the input file to determine its size
    fseek(input_file, 0, SEEK_END);
    long file_size = ftell(input_file);
    rewind(input_file);

    // Allocate memory to read the file content
    char *data = (char *)malloc(file_size + 1);
    if (data == NULL) {
        perror("Failed to allocate memory");
        fclose(input_file);
        return;
    }

    // Read the file into the allocated memory
    fread(data, 1, file_size, input_file);
    data[file_size] = '\0'; // Null-terminate the string

    // Close the input file
    fclose(input_file);

    // Open the output file for writing
    FILE *output_file = fopen(output_file_name, "w");
    if (output_file == NULL) {
        perror("Failed to open output file");
        free(data);
        return;
    }

    // Write the file in reverse order, character by character
    for (long i = file_size - 1; i >= 0; i--) {
        fputc(data[i], output_file);
    }

    // Close the output file and free the allocated memory
    fclose(output_file);
    free(data);
}

int main() {
    char *input_file_name = "input.txt";
    char *output_file_name = "output.txt";

    reverse_file(input_file_name, output_file_name);

    printf("File '%s' inverted and saved as '%s'.\n", input_file_name, output_file_name);

    return 0;
}
