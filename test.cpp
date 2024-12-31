#include <iostream>
#include <fstream>
#include <nlohmann/json.hpp>

using json = nlohmann::json;

int main()
{
    // Open the JSON file
    std::ifstream file("example.json");

    if (!file.is_open())
    {
        std::cerr << "Error opening file!" << std::endl;
        return -1;
    }

    // Parse the JSON content
    json j;
    file >> j;

    // Access data from the JSON object
    std::string name = j["name"];
    int age = j["age"];
    bool isStudent = j["isStudent"];
    std::vector<std::string> courses = j["courses"].get<std::vector<std::string>>();

    // Print the data
    std::cout << "Name: " << name << std::endl;
    std::cout << "Age: " << age << std::endl;
    std::cout << "Is Student: " << isStudent << std::endl;
    std::cout << "Courses: ";
    for (const auto &course : courses)
    {
        std::cout << course << " ";
    }
    std::cout << std::endl;

    return 0;
}
