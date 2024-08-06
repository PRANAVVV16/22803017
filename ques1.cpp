#include <iostream>

using namespace std;


int main()

{

   int size=0;int sum=0;

   cin>>size;

   int *ptr=new int[size];

   for(int i=0;i<size;i++)

   {

       cin>>ptr[i];

       sum+=ptr[i];

   }

   int avg=sum/size;

   cout<<avg;

    return 0;

}