
#include <thread>
#include <condition_variable>
#include <queue>
#include <iostream>

template<typename T> class concurrent_queue {
    std::mutex mtx;
    std::condition_variable cond;
    std::queue<T> q;
public:
    void push(T t) {
        std::unique_lock<std::mutex> lock(mtx);
        q.push(t);
        cond.notify_one();
    }

    T pop() {
        std::unique_lock<std::mutex> lock(mtx);
        cond.wait(lock, [&](){return !q.empty();});
        T t = q.front();
        q.pop();
        return t;
    }
};

int main() {
    enum Action { SayHello, SayWorld, Quit };
    concurrent_queue<Action> queue1, queue2;

    std::thread t1([&]() {
        for (int i = 0; i < 1000; ++i) {
            std::cout << "Hello ";
            queue1.push(SayWorld);
            queue2.pop();
        }
        queue1.push(Quit);
    });

    std::thread t2([&]() {
        while(queue1.pop() != Quit) {
            std::cout << " World\n";
            queue2.push(SayHello);
        }
    });

    t1.join();
    t2.join();
}
