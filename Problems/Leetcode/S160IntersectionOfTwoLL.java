class ListNode {
    int val;
    ListNode next;

    ListNode(int x) {
        val = x;
        next = null;
    }
}

/**
 * S160IntersectionOfTwoLL
 */
public class S160IntersectionOfTwoLL {
    static ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        if (headA == null || headB == null)
            return null;

        ListNode node1 = headA;
        ListNode node2 = headB;

        while (node1 != node2) {
            if (node1 != null) {
                node1 = node1.next;
            } else {
                node1 = headB;
            }

            if (node2 != null) {
                node2 = node2.next;
            } else {
                node2 = headA;
            }
        }

        return node1;
    }

    static ListNode buildLL(int[] arr) {
        ListNode node = new ListNode(arr[0]);
        ListNode head = node;

        for (int i = 1; i < arr.length; i++) {
            node.next = new ListNode(arr[i]);
            node = node.next;
        }

        return head;
    }

    public static void main(String[] args) {
        int arr1[] = { 1, 2, 3, 4, 5 };
        int arr2[] = { -1, 0 };

        ListNode headA = buildLL(arr1);
        ListNode headB = buildLL(arr2);
        headB.next.next = headA.next.next;

        ListNode sol = getIntersectionNode(headA, headB);

        System.out.println((sol != null) ? sol.val : null);
    }

}