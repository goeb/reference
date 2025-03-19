#include <map>
#include <stdio.h>
#include <string>

class Container {
	public:
	struct Iterator {
		Iterator(std::map<std::string, std::string>::const_iterator it) noexcept : current(it) {}
		Iterator &operator++() noexcept {
			current++;
			return *this;
		}
		bool operator!=(const Iterator &other) const noexcept {
			return this->current != other.current;
		}
		std::pair<std::string, std::string> operator*() const noexcept {
			return *current;
		}

		private:
			std::map<std::string, std::string>::const_iterator current;
	};

	Iterator begin() const noexcept {
		return Iterator(this->items.begin());
	}

	Iterator end() const noexcept {
		return Iterator(this->items.end());
	}

	std::map<std::string, std::string> items;
};

int main()
{
	Container container;
	container.items["a"] = "aaa";
	container.items["b"] = "bbb";
	container.items["3"] = "333";
	container.items["foo"] = "bar";

	for (auto item: container) {
		printf("%s -> %s\n", item.first.c_str(), item.second.c_str());
	}
}
