import java.util.Scanner;

class ListNode {
    int val;
    ListNode next;

    ListNode() {
    }

    ListNode(int val) {
        this.val = val;
    }

    ListNode(int val, ListNode next) {
        this.val = val;
        this.next = next;
    }
}

/**
 * LC19RemoveNthNodeFromEnd
 */
public class LC19RemoveNthNodeFromEnd {

    public static int getLLLenght(ListNode head) {
        int len = 1;
        ListNode node = head;

        while (node.next != null && node.next.next != null) {
            node = node.next.next;
            len += 2;
        }

        if (node.next != null) {
            len++;
        }

        return len;
    }

    public static ListNode removeNthFromEnd(ListNode head, int n) {
        if (head == null) {
            return head;
        }

        int lenght = getLLLenght(head);
        int index = lenght-n+1; // +1 to adjust for new LL with temphead attached

        ListNode tempHead = new ListNode(-1, head);
        ListNode node = tempHead;

        int i = 0;
        while (i<index-1) {
            i++;
            node = node.next;
        }

        node.next = node.next.next;

        return tempHead.next;
    }

    // take element input
    public static void populateArr(int[] arr, int startIndex, int n) {
        // populates n numbers from startIndex
        Scanner scan = new Scanner(System.in);
        for (int i = startIndex; i < startIndex + n; i++) {
            arr[i] = scan.nextInt();
        }
    }

    public static void printArr(int[] arr, int startIndex, int n) {
        // prints n numbers from startIndex
        for (int i = startIndex; i < startIndex + n && i < arr.length; i++) {
            System.out.print(arr[i] + " ");
        }
        System.out.println();
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

    public static void printLL(ListNode head) {
        if (head == null) {
            return;
        }

        ListNode node = head;
        while (node != null) {
            System.out.println("Data: " + node.val);
            node = node.next;
        }
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.print("length of array: ");
        int n = scan.nextInt();
        int arr[] = new int[n];

        System.out.print("Enter position from back to delete: ");
        int i = scan.nextInt();

        System.out.print("Enter elements of array: ");
        populateArr(arr, 0, n); // populates array from [startIndex, startIndex+length) position
        scan.close();

        ListNode head = buildLL(arr);
        ListNode node = removeNthFromEnd(head, i);
        printLL(node);
        // System.out.println(getLLLenght(head));
    }
}