#include <cstdio>
#include <cstring>
#include <cstdint>
#include <cstdlib>
#include <algorithm>
#include <string>
#include <numeric>
#include <iostream>

using namespace std;

struct Cube {
    int f, b, l, r, u, d;
    int x, y;

    Cube(int x, int y): x(x), y(y) {
        f = b = l = r = u = d = 0;
    } 

    void up() {
        int t = f;
        f = d; d = b; b = u; u = t;
        x -= 1;
    }
    
    void down() {
        int t = f;
        f = u; u = b; b = d; d = t;
        x += 1;
    }

    void left() {
        int t = u;
        u = r; r = d; d = l; l = t;
        y -= 1;
    }

    void right() {
        int t = u;
        u = l; l = d; d = r; r = t;
        y += 1;
    }

    void print() {
        cout << u << "\n" << l << " " << f << " " << r << " " << b << "\n" << d << "\n";
    }
};

int32_t main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    
    int n, m, x, y, k;
    cin >> n >> m >> x >> y >> k;

    int floor[20][20];
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            cin >> floor[i][j];
        }
    }

    Cube cube(x, y);
    int move;
    for (int i = 0; i < k; ++i) {
        cin >> move;
        if (move == 1) {
            if (cube.y + 1 == m) continue;
            cube.right();
        } else if (move == 2) {
            if (cube.y == 0) continue;
            cube.left();
        } else if (move == 3) {
            if (cube.x == 0) continue;
            cube.up();
        } else {
            if (cube.x + 1 == n) continue;
            cube.down();
        }
        int& bottom = floor[cube.x][cube.y];
        if (bottom == 0) {
            bottom = cube.d;
        } else {
            cube.d = bottom;
            bottom = 0;
        }
        // cube.print();
        // for (int i = 0; i < n; ++i) {
        //     for (int j = 0; j < m; ++j) {
        //         cout << floor[i][j] << " ";
        //     }
        //     cout << "\n";
        // }
        cout << cube.u << "\n";
    }

}