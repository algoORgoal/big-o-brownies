# [Silver I] 카잉 달력 - 6064 

[문제 링크](https://www.acmicpc.net/problem/6064) 

### 성능 요약

메모리: 34536 KB, 시간: 792 ms

### 분류

수학, 브루트포스 알고리즘, 정수론, 중국인의 나머지 정리

### 제출 일자

2026년 3월 27일 18:02:12

### 문제 설명

<p>It was recently revealed by the ICPC excavation team that the Inca Empire was established just after the Cain Empire which was a splendid civilization that flourished in South America. It is believed that the people in the Cain Empire used an interesting odd calendar. In their calendar, a year was represented by <x:y>, where x and y are natural numbers which are less than or equal to M and N, respectively. The first year, that is, the beginning of the world is represented by <1:1>. The second year is represented by <2:2>. Let <x':y'>be the following year of <x:y>. If x < M, x' = x + 1, otherwise x' = 1. Similarly, if y < N, y' = y + 1, otherwise y' = 1. The last year of their calendar is <M:N>. It is said that there was a prophecy which states the world ends in the year <M:N>. </p>

<p>For example, assume that M = 10 and N = 12. The first year is represented by <1:1>. The year <1:11> represents the 11<sup>th</sup> year, <3:1> represents the 13<sup>th</sup> year, and <10:12> represents the 60<sup>th</sup> year which is the last year. </p>

<p>Given four integers M, N, x, and y, write a program that computes the number k such that <x:y> represents the k<sup>th</sup> year, where <x:y> is the last year of the world in the Cain Calendar.</p>

### 입력 

 <p>Your program is to read from standard input. The input consists of T test cases. The number of test cases T is given in the first line of the input. Each test case consists of a single line containing four integers M, N, x, and y (1 ≤ M,N ≤ 40 000, 1 ≤ x ≤ M, 1 ≤ y ≤ N), where <M:N> is the last year of the world in the Cain Calendar.</p>

### 출력 

 <p>Your program is to write to standard output. Print exactly one line for each test case. The line should contain an integer k, where the k<sup>th</sup> year is represented by <x:y> for x and y given in the input. If there doesn’t exist a year represented by <x:y>, print -1. </p>

