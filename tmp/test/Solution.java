package tmp.test;

class Node {
    int data;
    Node next;

    Node(int _data, Node _next) {
        data = _data;
        next = _next;
    }
}

/**
 * Solution
 */
public class Solution {

    public static void main(String[] args) {
        //Node list_dummy[]=new Node[3];
        Node head, node;
        head = new Node(0, null);
        node = head;

        node.next = new Node(1, null);
        node = node.next;

        node.next = new Node(2, null);
        node = node.next;
    }
}