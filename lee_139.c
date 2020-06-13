#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include "uthash.h"
#include "securec.h"
#define MAX 100

typedef struct {
    char word[MAX];
    UT_hash_handle hh;
} WordMap;

bool BFS(char *s, char **wordDict, int wordDictSize, WordMap *wordMap)
{
    int length = strlen(s);
    int visited[length + 1];
    memset(visited, 0, sizeof(visited));
    int queue[length];
    int queueHead, queueTail;
    queueHead = queueTail = 0;
    queue[queueTail++] = 0;
    while (queueHead < queueTail) {
        int start = queue[queueHead++];
        char tempStr[length + 1];
        for (int i = 1; i + start <= length; i++) {
            memset(tempStr, 0, length + 1);
            strncpy(tempStr, s + start, i);
            WordMap *temp;
            HASH_FIND_STR(wordMap, tempStr, temp);
            if (temp != NULL && visited[i + start] == 0) {
                if (i + start == length) {
                    return true;
                }
                queue[queueTail++] = i + start;
                visited[i + start] = 1;
            }
        }
    }
    return false;
}

bool wordBreak(char * s, char ** wordDict, int wordDictSize)
{
    WordMap *wordMap, *unit;
    wordMap = NULL;
    for (int i = 0; i < wordDictSize; i++) {
        unit = malloc(sizeof(WordMap));
        strcpy(unit->word, wordDict[i]);
        HASH_ADD_STR(wordMap, word, unit);
    }
    return BFS(s, wordDict, wordDictSize, wordMap);
}

int main(int argc, char const *argv[])
{
    char *s = "applepenapple";
    char *input[] = {"apple","pen"};
    int wordDictSize = 2;
    char **wordDict = malloc(sizeof(char *) * wordDictSize);
    memcpy(wordDict, input, wordDictSize * sizeof(char *));
    bool res = wordBreak(s, wordDict, wordDictSize);
    printf("%d", res);
    return 0;
}

/*
"applepenapple"
["apple","pen"]
*/


