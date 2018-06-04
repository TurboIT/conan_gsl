#include <vector>
#include <gsl/span>


int main() {
    auto test = std::vector<int>();
    gsl::span<int> s(test);

}
