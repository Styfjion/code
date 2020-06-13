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

bool wordBreak(char * s, char ** wordDict, int wordDictSize)
{
    WordMap *map,*unit;
    map = NULL;
    for (int i = 0; i < wordDictSize; i++) {
        unit = malloc(sizeof(WordMap));
        strcpy(unit->word, wordDict[i]);
        HASH_ADD_STR(map, word, unit);
    }

    int length = strlen(s);
    bool dp[length + 1];
    memset(dp, 0, sizeof(dp));
    dp[0] = true;
    for (int i = 1; i <= length; i++) {
        char subStr[length + 1];
        for (int j = 0; j < i; j++) {
            memset(subStr, 0, sizeof(subStr));
            strncpy(subStr, s + j, i - j);
            WordMap *temp;
            HASH_FIND_STR(map, subStr, temp);
            if (dp[j] && temp != NULL) {
                dp[i] = true;
            }
        }
    }
    return dp[length];
}