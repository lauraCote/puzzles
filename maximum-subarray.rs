struct Solution {}
impl Solution {
    pub fn max_sub_array(nums: Vec<i32>) -> i32 {
        if nums.len() == 0 {
            return 0;
        }

        let mut local_max = nums[0];
        let mut global_max = local_max;

        for num in nums.iter().skip(1) {
            local_max = std::cmp::max(*num, *num + local_max);
            if local_max > global_max {
                global_max = local_max
            }
        }

        return global_max;
    }
}

fn main() {
    let mut vec: Vec<i32> = Vec::new();
    vec.push(1);
    println!("{}", Solution::max_sub_array(vec));
}