class Solution:
    def MaxK(self, arr):
        def check(arr):
            newarr = []
            arr = set(arr)
            for i in arr:
                if -i in arr:
                    newarr.append(i)
            return newarr
        def Big(newarr):
            if not newarr:
                return -1
            max = 0
            for i in newarr:
                if(max < i):
                    max = i
            return max
        
        result = check(arr)
        maxvlaue = Big(result)
        return maxvlaue

if __name__ == "__main__":
    arr = [-1,2,-3,3,4,7,-4]
    solu = Solution()
    print(solu.MaxK(arr))
