# [Gold V] 택배 배송 - 5972 

[문제 링크](https://www.acmicpc.net/problem/5972) 

### 성능 요약

메모리: 61116 KB, 시간: 268 ms

### 분류

그래프 이론, 최단 경로, 데이크스트라

### 제출 일자

2026년 4월 2일 13:20:25

### 문제 설명

<p>Farmer John must deliver a package to Farmer Dan, and is preparing to make his journey. To keep the peace, he gives a tasty treat to every cow that he meets along his way and, of course, FJ is so frugal that he would like to encounter as few cows as possible.</p>

<p>FJ has plotted a map of N (1 <= N <= 50,000) barns, connected by M (1 <= M <= 50,000) bi-directional cow paths, each with C_i (0 <= C_i <= 1,000) cows ambling along it. A cow path connects two distinct barns, A_i and B_i (1 <= A_i <= N; 1 <= B_i <= N; A_i != B_i). Two barns may be directly connected by more than one path. He is currently located at barn 1, and Farmer Dan is located at barn N.</p>

<p>Consider the following map:</p>

<pre>           [2]---
          / |    \
         /1 |     \ 6
        /   |      \
     [1]   0|    --[3]
        \   |   /     \2
        4\  |  /4      [6]
          \ | /       /1
           [4]-----[5] 
                3  </pre>

<p>The best path for Farmer John to take is to go from 1 -> 2 -> 4 -> 5 -> 6, because it will cost him 1 + 0 + 3 + 1 = 5 treats.</p>

<p>Given FJ's map, what is the minimal number of treats that he should bring with him, given that he will feed each distinct cow he meets exactly one treat? He does not care about the length of his journey.</p>

### 입력 

 <ul>
	<li>Line 1: Two space-separated integers: N and M</li>
	<li>Lines 2..M+1: Three space-separated integers: A_i, B_i, and C_i</li>
</ul>

<p> </p>

### 출력 

 <ul>
	<li>Line 1: The minimum number of treats that FJ must bring</li>
</ul>

<p> </p>

