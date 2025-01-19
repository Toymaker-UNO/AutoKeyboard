#include "simple_xmlss.hpp"

int main() {
    simple_xmlss::book new_book("Pet Spreadsheet");
    new_book.set_string("Dog",    "Pet", 1, 1);
    new_book.set_string("Cat",    "Pet", 2, 3);
    new_book.set_string("Rabbit", "Pet", 4, 3);
    new_book.print_xmlss("./pet.xml");
    return 0;
}