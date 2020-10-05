# Complement of Base 10 Integer

class Solution:
	def bitwiseComplement(self, N: int) -> int:
		if N == 0:
			return 1

		binary_num = ''
		while N != 0:
			rem = N % 2
			binary_num += str(rem)
			N = N // 2
		binary_num = binary_num[::-1]

		complement_num = ''
		for i in range(len(binary_num)):
			if binary_num[i] == '1':
				complement_num += '0'
			if binary_num[i] == '0':
				complement_num += '1'

		complement_num = complement_num[::-1]
		result = 0
		for i in range(len(complement_num)):
			result += int(complement_num[i]) * (2 ** i)

		return result
