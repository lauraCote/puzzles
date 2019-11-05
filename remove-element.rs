struct Solution {}
impl Solution {
    pub fn remove_element(nums: &mut Vec<i32>, val: i32) -> i32 {
        if nums.len() == 0 {
            return 0;
        }

        let mut index = 0;
        let mut last_index = nums.len();

        while index < last_index {
            if nums[index] == val {
                last_index -= 1;
                let last_val = nums[last_index];
                nums[last_index] = val;
                nums[index] = last_val;
            } else {
                index += 1;
            }
        }

        nums.truncate(index);
        return nums.len() as i32; 
    }
}

fn main() {
    let mut vec: Vec<i32> = Vec::new();
    vec.push(2);
    vec.push(3);
    vec.push(3);
    vec.push(3);
    vec.push(2);
    println!("{}", Solution::remove_element(&mut vec, 3));
}