/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    void reorderList(ListNode* head) {
        ListNode* slow = head;
        ListNode* fast = head->next;
        while(fast && fast->next){
            slow = slow->next;
            fast = fast->next;
            fast = fast->next;
        }
        ListNode* secondH = slow->next;
        slow->next = nullptr;

        ListNode* prev = nullptr;
        ListNode* curr = secondH;
        while(curr){
            ListNode* nextN = curr->next;
            curr->next = prev;
            prev = curr;
            curr = nextN;
        }
        secondH = prev;
        ListNode* firstH = head;
        while(secondH){
            ListNode* temp1 = firstH->next;
            ListNode* temp2 = secondH->next;
            firstH->next = secondH;
            secondH->next = temp1;
            firstH = temp1;
            secondH = temp2;
        }

        
    }
};
