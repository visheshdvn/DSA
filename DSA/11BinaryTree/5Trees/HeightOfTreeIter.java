import java.util.Queue;
import java.util.ArrayDeque;
import java.util.Scanner;

class Node {
    int data;
    Node left, right;

    Node(int _data) {
        data = _data;
    }
}

class QueueObject {
    int curr_height;
    Node node;

    QueueObject(int h, Node _node) {
        curr_height = h;
        node = _node;
    }
}

public class HeightOfTreeIter {

    public static int height(Node root) {
        if (root == null) {
            return 0;
        }

        Queue<QueueObject> q = new ArrayDeque<QueueObject>();
        
        int height = 0;
        q.offer(new QueueObject(0, root));

        while (!q.isEmpty()) {
            QueueObject qo = q.poll();

            if (qo.node.left != null) {
                q.offer(new QueueObject(qo.curr_height+1, qo.node.left));
                height = qo.curr_height+1;
            }
            if (qo.node.right != null) {
                q.offer(new QueueObject(qo.curr_height+1, qo.node.right));
                height = qo.curr_height+1;
            }
        }

        return height;
    }

    public static Node insert(Node root, int data) {
        if (root == null) {
            return new Node(data);
        } else {
            Node cur;
            if (data <= root.data) {
                cur = insert(root.left, data);
                root.left = cur;
            } else {
                cur = insert(root.right, data);
                root.right = cur;
            }
            return root;
        }
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int t = scan.nextInt();
        Node root = null;
        while (t-- > 0) {
            int data = scan.nextInt();
            root = insert(root, data);
        }

        scan.close();
        int height = height(root);
        System.out.println(height);

    }
}
