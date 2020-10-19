#include<iostream>
#include<string>
using namespace std;

class Stack {
    private:
        int top;
        int arr[5] = {0};
    public:
        Stack() {
            top = -1;
        }

        bool isEmpty() {
            return (top == -1);
        }

        bool isFull() {
            return (top==4);
        }

        void push(int val) {
            if (isFull()) {
                cout<<"Stack Overflow, Not inserting" << endl;
                return;
            }

            top++;
            arr[top] = val;
        }

        int pop() {
            if (isEmpty()) {
                cout << "Stack UnderFlow" << endl;
                return -1;
            }

            int popval = arr[top];
            arr[top] = 0;
            top--;
            return popval;
        }

        int count() {
            return (top+1);
        }

        int peek(int pos) {
            if (-1 < pos < count()) {
                cout << "Position exceeded" << endl;
                return -1;
            }

            return arr[pos];
        }
 
        void change(int pos, int val) {
            if (-1 < pos < count()) {
                cout << "Position exceeded" << endl;
                return;
            }

            arr[pos] = val;
            cout << "Value changed at location " << pos << endl;
        }

        void display() {
            cout << "All values in Stack are" << endl;
            for (int i = 4; i >=0; i--) {
                cout << arr[i] << endl;
            }
            
        }
};


int main() {
    Stack s1;

    int option, position, value;

    do
    {
        cout << "enter operation to perform. Enter 0 to exit." << endl;
        cout << "1. Push" << endl;
        cout << "2. Pop" << endl;
        cout << "3. Check if Stack is Empty" << endl;
        cout << "4. Check if Stack is Full" << endl;
        cout << "5. Peek a position" << endl;
        cout << "6. total number of elements in Stack" << endl;
        cout << "7. Change element in a loaction" << endl;
        cout << "8. Display whole Stack" << endl;
        cout << "9. Clear Screen" << endl;
        cin >> option;

        switch (option) {
            case 0:
                break;
            case 1:
                cout << "Enter a value to push to stack" << endl;
                cin >> value;
                s1.push(value);
                break;
            
            case 2:
                cout << "Popped value - " << s1.pop() << endl;
                break;
            
            case 3:
                if(s1.isEmpty()) {
                    cout << "Stack is Empty" << endl;
                } else {
                    cout << "Satck is not empty" << endl;
                }
                break;
            
            case 4:
                if(s1.isFull()) {
                    cout << "Stack is Full" << endl;
                } else {
                    cout << "Satck is not Full" << endl;
                }
                break;

            case 5:
                cout << "Enter position" <<endl;
                cin >> position;
                cout << "Value at position - " << position  << " is " << endl << s1.peek(position) << endl;

            case 6:
                cout << "Total num of items in stack are - " << s1.count() << endl;
                break;

            case 7:
                cout << "Change Function Called - " << endl;
                cin >> position;
                cin >> value;
                s1.change(position, value);
                break;
            
            case 8:
                s1.display();
                break;
            
            case 9:
                system("cls");
                break;

            default:
                cout << "enter a valid option number" << endl;
                break;
        }

    } while (option != 0);
    
}