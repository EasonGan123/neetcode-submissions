class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numbers = {}
        for num in nums:
            numbers[num] = numbers.get(num,0) + 1
        
        ordered = sorted(numbers, key=numbers.get, reverse=True)
        return ordered[:k]


        