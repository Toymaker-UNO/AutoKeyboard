// This is tutorial of "simple_xmlss.hpp".
// "simple_xmlss.hpp" can be downloaded from "https://github.com/Toymaker-UNO/SimpleXmlss".
// "simple_xmlss.hpp" is licensed under the "MIT" License.

// Include the "simple_xmlss.hpp" header file
#include "simple_xmlss.hpp"

int main() {
// Create an instance of simple_xmlss::book named my_book.
simple_xmlss::book my_book;

// Set the string "Dog" in the cell at Column "1", Row "1" (i.e., Cell "A1") in the "Pet" sheet.
my_book.set_string("Dog",    "Pet", 1, 1);

// Set the string "Cat" in the cell at Column "2", Row "3" (i.e., Cell "B3") in the "Pet" sheet.
my_book.set_string("Cat",    "Pet", 2, 3);

// Set the string "Porsche" in the cell at Column "4", Row "3" (i.e., Cell "D3") in the "Car" sheet.
my_book.set_string("Porsche", "Car", 4, 3);

// Save the spreadsheet to the file "./my_spreadsheet.xml".
my_book.print_xmlss("./my_spreadsheet.xml");
return 0;