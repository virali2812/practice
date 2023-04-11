class Solution:

	def rowWithMax1s(self,arr, n, m):
		# code here
		result = list(map(sum, arr))
		i = max(result)
		if i == 0:
		    return -1
		else:
		    return result.index(i)
