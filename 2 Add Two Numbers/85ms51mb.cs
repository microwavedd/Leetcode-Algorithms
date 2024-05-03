public class Solution {
    public ListNode AddTwoNumbers(ListNode l1, ListNode l2) {
        ListNode dummy_head = new ListNode();
        ListNode current = dummy_head;
        int carry = 0;

        while (l1 != null || l2 != null || carry != 0) {
            int sum_val = carry;
            if (l1 != null) {
                sum_val += l1.val;
                l1 = l1.next;
            }
            if (l2 != null) {
                sum_val += l2.val;
                l2 = l2.next;
            }

            carry = sum_val / 10;
            int digit = sum_val % 10;

            current.next = new ListNode(digit);
            current = current.next;
        }

        return dummy_head.next;
    }
}