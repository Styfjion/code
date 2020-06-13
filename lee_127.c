#include <stdlib.h>
#include <string.h>
#include "hlist.h"
#define MAX 100

typedef struct Node Node;
typedef struct List List;

typedef struct {
    char word[MAX];
    int pathLen;
    Node node;
} Queue;

bool SimilarWord(char *a, char *b) {
    int count = 0;
    for (int i = 0; a[i] != '\0'; i++) {
        if (a[i] != b[i]) {
            count++;
        }
        if (count > 1) {
            return false;
        }
    }
    return count == 1;
}

int ladderLength(char * beginWord, char * endWord, char ** wordList, int wordListSize){
    
    bool visited[wordListSize];
    memset(visited, false, sizeof(visited));
    List queue;
    ListInit(&queue);
    Queue *unit = malloc(sizeof(Queue));
    strcpy(unit->word, beginWord);
    unit->pathLen = 1;
    ListAddTail(&queue, &unit->node);
    for (int i = 0; i < wordListSize; i++) {
        if (!strcmp(beginWord, wordList[i])) {
            visited[i] = true;
            break;
        }
    }
    while (!ListEmpty(&queue)){
        unit = LIST_HEAD_ENTRY(&queue, Queue, node);
        if (!strcmp(unit->word, endWord)) {
            return unit->pathLen;
        }
        ListRemoveHead(&queue);
        for (int i =0; i < wordListSize; i++) {
            if (!visited[i] && SimilarWord(unit->word, wordList[i])) {
                visited[i] = true;
                Queue *nextUnit = malloc(sizeof(Queue));
                strcpy(nextUnit->word, wordList[i]);
                nextUnit->pathLen = unit->pathLen + 1;
                ListAddTail(&queue, &nextUnit->node);
            }
        }
    }
    return 0;
}
