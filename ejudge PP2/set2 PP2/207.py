n = input()
list_ = list(map(int, input().split()))

max_ = max(list_)
position = list_.index(max_)

print(position + 1)