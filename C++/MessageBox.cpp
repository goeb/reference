
// inter-thread message box
// Scheme:
//  - a single thread server
//  - many client threads that post a query and wait for a response.
//
//
// g++ MessageBox.cpp -lpthread -g
//
#include <list>
#include <string.h>
#include <pthread.h>
#include <unistd.h>
#include <stdio.h>


enum MessageCode {
    ATTACH,
    DETACH,
    START_PPP,
    STOP_PPP,
    SEND_AT
};

#define BSIZE 128

struct Message {
    pthread_cond_t responseIndicator;
    pthread_mutex_t responseMutex; // associated with the pthread_cond_t
    // data
    char query[BSIZE+1];
    char response[BSIZE+1];
    Message() {
        responseIndicator = PTHREAD_COND_INITIALIZER;
        responseMutex = PTHREAD_MUTEX_INITIALIZER;
    }
};

class MessageBox {
    public:
    std::list<struct Message*> messages;
    pthread_mutex_t mutex;
    MessageBox() {
        mutex = PTHREAD_MUTEX_INITIALIZER;
    }
    void query(struct Message* m);
    void indicateResponse(struct Message* m);
    struct Message * getMessage();
};


MessageBox B;

// client code
void *client_side(void*name)
{
    printf("client_side[%s] starting...\n", (char*)name);
    int i = 0;
    while (1) {
        struct Message m;
        sprintf(m.query, "%s: get x-%03d", (char*)name, i);
        printf("[%s] going to query: %s...\n", (char*)name, m.query);
        B.query(&m); // block until the server responds
        printf("%s response: %s\n", (char*)name, m.response);

        sleep(2);
    }
    return 0;
}

void *server_side(void*)
{
    while (1) {
        struct Message *nextMsg = B.getMessage();
        if (nextMsg) {
            sprintf(nextMsg->response, "server-echo: %s (yop)", nextMsg->query);
            printf("serveur sending response: [%s]\n", nextMsg->response);
            B.indicateResponse(nextMsg);
        } else usleep(200000);
    }
    return 0;
}

void MessageBox::query(struct Message* m)
{
    pthread_mutex_lock(&m->responseMutex);

    pthread_mutex_lock(&mutex); // lock list
    messages.push_back(m);
    pthread_mutex_unlock(&mutex); // unlock list

    int r = pthread_cond_wait(&m->responseIndicator, &m->responseMutex);
    if (r != 0) {
        printf("pthread_cond_wait error: %s\n", strerror(r));
    }
    pthread_mutex_unlock(&m->responseMutex);

}
struct Message * MessageBox::getMessage()
{
    struct Message *m = 0;
    pthread_mutex_lock(&mutex); // lock list
    if (messages.size()>0) {
        m = messages.front();
        messages.pop_front();
    }
    pthread_mutex_unlock(&mutex); // unlock list
    return m;
}
void MessageBox::indicateResponse(struct Message* m)
{
    pthread_mutex_lock(&m->responseMutex);
    pthread_cond_signal(&m->responseIndicator);
    pthread_mutex_unlock(&m->responseMutex);
}


int main()
{
    pthread_t thread;
    pthread_attr_t attr;
    pthread_attr_init(&attr);

    int r = pthread_create(&thread, &attr, client_side, (void*)"bob");
    if (r != 0) {
        printf("pthread_create(1) error: %s\n", strerror(r));
    }
    r = pthread_create(&thread, &attr, client_side, (void*)"alice");
    if (r != 0) {
        printf("pthread_create(2) error: %s\n", strerror(r));
    }

    server_side(0);
}
