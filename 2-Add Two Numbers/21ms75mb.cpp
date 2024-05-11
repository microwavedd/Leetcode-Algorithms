class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* dummy_head = new ListNode();
        ListNode* current = dummy_head;
        int carry = 0;

        while (l1 || l2 || carry) {
            int sum_val = carry;
            if (l1) {
                sum_val += l1->val;
                l1 = l1->next;
            }
            if (l2) {
                sum_val += l2->val;
                l2 = l2->next;
            }

            carry = sum_val / 10;
            int digit = sum_val % 10;

            current->next = new ListNode(digit);
            current = current->next;
        }

        return dummy_head->next;
    }
};