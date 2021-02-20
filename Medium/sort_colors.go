// question
// Input: nums = [2,0,2,1,1,0]
// Output: [0,0,1,1,2,2]

func sortColors(nums []int)  {
    for i := 1; i < len(nums); i++ {
        for j := 0; j < len(nums) - 1; j++ {
            if nums[j] > nums[j + 1] {
                temp := nums[j]
                nums[j] = nums[j + 1]
                nums[j + 1] = temp
            }
        }
    }
}
