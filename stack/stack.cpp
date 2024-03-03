#include <iostream>


class Node
{
    public: 
        int value; 
        Node *next;
};


class Stack
{
    private: 
        Node *curr = new Node();
        int elements;
    public: 
        void push(int data)
        {
            Node *newElement = new Node();
            newElement -> value = data;
            newElement -> next = this -> curr -> next;
            this -> curr -> next = newElement;
            this -> elements++;
        }

        int top()
        {
            return this -> curr -> value;
        }

        void pop()
        {
            Node *top = this -> curr; 
            this -> curr -> next = this -> curr -> next -> next;
            this -> elements--;
            delete top; 
        }

        int size()
        {
            return this -> elements;
        }

        bool empty()
        {
            return ! this -> size();
        }
};


Stack my_stack; 

int main()
{
    my_stack.push(1);
    my_stack.push(2);
    my_stack.push(3);
    my_stack.push(4);
    // std::cout<<my_stack.top()<<'\n';

    while(!my_stack.empty())
    {
        std::cout<<my_stack.top()<<'\n';
        my_stack.pop();
    }

}
