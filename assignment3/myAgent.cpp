#include <iostream>
#include <fstream>
#include <queue>
using namespace std;

double readFromFile(string fileName)
{
    double n;
    ifstream file;
    file.open("strat.txt");

    if(!file.is_open())
    {
    cout << "File could not be opened." << endl;
    return 1;
    }

    while(!file.eof())
    {
      file >> n;
    }
    file.close();
    return n;
}

void writeToFile(string fileName, double strat)
{
  ofstream file;
  file.open("strat.txt");

  file << strat;
  file.close();
}

double PrintAction(queue<double>& myQueue,int pass_move)
{
  double num = 0.0;
  double strats;
  strats = myQueue.front();
  //if opponent stays silent increase by 0.1
  if(pass_move == 0)
  {
    num = strats+0.01;
  }
  else//if opponent confess decrease by 0.1
  {
    num = strats-0.01;
  }
  //if 0.5+ confess
  if(num >= 0.5){
    cout << "confess" << endl;
  }
  else//if -0.5 silent
  {
    cout << "silent" << endl;
  }
  return num;
}

int main(int argc, char* argv[]) {
  double num;
  queue<double> Numque;
  string arg = argv[2];
  
 // cout << arg << endl;

  if(arg == "silent"){
    num = readFromFile("strat.txt");
    Numque.push(num);
    //1 = Opponent stayed silent
    num = PrintAction(Numque,0);
    writeToFile("strat.txt",num);
  }
  else if(arg == "confess") {
    num = readFromFile("strat.txt");
    Numque.push(num);
    //1 = opponent confessed
    num = PrintAction(Numque,1);
    writeToFile("strat.txt",num);
  }
  else{
    writeToFile("strat.txt",0.5);
    cout << "confess" << endl;
  }
  
  return 0;
}
