# [Silver V] 비밀번호 발음하기 - 4659 

[문제 링크](https://www.acmicpc.net/problem/4659) 

### 성능 요약

메모리: 32412 KB, 시간: 36 ms

### 분류

구현, 문자열

### 제출 일자

2026년 3월 30일 14:33:02

### 문제 설명

<p>Password security is a tricky thing. Users prefer simple passwords that are easy to remember (like buddy), but such passwords are often insecure. Some sites use random computer-generated passwords (like xvtpzyo), but users have a hard time remembering them and sometimes leave them written on notes stuck to their computer. One potential solution is to generate "pronounceable" passwords that are relatively secure but still easy to remember.</p>

<p>FnordCom is developing such a password generator. You work in the quality control department, and it's your job to test the generator and make sure that the passwords are acceptable. To be acceptable, a password must satisfy these three rules:</p>

<ol>
	<li>It must contain at least one vowel.</li>
	<li>It cannot contain three consecutive vowels or three consecutive consonants.</li>
	<li>It cannot contain two consecutive occurrences of the same letter, except for 'ee' or 'oo'.</li>
</ol>

<p>(For the purposes of this problem, the vowels are 'a', 'e', 'i', 'o', and 'u'; all other letters are consonants.) Note that these rules are not perfect; there are many common/pronounceable words that are not acceptable.</p>

### 입력 

 <p>The input consists of one or more potential passwords, one per line, followed by a line containing only the word 'end' that signals the end of the file. Each password is at least one and at most twenty letters long and consists only of lowercase letters.</p>

### 출력 

 <p>For each password, output whether or not it is acceptable, using the precise format shown in the example.</p>

<p> </p>

