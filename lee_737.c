/*并查集*/
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "uthash.h"
#define MAX_LEN 20
typedef struct {
    char word[MAX_LEN];
    int index;
    UT_hash_handle hh;
} Myhash;

int FindRoot(int root, int *pre) 
{
    int son, tmp;
    son = root;
    while (root != pre[root]) {
        root = pre[root];
    }
    while (root != son) {
        tmp = pre[son];
        pre[son] = root;
        son = tmp;
    }
    return root;
}

Myhash * InitHash( char *** pairs, int pairsSize, int *hashSize)
{
    int count = 0;
    Myhash *map, *node;
    map = NULL;
    for (int i = 0; i < pairsSize; i++) {
        for (int j = 0; j < 2; j++) {
            node = NULL;
            HASH_FIND_STR(map, pairs[i][j], node);
            if(node == NULL) {
                node = malloc(sizeof(Myhash));
                strcpy(node->word, pairs[i][j]);
                node->index = count++;
                HASH_ADD_STR(map, word, node);
            }
        }
    }
    *hashSize = count;
    return map;
}

void UnionHash(Myhash *map,  char *** pairs, int pairsSize, int *pre)
{
    Myhash *node1, *node2;
    for (int i = 0; i < pairsSize; i++) {
           node1 = node2 = NULL;
           HASH_FIND_STR(map, pairs[i][0], node1);
           HASH_FIND_STR(map, pairs[i][1], node2);
           int root1 = FindRoot(node1->index, pre);
           int root2 = FindRoot(node2->index, pre);
           if (root1 != root2) {
               pre[root2] = root1;
           }
        }
}

bool areSentencesSimilarTwo(char ** words1, int words1Size, char ** words2, int words2Size, char *** pairs, int pairsSize, int* pairsColSize){
    if(words1Size != words2Size) {
        return false;
    }
    int hashSize;
    Myhash *map;
    map = InitHash(pairs, pairsSize, &hashSize);
    int pre[hashSize];
    for (int i = 0; i < hashSize; i++) {
        pre[i] = i;
    }
    UnionHash(map, pairs, pairsSize, pre);
    Myhash *node1, *node2;
    for (int i = 0; i <words1Size; i++) {
        node1 = node2 = NULL;
        if (strcmp(words1[i], words2[i]) == 0) {
            continue;
        }
        HASH_FIND_STR(map, words1[i], node1);
        HASH_FIND_STR(map, words2[i], node2);
        if (node1 == NULL || node2 == NULL) {
            return false;
        }
        int root1 = FindRoot(node1->index, pre);
        int root2 = FindRoot(node2->index, pre);
        if(root1 != root2) {
            return false;
        }
    }
    return true;
}

int main(int argc, char const *argv[])
{
    char *words1[] = {"great","acting","skills"};
    char *words2[] = {"fine","drama","talent"};
    char *pairs[][2] = {{"great","good"},{"fine","good"},{"drama","acting"},{"skills","talent"}};
    char **w1 = malloc(3 * sizeof(char *));
    char **w2 = malloc(3 * sizeof(char *));
    for (int i = 0; i <3; i++) {
        w1[i] = words1[i];
        w2[i] = words2[i];
    }
    char ***pa = malloc(4 * sizeof(char **));
    for (int i = 0; i < 4; i++) {
        pa[i] = malloc(2 * sizeof(char *));
        pa[i][0] = pairs[i][0];
        pa[i][1] = pairs[i][1];
    }
    int a = 2;
    printf("%d", areSentencesSimilarTwo(w1, 3, w2, 3, pa, 4, &a));
    return 0;
}
