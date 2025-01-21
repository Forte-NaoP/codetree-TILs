#include <cstdio>
#include <cstring>
#include <cstdint>
#include <cstdlib>
#include <algorithm>
#include <string>
#include <numeric>
#include <iostream>

using namespace std;

int n, m;

void print(int arr[][20]) {
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            cout << arr[i][j] << " ";
        }
        cout << "\n";
    }
    cout << "-----------\n";
}

void sign(int arr[][20]) {
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            arr[i][j] = abs(arr[i][j]);
        }
    }
}

void up(int arr[][20]) {
    for (int j = 0; j < m; ++j) {
        for (int i = 0; i < n; ++i) {
            if (arr[i][j] == 0) continue;
            int k = i;
            while (k > 0 && arr[k - 1][j] == 0) {
                arr[k - 1][j] = arr[k][j];
                arr[k][j] = 0;
                --k;
            }
            if (k > 0 && arr[k - 1][j] == arr[k][j]) {
                arr[k - 1][j] = -arr[k - 1][j] * 2;
                arr[k][j] = 0;
            } 
        }
    }
}

void down(int arr[][20]) {
    for (int j = 0; j < m; ++j) {
        for (int i = n - 1; i >= 0; --i) {
            if (arr[i][j] == 0) continue;
            int k = i;
            while (k < n - 1 && arr[k + 1][j] == 0) {
                arr[k + 1][j] = arr[k][j];
                arr[k][j] = 0;
                ++k;
            }
            if (k < n - 1 && arr[k + 1][j] == arr[k][j]) {
                arr[k + 1][j] = -arr[k + 1][j] * 2;
                arr[k][j] = 0;
            } 
        }
    }
}

void left(int arr[][20]) {
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            if (arr[i][j] == 0) continue;
            int k = j;
            while (k > 0 && arr[i][k - 1] == 0) {
                arr[i][k - 1] = arr[i][k];
                arr[i][k] = 0;
                --k;
            }
            if (k > 0 && arr[i][k - 1] == arr[i][k]) {
                arr[i][k - 1] = -arr[i][k - 1] * 2;
                arr[i][k] = 0;
            } 
        }
    }
}

void right(int arr[][20]) {
    for (int i = 0; i < n; ++i) {
        for (int j = m - 1; j >= 0; --j) {
            if (arr[i][j] == 0) continue;
            int k = j;
            while (k < m - 1 && arr[i][k + 1] == 0) {
                arr[i][k + 1] = arr[i][k];
                arr[i][k] = 0;
                ++k;
            }
            if (k < m - 1 && arr[i][k + 1] == arr[i][k]) {
                arr[i][k + 1] = -arr[i][k + 1] * 2;
                arr[i][k] = 0;
            } 
        }
    }
}

void copy(int dst[][20], int src[][20]) {
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            dst[i][j] = src[i][j];
        }
    }
}

int ans = 0;
void backtrack(int arr[][20], int depth) {
    if (depth == 5) {
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < m; ++j) {
                ans = max(ans, arr[i][j]);
            }
        }
        return;
    }

    int _arr[20][20];

    copy(_arr, arr);
    up(_arr); sign(_arr);
    backtrack(_arr, depth + 1);

    copy(_arr, arr);
    down(_arr); sign(_arr);
    backtrack(_arr, depth + 1);

    copy(_arr, arr);
    left(_arr); sign(_arr);
    backtrack(_arr, depth + 1);

    copy(_arr, arr);
    right(_arr); sign(_arr);
    backtrack(_arr, depth + 1);
}

int32_t main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    
    int arr[20][20];
    cin >> n;
    m = n;
    for (int i = 0; i < n; ++i) {
        for(int j = 0; j < m; ++j) {
            cin >> arr[i][j];
        }
    }
    
    backtrack(arr, 0);
    cout << ans << "\n";
}