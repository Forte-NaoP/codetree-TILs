#include <cstdio>
#include <cstring>
#include <cstdint>
#include <cstdlib>
#include <algorithm>
#include <string>
#include <numeric>
#include <iostream>
#include <vector>

using namespace std;

int n;
int max_income;
int day[15], income[15];

int calc_income(int picked) {
    int total = 0;
    for (int i = 0; i < n; ++i) {
        if (picked & (1 << i)) {
            total += income[i];
        }
    }
    return total;
}

void search(int picked, int last) {
    if (last == n) {
        max_income = max(max_income, calc_income(picked));
        return;
    }

    for (int i = last; i < n; ++i) {
        search(picked | (1 << i), day[i]);
    }
}

int32_t main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    cin >> n;
    for (int i = 0; i < n; ++i) {
        cin >> day[i] >> income[i];
        day[i] += i;
    }

    search(0, 0);
    cout << max_income << "\n";

}