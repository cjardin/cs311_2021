#include <iostream>
#include <cstring>

using namespace std;
  
int main(int argc, char** argv)
{
    int last_move = 0;
    //cout << "You have entered " << argc
    //     << " arguments:" << "\n";
 
    	
    //for (int i = 0; i < argc; ++i)
    //    cout << argv[i] << "\n";
    //cout << "silent";
    if( strcmp(argv[2], "silent" ) == 0){
		    cout << "confess";
    }else {
      cout << "silent";
    }
  
    return 0;
}

