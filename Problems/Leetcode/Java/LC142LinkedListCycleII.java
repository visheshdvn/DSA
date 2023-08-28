import java.util.Hashtable;

class ListNode {
    int val;
    ListNode next;

    ListNode(int x) {
        val = x;
        next = null;
    }
}

public class LC142LinkedListCycleII {

    public static ListNode detectCycleOptimized(ListNode head) {
        if (head == null || head.next == null) {
            return null;
        }

        ListNode slow = head, fast = head, entry = head;

        while (fast.next != null && fast.next.next != null) {
            slow = slow.next;
            fast = fast.next.next;

            if (fast == slow) {
                while (entry != slow) {
                    entry = entry.next;
                    slow = slow.next;
                }
                return entry;
            }
        }

        return null;
    }

    public static ListNode detectCycle(ListNode head) {
        if (head == null) {
            return null;
        }

        ListNode node = head;
        Hashtable<ListNode, Integer> h = new Hashtable<>();

        int index = 0;
        while (node != null) {
            int i = h.getOrDefault(node, -1);

            if (i == -1) {
                h.put(node, index);
            } else {
                return node;
            }

            node = node.next;
            index++;
        }

        return null;
    }

    public static void main(String[] args) {
        ListNode head = new ListNode(1);
        ListNode node1 = new ListNode(2);
        ListNode node2 = new ListNode(3);
        ListNode node3 = new ListNode(4);
        ListNode node4 = new ListNode(5);
        ListNode node5 = new ListNode(6);
        ListNode node6 = new ListNode(7);

        head.next = node1;
        node1.next = node2;
        node2.next = node3;
        node3.next = node4;
        node4.next = node5;
        node5.next = node6;
        node6.next = node3;

        System.out.println(detectCycleOptimized(head));
    }
}