// question
// Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue. We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

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
