#include <string>
#include <stdio.h>
#include <stdlib.h>
#include <errno.h>
#include <string.h>
#include <fstream>
#include <sstream>
#include <vector>


void usage()
{
    printf("Usage: diff <file1> <file2>\n");
    exit(1);   
}

int min(int a, int b)
{
    if (a < b) return a;
    else return b;
}

#define MAX_SIZE 1024
void diff(const std::string &source, const std::string &dest)
{
    const int source_len = source.size();
    const int dest_len = dest.size();

    if (source_len > MAX_SIZE) {
        printf("source_len > MAX_SIZE\n");
        exit(1);
    }
    if (dest_len > MAX_SIZE) {
        printf("dest_len > MAX_SIZE\n");
        exit(1);
    }

    // matrix of Levenshtein distance
    // build the matrix
    unsigned int matrix[MAX_SIZE][MAX_SIZE];
    memset(matrix, 0, sizeof(matrix));

    // initialize the matrix
    int i, j;
    for (i=0; i<source_len+1; i++) matrix[i][0] = i;
    for (j=0; j<dest_len+1; j++) matrix[0][j] = j;

    // compute the matrix
    for (i=0; i<source_len; i++) {
        for (j=0; j<dest_len; j++) {
            if (source[i] == dest[j]) matrix[i+1][j+1] = matrix[i][j];
            else matrix[i+1][j+1] = min(matrix[i][j+1], matrix[i+1][j])+1;
        }
    }

    // follow the path starting from the end
    // in order to find the optimized path
    std::vector<std::pair<char, char> > stack;
    j = dest_len;
    i = source_len;
    while (i>0 and j>0) {
        char modifier; // '+', '-' or '='
        char character;
        if (source[i-1] == dest[j-1]) {
            modifier = '=';
            character = source[i-1];
            j = j-1;
            i = i-1;
        } else {
            // find the best cell
            if (matrix[i-1][j] < matrix[i][j-1]) {
                modifier = '-';
                character = source[i-1];
                i = i-1;
            } else {
                modifier = '+';
                character = dest[j-1];
                j = j-1;
            }
        }
        //printf("DEBUG: %c%c\n", modifier, character);
        stack.insert(stack.begin(), std::make_pair(modifier, character));
    }
    while (i>0) { // source characters to be removed
        stack.insert(stack.begin(), std::make_pair('-', source[i-1])); 
        i = i-1;
    }
    while (j>0) { // dest characters to be added
        stack.insert(stack.begin(), std::make_pair('+', dest[j-1]));
        j = j-1;
    }

    // simplify the stack (put +, - or = together)
    std::vector<std::pair<char, std::string> > simplified_stack;
    simplified_stack.push_back(std::make_pair(stack.front().first, std::string(1, stack.front().second)));
    i = 1;
    int i_s = 0; // index in the simplified stack
    while (i < stack.size()) {
        if (stack[i].first == simplified_stack[i_s].first) {
            simplified_stack[i_s].second += stack[i].second;
        } else {
            i_s++;
            // insert new modifier
            char modifier = stack[i].first;
            std::string newcontents;
            newcontents += stack[i].second;
            simplified_stack.push_back(std::make_pair(modifier, newcontents));
        }
        i++;
    }
    // print simplified_stack
    std::vector<std::pair<char, std::string> >::iterator chunk;
    for (chunk=simplified_stack.begin(); chunk!=simplified_stack.end(); chunk++) {
        printf("%c%s\n", chunk->first, chunk->second.c_str());
    }
}

int loadFile(const char *filepath, std::string &data)
{
    std::ifstream f(filepath);
    if (!f.good()) return -1;
    std::stringstream buffer;
    buffer << f.rdbuf();
    data = buffer.str();
    return 0;
}


int main(int argc, char **argv)
{
    if (argc != 3) usage();

    std::string data1;
    std::string data2;
    int r = loadFile(argv[1], data1);
    if (r != 0) {
        printf("error while loading %s: %s\n", argv[1], strerror(errno));
        exit(1);
    }

    r = loadFile(argv[2], data2);
    if (r != 0) {
        printf("error while loading %s: %s\n", argv[2], strerror(errno));
        exit(1);
    }

    diff(data1, data2);
    return 0;
}
