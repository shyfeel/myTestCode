#include <iostream>  
#include "person.pb.h"  
#include <fstream>  
#include <string>  
  
using namespace std;  
  
int main(){  
    Person *person = new Person;  
    char buffer[BUFSIZ];  
    fstream input("myfile",ios::in|ios::binary);  
    input.read(buffer,sizeof(Person));  
    person->ParseFromString(buffer);  //用这个方法，通常不用ParseFromString  
    cout << person->name() << person->phonenum(0) << endl;  
    cout << person->age()<<endl; 
    return 0;  
}  
