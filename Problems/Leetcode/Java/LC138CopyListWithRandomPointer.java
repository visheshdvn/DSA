class Node {
    int val;
    Node next;
    Node random;

    public Node(int val) {
        this.val = val;
        this.next = null;
        this.random = null;
    }
}

public class LC138CopyListWithRandomPointer {
    public static Node copyRandomList(Node head) {
        if (head == null) {
            return head;
        }
        
        Node node = head;
        while (node != null) {
            Node t = new Node(node.val);
            t.next = node.next;
            node.next = t;

            node = node.next.next;
        }

        node = head;
        while (node != null) {
            if (node.random != null) {
                node.next.random = node.random.next;
            }

            node = node.next.next;
        }

        Node nHead = head.next;
        Node back = head;
        Node front = nHead;

        while (front != null && back != null) {
            back.next = back.next.next;

            if (front.next != null) {
                front.next = front.next.next;
            }

            back = back.next;
            front = front.next;
        }

        return nHead;
    }

    public static void printLL(Node head) {
        Node node = head;
        while (node != null) {
            System.out.print(node.val + " ");
            node = node.next;
        }
    }

    public static void main(String[] args) {
        Node node0 = new Node(7);
        Node node1 = new Node(13);
        Node node2 = new Node(11);
        Node node3 = new Node(10);
        Node node4 = new Node(1);

        node0.next = node1;
        node1.next = node2;
        node2.next = node3;
        node3.next = node4;

        node1.random = node0;
        node2.random = node4;
        node3.random = node2;
        node4.random = node0;

        Node head = copyRandomList(node0);
        printLL(head);
    }
}
