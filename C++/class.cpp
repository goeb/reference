
class CEventManager
{

public:
 enum Status { 0, SIGNAL_CAUGHT, ERROR };
 enum Flag { READ, WRITE };
}
class A
{
public:
	enum Type { 
		OK,
		ERROR
	};
	static Type f(int x);
};

A::Type A::f(int x) {
	return OK;
}

main()
{
	if (A::f(1) == A::OK) {
	}
}
