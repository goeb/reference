
#include "Wagon.hpp"

class BlueWagon : public Wagon {
    public:
    BlueWagon(const string & _name);
    virtual ~BlueWagon();
    virtual void print();
    virtual void run_thread();
};

BlueWagon::BlueWagon(const string & _name) : Wagon(_name)
{}

BlueWagon::~BlueWagon()
{
    cout << "BlueWagon::~BlueWagon()\n";
}

void *thread_body(void *arg)
{
    cout << "Entering thread_body()...\n";
    int counter = 0;
    while (1)
    {
        cout << "BlueWagon::run_thread(): counter=" << counter << endl;
        counter++;
        usleep(200000);
    }
}
void BlueWagon::run_thread()
{
    cout << "BlueWagon::run_thread()" << endl;
    pthread_t thread;
    pthread_attr_t pthread_custom_attr;
    pthread_attr_init(&pthread_custom_attr);

    pthread_create(&thread, &pthread_custom_attr, thread_body, 0);
    cout << "BlueWagon::run_thread(): thread spawned." << endl;
}

extern "C"
{
    int square(int arg)
    {
        return (arg*arg);
    }

    Wagon* createWagon(string &name) {
        return new BlueWagon(name);
    }

};

void BlueWagon::print() {
    cout << "BlueWagon: my name is " << name << endl;
}



