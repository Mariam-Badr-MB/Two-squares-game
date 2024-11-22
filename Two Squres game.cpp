#include <limits>
#include <iostream>

using namespace std;
int main(){    
    int number,points;
    cout<<"Welcome to this Game"<< endl;
    cout<<"To win, you have to score 100 point"<<endl;
    cout<<"3_the number is between (1:10)"<<endl;

    points = 0 ;
    cout<<"points = "<<points<<endl;

    while (points < 100)
    {
        cout<<"player1: please, enter the number: ";
        cin>> number ;

        while (true){  

         if (cin.fail())
           {
            cin.clear();
            cin.ignore(numeric_limits<streamsize>::max());
            cout<<"invalid" <<endl;
            cout<<"player1: please, enter the number: ";
            cin>> number ;     
          }
         else
             {
            break;
          }

         }
        while (number < 1 || number > 10 ){

           cout<<"player1 please enter number between (1:10): ";
           cin >> number;

           }

        points += number ;
        cout <<"Now point = "<< points <<endl; 
        while (points >= 100)  

          {
            if (points == 100){
                cout << "player 1 is winning " <<endl;
                cout << "End Game "<<endl ;
                break; 
            }
            else
                 {
                points -= number;
                cout << "player1:you have score bigger than 100 point.please, enter the number:  ";
                cin >> number;
            }
        }       
        cout<<"player2: please, enter the number: ";
        cin >> number ;

        while (number < 1 || number > 10 ){

           cout<<"player2 please enter number between (1:10): " ;
           cin >> number;
        }
        points += number ;

        cout <<"Now point = "<< points <<endl; 

        while (points >= 100)  
          {
            if (points == 100){
                cout << "player 2 is winning "<<endl;
                cout << "End Game "<<endl ;
                break;
            }
            else
                 {
                points -= number;
                cout << """player2:you have score bigger than 100 point.please, enter the number:  """;
                cin >>number;
            }       
        }
         

    }
    
    
return 0;
}





