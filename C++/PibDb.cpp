
class Condition
{
    public:
        void block(Mutex & m, int timeout);
        void release();
};
void Condition::block(Mutex & m, int timeout)
{
    while(!condition)
             pthread_cond_timedwait(&cond, &m, t);

}

class Mutex
{
    private:
        
    public:
        void lock();
        void unlock();
};

class PendingPibRequest
{
    public:
        int id;
        Condition  c;
        int value;
};

class PibDatabase
{
    public:
        int waitForPib(int id);
        int notify(int id, int value);
        
    private:
        Mutex m;
        std::list<PendingPibRequest*> pib;

};

int PibDatabase::waitForPib(int id, int timeout)
{
    m.lock();
    PendingPibRequest *p = new PendingPibRequest(id);
    pib.push_back(p);
    p->c.block(m, timeout); // this unlocks the mutex before waiting
    m.unlock();
    int value = p->value;
    delete p;
    return value;
}
        
int PibDatabase::notifyPib(int id, int value)
{
    m.lock();
    std::list<PendingPibRequest*>::iterator it;
    it = pib.begin();
    while (it != pib.end()) {
        if (it->id == id) {
            it->value = value;
            it->c->release();
            it = pib.erase(it);// remove current element
        } else it ++;
    }
    m.unlock();
}


