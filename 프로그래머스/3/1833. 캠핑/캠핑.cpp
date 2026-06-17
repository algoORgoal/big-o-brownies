#include <iostream>
#include <vector>
#include <algorithm>
#include <unordered_map>
#include <set>

using namespace std;

int solution(int n, vector<vector<int>> data) {
    vector<int> x_list;
    vector<int> y_list;
    
    for (vector<int> position: data) {
        int x = position[0], y = position[1];
        x_list.push_back(x);
        y_list.push_back(y);
    }
    
    sort(x_list.begin(), x_list.end());
    sort(y_list.begin(), y_list.end());
    
    x_list.erase(unique(x_list.begin(), x_list.end()), x_list.end());
    y_list.erase(unique(y_list.begin(), y_list.end()), y_list.end());
    
    
    unordered_map<int, int> x_to_index;
    unordered_map<int, int> y_to_index;
    
    for (int i = 0; i < x_list.size(); i++) {
        x_to_index[x_list[i]] = i;
    }
    
    for (int i = 0; i < y_list.size(); i++) {
        y_to_index[y_list[i]] = i;
    }
    
    set<pair<int, int>> compressed_points;
    
    for (vector<int> position: data) {
        int x = position[0], y = position[1];
        int compressed_x = x_to_index[x], compressed_y = y_to_index[y];
        pair<int, int> compressed_point(compressed_x, compressed_y);
        compressed_points.insert(compressed_point);
    }
    
    vector<vector<int>> count_point(n, vector<int>(n));
    
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (i - 1 >= 0 && j - 1 >= 0) {
                count_point[i][j] = count_point[i - 1][j] + count_point[i][j - 1] - count_point[i - 1][j - 1];
            }
            else if (i - 1 >= 0) {
                count_point[i][j] = count_point[i - 1][j];
            }
            else if (j - 1 >= 0) {
                count_point[i][j] = count_point[i][j - 1];
            }
            
            pair<int, int> p = { i, j };
            
            if (compressed_points.find(p) != compressed_points.end()) {
                count_point[i][j] += 1;
            }
        }
    }
    
    vector<pair<int, int>> compressed_point_vector(compressed_points.begin(), compressed_points.end());
    
    int total = 0;
    
    for (int i = 0; i < compressed_point_vector.size(); i++) {
        for (int j = i + 1; j < compressed_point_vector.size(); j++) {
            pair<int, int> x_pair = minmax(compressed_point_vector[i].first, compressed_point_vector[j].first);
            pair<int, int> y_pair = minmax(compressed_point_vector[i].second, compressed_point_vector[j].second);
            
            int min_x = x_pair.first, max_x = x_pair.second;
            int min_y = y_pair.first, max_y = y_pair.second;
            
            if (min_x == max_x || min_y == max_y) continue;
            
            if (max_x - min_x <= 1 || max_y - min_y <= 1) {
                total += 1;
                continue;
            }
            
            
            int count = count_point[max_x - 1][max_y - 1];
            if (min_x >= 0) count -= count_point[min_x][max_y - 1];
            if (min_y >= 0) count -= count_point[max_x - 1][min_y];
            if (min_x >= 0 && min_y >= 0) count += count_point[min_x][min_y];    
            
            if (count == 0) {
                total += 1;
            }
        }
    }
    
    return total;
    

    
    
    
    
    
    return 0;
    
    
    
    
    // unordered_map<int, int> x_to_index;
    // unordered_map<int, int> y_to_index;
    
    
}


// 1. 값을 인덱스로 변환할 수 있는 x table, y table 만들기 => 2 ** 31 에서 5000 size
// 2. 이를 통해 좌표 압축을 수행한 결과를 compressed_points에 저장
// 3. s[i][j]: (0,0)부터 (i, j)까지의 좌표 개수
//    s[i][j] = s[i - 1][j] + s[i][j - 1] - s[i][j]
//    if (i,j) in compressed_points s[i][j] += 1
// for i in range(0..len(compressed_points)):
//   for j in range(i + 1..len(compressed_points)):
//     x1, y1 = compressed_points[i]
//     x2, y2 = compressed_points[j]
//     if s[x1][y1] - s[x2][y2] == 0:
//       total += 1
// return total