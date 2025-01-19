#include "simple_xmlss.hpp"

int main() {
    // Create a new simple_xmlss::book instance with the title "Make My Pet Spreadsheet".
    // "Make My Pet Spreadsheet" is a debugging string used as an identifier for the simple_xmlss::book instance.
    simple_xmlss::book my_pet("My Pet Spreadsheet");

    // Set the string "Dog" in the cell at Column 1, Row 1 (i.e., Cell A1) in the "Pet" sheet.
    my_pet.set_string("Dog",    "Pet", 1, 1);

    // Set the string "Cat" in the cell at Column 2, Row 3 (i.e., Cell A1) in the "Pet" sheet.
    my_pet.set_string("Cat",    "Pet", 2, 3);

    // Set the string "Rabbit" in the cell at Column 4, Row 3 (i.e., Cell A1) in the "Pet" sheet.
    my_pet.set_string("Rabbit", "Pet", 4, 3);

    // Save the spreadsheet to the file "./my_pet.xml".
    my_pet.print_xmlss("./my_pet.xml");
    return 0;
}