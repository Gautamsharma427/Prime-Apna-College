#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int main(){
        // vector<int> prices = {7,1,5,3,6,4};
        // int lowest = *min_element(prices.begin(),prices.end());
        // int largest = *max_element(prices.begin(),prices.end());
        // auto lowestIndex = find(prices.begin(),prices.end(),lowest); 
        // auto largestIndex = find(prices.begin(),prices.end(),largest);
        
        // if(distance(prices.begin(),lowestIndex)>distance(prices.begin(),largestIndex)){
        //     return 0;
        // }
        // else if(distance(prices.begin(),lowestIndex)==distance(prices.begin(),largestIndex)){
        //     return 0;
        // }
        // else{
        //     // distance(prices.begin(),lowestIndex)>distance(prices.begin(),largestIndex)
        //     int profit = 0;
        //     for (int i = distance(prices.begin(),lowestIndex); i < distance(prices.begin(),largestIndex); i++)
        //     {
        //         profit = profit+=prices[i];
        //     }
        //     cout<<profit;
            
        // }
        vector<int> arr = {7,1,5,3,6,4};
        int minPrice = arr[0];
        int profit = 0;
        for (int i = 0; i < arr.size(); i++)
        {
            int currentPrice = arr[i];
            int todayProfit = currentPrice-minPrice;//today's profit
            if(todayProfit>profit){
                profit = todayProfit;
            }
            minPrice = min(arr[i],minPrice);
        }
        cout<<"profit: "<<profit;        
    }