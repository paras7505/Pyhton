#include <iostream>
#include <vector>
using namespace std;

int simpleArraySum(int n) {
    for(int i = 0; i<n; i++)
    {
        for(int j = 0; j<i; j++)
        {
            
        }
    }
}

int main() {
    int n;
    cin >> n;

    vector<int> ar(n);
    for (int i = 0; i < n; i++) {
        cin >> ar[i];
    }

    int result = simpleArraySum(ar);
    cout << result << endl;

    return 0;
}
