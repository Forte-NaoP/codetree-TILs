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

vector<vector<pair<int, int>>> tetris = {
    {{0, 0}, {0, 1}, {0, 2}, {0, 3}}, // ㅡ
    {{0, 0}, {1, 0}, {2, 0}, {3, 0}},
    {{0, 0}, {1, 0}, {0, 1}, {1, 1}}, // ㅁ
    {{0, 0}, {-1, 0}, {0, 1}, {-2, 0}}, // ㄱ
    {{0, 0}, {1, 0}, {0, 1}, {0, 2}},
    {{0, 0}, {0, -1}, {1, 0}, {2, 0}},
    {{0, 0}, {-1, 0}, {0, -1}, {0, -2}},
    {{0, 0}, {-1, 0}, {0, -1}, {-2, 0}}, // ㄱ
    {{0, 0}, {1, 0}, {0, -1}, {0, -2}},
    {{0, 0}, {0, 1}, {1, 0}, {2, 0}},
    {{0, 0}, {-1, 0}, {0, 1}, {0, 2}},
    {{0, 0}, {-1, 0}, {0, 1}, {1, 1}}, // ㄴㄱ
    {{0, 0}, {-1, 0}, {0, -1}, {-1, 1}},
    {{0, 0}, {-1, 0}, {0, -1}, {1, -1}}, // ㄴㄱ
    {{0, 0}, {-1, 0}, {0, 1}, {-1, -1}},
    {{0, 0}, {-1, 0}, {0, 1}, {1, 0}}, // ㅏ
    {{0, 0}, {-1, 0}, {0, -1}, {0, -1}}, // ㅗ
    {{0, 0}, {-1, 0}, {0, -1}, {1, 0}}, // ㅓ
    {{0, 0}, {1, 0}, {0, -1}, {0, 1}}, // ㅜ
};

int arr[200][200];

int32_t main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    
    int n, m;
    cin >> n >> m;

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            cin >> arr[i][j];
        }
    }

    int ans = 0;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            for (auto& t : tetris) {
                int tmp = 0;
                for (auto& p: t) {
                    int x = i + p.first, y = j + p.second;
                    if (x < 0 || x >= n || y < 0 || y >= m) {
                        tmp = 0;
                        break;
                    }
                    tmp += arr[x][y];
                }
                ans = max(ans, tmp);
            }
        }
    }
    cout << ans << "\n";
}