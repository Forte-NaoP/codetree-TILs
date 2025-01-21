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
        {{0,1},{0,2},{0,3}},{{1,0},{2,0},{3,0}},		// 연속 일자 모형
		{{0,1},{1,0},{1,1}},							// 정사각형
        {{1,0},{1,1},{2,0}},{{1,0},{2,0},{1,-1}},{{0,1},{0,2},{-1,1}},{{0,1},{0,2},{1,1}},	// 가운데 툭튀 형
        {{1,0},{1,1},{2,1}},{{1,0},{0,1},{-1,1}},{{0,1},{-1,1},{-1,2}},{{0,1},{1,1},{1,2}},	// 계단형
        {{1,0},{2,0},{2,1}},{{0,1},{-1,1},{-2,1}},{{0,1},{1,0},{2,0}},{{0,1},{1,1},{2,1}},	// ㄴ 형
        {{0,1},{0,2},{-1,2}},{{1,0},{1,1},{1,2}},{{0,1},{0,2},{1,2}},{{0,1},{0,2},{1,0}}
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
                int tmp = arr[i][j];
                for (auto& p: t) {
                    int x = i + p.first, y = j + p.second;
                    if (x < 0 || x >= n || y < 0 || y >= m) {
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