#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

int solution(int n, vector<vector<int>> data) {
    vector<int> x_list;
    vector<int> y_list;
    
    // 1. 모든 x좌표와 y좌표를 따로 모읍니다.
    for (int i = 0; i < n; i++) {
        x_list.push_back(data[i][0]);
        y_list.push_back(data[i][1]);
    }
    
    // 2. 좌표 압축을 위해 정렬하고 중복을 제거합니다.
    sort(x_list.begin(), x_list.end());
    sort(y_list.begin(), y_list.end());
    x_list.erase(unique(x_list.begin(), x_list.end()), x_list.end());
    y_list.erase(unique(y_list.begin(), y_list.end()), y_list.end());
    
    // 고유한 x, y 좌표의 개수
    int max_x = x_list.size();
    int max_y = y_list.size();
    
    // 3. 2차원 누적 합 배열 생성 (1-based index를 사용하기 위해 +1 크기로 만듦)
    // S[i][j]는 (1,1)부터 (i,j)까지의 직사각형 내에 있는 점의 개수입니다.
    vector<vector<int>> S(max_x + 1, vector<int>(max_y + 1, 0));
    
    // 주어진 데이터의 원본 좌표를 압축된 인덱스로 변환하고 배열에 점을 찍습니다.
    vector<pair<int, int>> points(n);
    for (int i = 0; i < n; i++) {
        // lower_bound로 값이 들어갈 인덱스를 찾습니다 (0-based)
        int comp_x = lower_bound(x_list.begin(), x_list.end(), data[i][0]) - x_list.begin();
        int comp_y = lower_bound(y_list.begin(), y_list.end(), data[i][1]) - y_list.begin();
        
        points[i] = {comp_x, comp_y};
        S[comp_x + 1][comp_y + 1] = 1; // 누적합을 위해 1-based 인덱스에 저장
    }
    
    // 4. 누적 합 계산
    for (int i = 1; i <= max_x; i++) {
        for (int j = 1; j <= max_y; j++) {
            S[i][j] += S[i - 1][j] + S[i][j - 1] - S[i - 1][j - 1];
        }
    }
    
    int answer = 0;
    
    // 5. 점들을 x좌표 기준으로 정렬 (순차적 탐색을 위함)
    sort(points.begin(), points.end());
    
    // 6. O(N^2)으로 모든 점의 쌍을 검사합니다.
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            int x1 = points[i].first;
            int y1 = points[i].second;
            int x2 = points[j].first;
            int y2 = points[j].second;
            
            // 직사각형의 넓이가 0이면 텐트를 칠 수 없음
            if (x1 == x2 || y1 == y2) continue;
            
            // 두 점이 만드는 직사각형의 '내부 영역' 좌표를 구합니다. (1-based)
            int min_x = min(x1, x2) + 1;
            int max_x = max(x1, x2) - 1;
            int min_y = min(y1, y2) + 1;
            int max_y = max(y1, y2) - 1;
            
            // 두 점이 인접해 있어서 아예 내부에 공간이 없는 경우는 조건을 만족하는 것입니다.
            if (min_x > max_x || min_y > max_y) {
                answer++;
                continue;
            }
            
            // 내부 영역에 쐐기(점)가 몇 개 있는지 2차원 누적 합으로 O(1) 만에 구합니다.
            // +1은 1-based index 변환 처리용입니다.
            int count = S[max_x + 1][max_y + 1] 
                      - S[min_x][max_y + 1] 
                      - S[max_x + 1][min_y] 
                      + S[min_x][min_y];
            
            // 내부에 점이 하나도 없으면 텐트를 칠 수 있습니다.
            if (count == 0) {
                answer++;
            }
        }
    }
    
    return answer;
}