#include "data_model.h"

std::string hexlify(const unsigned char *data, size_t length, size_t limit)
{
    std::string result;
    char buffer[3];
    for (size_t i = 0; i < length; i++) {
        if (limit > 0 && i >= limit) {
            result += "...";
            break;
        }
        sprintf(buffer, "%02X", data[i]);
        result += buffer;
    }
    return result;
}

std::string hexlify(const OctetString &data, size_t limit)
{
    return hexlify(data.data(), data.size(), limit);
}

Array::~Array()
{
    for (auto i: items) delete i;
    items.clear();
}

std::string Array::to_string() const
{
    std::string result;
    for (auto const &i: items) {
        if (!result.empty()) result += ",";
        result += i->to_string();
    }
    result.insert(0, "[");
    result += "]";
    return result;
}

Array::Array(const Array& other)
{
    *this = other;
}

Array& Array::operator=(const Array& other)
{
    if (this == &other) return *this;

    // Clean pre-existing value
    for (auto i: items) {
        delete i;
    }
    items.clear();
    for (auto i: other.items) {
        items.push_back(i->clone());
    }
    return *this;
}

/**
 * @brief Array::push_back
 * @param value
 *
 * The value is taken by the Array instance. The caller
 * must not delete it after this call.

 */
void Array::push_back(Value *value)
{
    items.push_back(value);
}


Value *Array::clone() const
{
    Array *new_array = new Array();
    for (auto i: items) {
        new_array->items.push_back(i->clone());
    }
    return new_array;
}

Object::~Object()
{
    for (auto i: items) {
        delete i.second;
    }
}

std::string Object::to_string() const
{
    std::string result;
    for (auto const &i: items) {
        if (!result.empty()) result += ",";
        result += i.first + ":" + i.second->to_string();
    }
    result.insert(0, "{");
    result += "}";
    return result;
}

Object::Object(const Object &other)
{
    *this = other;
}

Object& Object::operator=(const Object &other)
{
    if (this == &other) return *this;

    // Clean pre-existing value
    for (auto i: items) {
        delete i.second;
    }
    items.clear();

    for (auto i: other.items) {
        items[i.first] = i.second->clone();
    }
    return *this;
}

/**
 * @brief Object::insert
 * @param key
 * @param value
 *
 * The value is taken by the Object instance. The caller
 * must not delete it after this call.
 */
void Object::insert(const std::string &key, Value *value)
{
    if (items.count(key)) delete items[key];
    items[key] = value;
}

const Value *Object::get(const std::string &key) const
{
    std::map<std::string, Value*>::const_iterator it = items.find(key);
    if (it == items.end()) return nullptr;
    return it->second;
}

Value *Object::clone() const
{
    Object *new_object = new Object();
    for (auto i: items) {
        new_object->items[i.first] = i.second->clone();
    }
    return new_object;
}

std::string GenericString::to_string() const
{
    return std::string(this->data(), this->size());
}

Value *Number::clone() const
{
    return new Number(this->to_string());
}

Value *String::clone() const
{
    return new String(this->to_string());
}

Value *Literal::clone() const
{
    return new Literal(this->to_string());
}

Bytes::Bytes(const unsigned char *ptr, size_t size) : bytes(ptr, size)
{

}

Value *Bytes::clone() const
{
    return new Bytes(bytes.data(), bytes.size());
}

std::string Bytes::to_string() const
{
    return hexlify(bytes.data(), bytes.size());
}

/* demonstration program about how to use these types
 *
 * Expected output:
 * obj1: {literal expression:true,some bytes:736F6D6520646174612E2E2E,word:hello}
 * array1: [{literal expression:true,some bytes:736F6D6520646174612E2E2E,word:hello},{literal expression:true,name:John,some bytes:736F6D6520646174612E2E2E,word:hello}]
 */

int main()
{
	String *str1 = new String("hello");
	Literal *literal = new Literal("true");
	unsigned char data[] = "some data...";
	Bytes *bytes = new Bytes(data, sizeof(data));
	Object obj1;
	obj1.insert("word", str1);
	obj1.insert("literal expression", literal);
	obj1.insert("some bytes", bytes);

	printf("obj1: %s\n", obj1.to_string().c_str());

	Value *obj2 = obj1.clone();
	Array array1;
	array1.push_back(obj2);
	obj1.insert("name", new String("John"));
	array1.push_back(obj1.clone());

	printf("array1: %s\n", array1.to_string().c_str());
}
