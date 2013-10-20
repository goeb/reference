#include <iostream>
#include <queue>

using namespace std;

class Semaphore
{
public:
    int receive() { return 0; }
};


template <class T> class GenericQueue
{
protected:
    queue<T> Q;
    Semaphore sharedSemaphore;
    T _pop() {T x; return x;} // decrease semaphore, remove first element and return it
    void _push(T) {} ; // increase semaphore, add a new element
public:
};

template <class T> class IncomingQueue : public GenericQueue<T>
{
public:
    T pop() { return GenericQueue<T>::_pop(); } // call _pop()
    void setSemaphore(Semaphore x) {}; // TODO
    int getId() { return 0; }
};

template <class T> class OutgoingQueue : public GenericQueue<T>
{
public:
    void push(T element) { _push(element); } // call _push()
};

class Layer1
{
public:
    IncomingQueue<int> subscribeToUpcomingMessages() { IncomingQueue<int> x; return x;}
    IncomingQueue<string> subscribeToTrace() { IncomingQueue<string> x; return x;}
};

class Layer2
{
public:
    void main();
};

void Layer2::main()
{
    Layer1 lowLayer;
    IncomingQueue<string> layer1Traces = lowLayer.subscribeToTrace();

    OutgoingQueue<string> layer2Traces;
    IncomingQueue<string> fromLayer3;

    Semaphore semaphore;
    layer1Traces.setSemaphore(semaphore);
    fromLayer3.setSemaphore(semaphore);

    int id;

    while ((id = semaphore.receive()) != -1)
    {
        if (id == layer1Traces.getId()) // problem: does not work with dynamically created queues
        {
            // processIncomingLayer1Message(layer1.pop());
            //
            string s = "toto";
            layer2Traces.push(s);
        }
        else if (id == fromLayer3.getId())
        {
            // process down coming event
            string s = "toto2";
            layer2Traces.push(s);
        }
        // else... manage dynamically created incoming queues
    }
}

main()
{
    Layer2 layer2;
    layer2.main();
}
