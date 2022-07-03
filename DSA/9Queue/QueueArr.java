/**
 * QueueArr
 */

class Queue {
    int queue[];
    int size = 0, front = 0, cap;

    Queue(int c) {
        queue = new int[c];
        cap = c;
    }

    // methods
    boolean isFull() {
        return cap == size;
    }

    boolean isEmpty() {
        return (size == 0);
    }

    int getFront() {
        if (isEmpty()) {
            return -1;
        } else {
            return front;
        }
    }

    int getRear() {
        if (isEmpty()) {
            return -1;
        } else {
            return (front + size - 1) % cap;
        }
    }

    void enQueue(int x) {
        if (isFull()) {
            System.out.println("Queue space full. Cannot put: " + x);
            return;
        }
        int rear = getRear();
        rear = (rear + 1) % cap;
        queue[rear] = x;
        size++;
    }

    void deQueue() {
        if (isEmpty()) {
            System.out.println("Queue already empty.");
            return;
        }
        front = (front + 1) % cap;
        size--;
    }
}

public class QueueArr {

    public static void main(String[] args) {
        Queue queue = new Queue(10);

        queue.enQueue(1);
        queue.enQueue(2);
        queue.enQueue(3);
        queue.enQueue(4);
        queue.enQueue(5);
        queue.enQueue(6);
        queue.enQueue(7);
        queue.enQueue(8);
        queue.enQueue(9);
        queue.enQueue(10);
        queue.deQueue();
        queue.enQueue(11);
        // System.out.println(queue.size + " " + queue.cap);
        // System.out.println(queue.front + " " + queue.queue);
        for (int i = 0; i < 10; i++) {
            System.out.println(queue.queue[i] + " ");
        }
    }
}
