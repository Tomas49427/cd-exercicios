#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void reverse_file(char *input_file_name, char *output_file_name) {
    FILE *input_file = fopen(input_file_name, "r");
    if (input_file == NULL) {
        perror("Failed to open input file");
        return;
    }

    // Dynamic array to hold lines
    char **lines = NULL;
    char line[1024]; // Assuming lines do not exceed 1024 characters
    int count = 0;

    // Read lines into the dynamic array
    while (fgets(line, sizeof(line), input_file)) {
        // Trim newline character
        size_t length = strlen(line);
        if (line[length - 1] == '\n') {
            line[length - 1] = '\0';
        }
        // Resize the array of lines
        lines = realloc(lines, (count + 1) * sizeof(char *));
        if (lines == NULL) {
            perror("Failed to allocate memory");
            fclose(input_file);
            return;
        }
        // Duplicate the line to store in the array
        lines[count++] = strdup(line);
    }

    // Close the input file
    fclose(input_file);

    // Open the output file for writing
    FILE *output_file = fopen(output_file_name, "w");
    if (output_file == NULL) {
        perror("Failed to open output file");
        for (int i = 0; i < count; i++) {
            free(lines[i]);
        }
        free(lines);
        return;
    }

    // Write lines in reverse order
    for (int i = count - 1; i >= 0; i--) {
        fprintf(output_file, "%s\n", lines[i]);
        free(lines[i]); // Free each line as we write it
    }

    // Free the array and close the output file
    free(lines);
    fclose(output_file);
}

int main() {
    char *input_file_name = "input.txt";
    char *output_file_name = "output.txt";

    reverse_file(input_file_name, output_file_name);

    printf("File '%s' inverted and saved as '%s'.\n", input_file_name, output_file_name);

    return 0;
}
