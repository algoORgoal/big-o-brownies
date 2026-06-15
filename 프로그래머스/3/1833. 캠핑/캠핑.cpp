#include <vector>
#include <iostream>
#include <cmath>
#include <unordered_map>
#include <algorithm>
#include <unordered_set>

using namespace std;

// 전역 변수를 정의할 경우 함수 내에 초기화 코드를 꼭 작성해주세요.
int solution(int n, vector<vector<int>> data) {
    unordered_set<pair<pair<int, int>, pair<int, int>>> visited;
    unordered_map<int, vector<int>> x_to_y_list;
    
    for (vector<int> position: data) {
        auto x = position[0], y = position[1];
        x_to_y_list[x].push_back(y);
    }
    
    unordered_set<int> x_keys;
    for (auto [x, y_list]: x_to_y_list) {
        x_keys.insert(x);
    }
    
    
    vector<int> x_key_vector(x_keys.begin(), x_keys.end());
    x_key_vector.sort(x_key_vector.begin(), x_key_vector.end());
        
    int total = 0;
    
    for (int i = 0; i < x_key_vector.size(); i++) {
        if (i == 0) {
            continue;
        }
        
        int last_x = x_key_vector[i - 1];
        int current_x = x_key_vector[i];
        
        for (int last_y: x_to_y_list[last_x]) {
            for (int current_y: x_to_y_list[current_x]) {
                visited.insert(
                    minmax(
                        pair<int, int>(last_x, last_y),
                        pair<int, int>(current_x, current_y)
                    )
                );

                total += 1;
            }
        }
    }
    
    
    unordered_map<int, vector<int>> y_to_x_list;

    
    for (vector<int> position: data) {
        auto x = position[0], y = position[1];
        y_to_x_list[y].push_back(x);
    }
    
    unordered_set<int> y_keys;
    for (auto [y, x_list]: y_to_x_list) {
        y_keys.insert(y);
    }
    
    
    vector<int> y_key_vector(y_keys.begin(), y_keys.end());
    y_key_vector.sort(y_key_vector.begin(), y_key_vector.end());
    
    for (int i = 0; i < y_key_vector.size(); i++) {
        if (i == 0) {
            continue;
        }
        
        int last_y = y_key_vector[i - 1];
        int current_y = y_key_vector[i];
        
        for (int last_x: y_to_x_list[last_y]) {
            for (int current_x: y_to_x_list[current_y]) {
                    if (!visited.contains(
                        minmax(
                            pair<int, int>(last_x, last_y),
                            pair<int, int>(current_x, current_y),
                        )
                    )) {
                        total += 1;
                    }
                }
            }
        }
    }

    return total;
}


// O(n) 시간 안에 스위핑으로 풀 수 있을 듯
// 1. x 좌표: y좌표 리스트 형태로 변환
// 2. x좌표 순으로 정렬하여 순회
//      count += 이전 x좌표 점의 개수 * 현재 x좌표 점의 개수(경계에 위치하는 경우 허용, 다른 점 포함하면 안 됌)
// 

// 반례: (1, 1), (2, 3), (3, 2)
// 1 * 1 + 1 * 1 = 2이지만,
// (1, 1), (3, 2)로도 가능하다. => y좌표 기준으로도 정렬을 해야 된다.
// 그리고 x좌표에서, 이미 지나간 쌍인지 확인도 해줘야 된다.


// 25_000_000