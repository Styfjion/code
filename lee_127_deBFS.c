#include <stdio.h>
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

int BFS(char * word, int *visit, int *othervist, List *queue, char ** wordList, int wordListSize) {
    Queue *unit = LIST_HEAD_ENTRY(queue, Queue, node);
    ListRemoveHead(queue);
    for (int i =0; i < wordListSize; i++) {
        if (!visit[i] && SimilarWord(unit->word, wordList[i])) {
            if (othervist[i]) {
                return unit->pathLen + othervist[i];
            }
            visit[i] = unit->pathLen + 1;
            Queue *nextUnit = malloc(sizeof(Queue));
            strcpy(nextUnit->word, wordList[i]);
            nextUnit->pathLen = unit->pathLen + 1;
            ListAddTail(queue, &nextUnit->node);
        }
    }
    return -1;
}

int ladderLength(char * beginWord, char * endWord, char ** wordList, int wordListSize){

    int visited_start[wordListSize], visited_end[wordListSize];
    memset(visited_start, 0, sizeof(visited_start));
    memset(visited_end, 0, sizeof(visited_end));
    List queue1, queue2;
    ListInit(&queue1);
    ListInit(&queue2);
    Queue *unit1, *unit2;
    unit1 = malloc(sizeof(Queue));
    unit2 = malloc(sizeof(Queue));
    strcpy(unit1->word, beginWord);
    strcpy(unit2->word, endWord);
    unit1->pathLen = 1;
    unit2->pathLen = 1;
    ListAddTail(&queue1, &unit1->node);
    ListAddTail(&queue2, &unit2->node);
    bool token = false;
    for (int i = 0; i < wordListSize; i++) {
        if (!strcmp(beginWord, wordList[i])) {
            visited_start[i] = 1;
        }
        if (!strcmp(endWord, wordList[i])) {
            visited_end[i] = 1;
            token = true;
        }
    }
    if (!token) {
        return 0;
    }
    while (!ListEmpty(&queue1) && !ListEmpty(&queue2)){
        int res;
        res = BFS(beginWord, visited_start, visited_end, &queue1, wordList, wordListSize);
        if (res != -1) {
            return res;
        }
        res = BFS(endWord, visited_end, visited_start, &queue2, wordList, wordListSize);
        if (res != -1) {
            return res;
        }
    }
    return 0;
}

int main(int argc, char const *argv[])
{
    char *input[] = {"hot","dot","dog","lot","log"};
    char *beginWord = "hit";
    char  *endWord = "cog";
    int wordListSize = 5;
    char **wordList = malloc(wordListSize * sizeof(char *));
    memcpy(wordList, input, wordListSize * sizeof(char *));
    int res = ladderLength(beginWord, endWord, wordList, wordListSize);
    printf("%d", res);
    return 0;
}

/*
"hit"
"cog"
["hot","dot","dog","lot","log"]
*/

