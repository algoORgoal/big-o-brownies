from functools import cmp_to_key


def comparator(a, b):
    if a[0] != b[0]:
        return b[0] - a[0]
    if a[1] != b[1]:
        return b[1] - a[1]
    return a[2] - b[2]

def solution(genres, plays):
    table = {}
    for i in range(0, len(genres)):
        genre = genres[i]
        if genre not in table:
            table[genre] = 0
        table[genre] += plays[i]

    songs = []
    for i in range(0, len(genres)):
        songs.append([table[genres[i]], plays[i], i])
    
    sorted_songs = sorted(songs, key=cmp_to_key(comparator))
    
    song_count_table = {}
    filtered_songs = []
    for song in sorted_songs:
        if song[0] in song_count_table and song_count_table[song[0]] == 2:
            continue
            
        if song[0] not in song_count_table:
            song_count_table[song[0]] = 0
        song_count_table[song[0]] += 1
        filtered_songs.append(song[2])
        
        
    return filtered_songs
    
    

# 장르별 내림차순 (높은거부터)
# 재생수 내림차순 (높은거부터)
# 인덱스 오름차순 (낮은거부터)

# 각 요소별로 [장르, 재생수, 인덱스] 담기