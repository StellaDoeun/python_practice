from itertools import combinations

card_num, target_sum = map(int, input().split())
card_list = list(map(int, input().split()))
biggest_sum = 0

for cards in combinations(card_list, 3):
    temp_sum = sum(cards)
    if biggest_sum < temp_sum <= target_sum:
        biggest_sum = temp_sum

print(biggest_sum)

# mylist[2,3,4,5,6]
# newlist = [i for i in mylist if i%2==0]
# newlist 출력시 [2,4,6] 만 원소로 출력
