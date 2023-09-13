
// Definition for a Node.
class Node {
    public int val;
    public Node prev;
    public Node next;
    public Node child;
};

/**
 * LC430
 */
public class LC430FlattenMultiLevelDoublyLL {
    public static Node flatten(Node head) {
        Node node = head;

        while (node != null) {
            Node temp = node.next;

            if (node.child != null) {
                Node childHead = flatten(node.child);

                childHead.prev = node;
                node.next = childHead;

                while (childHead.next != null) {
                    childHead = childHead.next;
                }

                childHead.next = temp;
                if (temp != null) {
                    temp.prev = childHead;
                }
            }

            node.child = null;
            node = temp;
        }

        return head;
    }

    public static void main(String[] args) {

    }
}