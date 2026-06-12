#include <vector>
#include <algorithm>

using namespace std;

long long solution(vector<vector<int>> land, int P, int Q) {
    // 1. 2차원 배열을 1차원 배열로 평탄화 (탐색 횟수를 줄이기 위한 핵심)
    vector<long long> blocks;
    // 메모리 재할당 오버헤드를 막기 위해 미리 공간 확보 (N*N 최대 90000)
    blocks.reserve(land.size() * land[0].size()); 
    
    for (const auto& row : land) {
        for (int h : row) {
            blocks.push_back(h);
        }
    }
    
    // 2. 오름차순 정렬 (비용 갱신을 O(1)로 하기 위한 빌드업)
    sort(blocks.begin(), blocks.end());
    
    long long n = blocks.size();
    long long current_height = blocks[0];
    long long cost = 0;
    
    // 3. 목표 높이를 '가장 낮은 블록'으로 맞췄을 때의 초기 비용 계산
    // 모두 깎기만 하면 되므로 Q 비용만 발생
    for (long long b : blocks) {
        cost += (b - current_height) * Q;
    }
    
    long long min_cost = cost;
    
    // 4. 높이를 다음 블록 크기로 한 칸씩 올려가며 비용 갱신
    for (long long i = 1; i < n; ++i) {
        // 높이가 같다면 비용도 같으므로 패스
        if (blocks[i] == blocks[i - 1]) continue;
        
        long long diff = blocks[i] - blocks[i - 1];
        
        // i개의 블록은 diff만큼 더 쌓아야 함 (P 비용 발생)
        cost += diff * i * P;
        // (n - i)개의 블록은 diff만큼 덜 깎아도 됨 (Q 비용 절감)
        cost -= diff * (n - i) * Q;
        
        if (cost < min_cost) {
            min_cost = cost;
        }
    }
    
    return min_cost;
}