struct ListNode
{
    int m_nValue;
    ListNode* m_pNext;
};
void AddToTail(ListNode** pHead,int value)
{
    ListNode *pNew = new ListNode();
    pNew->m_nValue = value;
    pNew->m_pNext = nullptr;
    if(*pHead==nullptr)
    {
        *pHead = pNew;
    }
    else
    {
        ListNode *pNode = *pHead;
        while(pNode->m_pNext!=nullptr)
            pNode = pNode->m_pNext;
        pNode->m_pNext = pNew;
    }
    
}
void RemoveNode(ListNode** pHead,int value)
{
    if(pHead==nullptr && *pHead == nullptr)
        return;
    ListNode *pToBeDelete = nullptr;
    if((*pHead)->m_nValue == value)
    {
        pToBeDelete = *pHead;
        *pHead = (*pHead)->m_pNext;
    }
    else
    {
        ListNode *pNode = *pHead;
        while(pNode->m_pNext!=nullptr && pNode->m_pNext->m_nValue!=value)
            pNode = pNode->m_pNext;
        if(pNode->m_pNext!=nullptr && pNode->m_pNext->m_nValue==value)
        {
            pToBeDelete = pNode->m_pNext;
            pNode->m_pNext = pNode->m_pNext->m_pNext;
        }
        if(pToBeDelete!=nullptr)
        {
            delete pToBeDelete;
            pToBeDelete = nullptr;
        }
    }
    
    
}