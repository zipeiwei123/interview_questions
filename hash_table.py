#python has builtin hash table, which is basically dictionary
hash_table = {3:"Fizz", 5:"Buzz"}

N = 20

for i in hash_table:
	print(i)

hash_list = []
for i in range(1, N):
	for j in hash_table:
		if i % j == 0:
			hash_list.append(hash_table[j])
		else:
			print(i)
	if hash_list:
		print(hash_list)
	hash_list = []