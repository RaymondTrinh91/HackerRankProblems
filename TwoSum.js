var twoSum = function(nums, target) {
    const dict = {}
    
    for(i = 0; i < nums.length; i++) {
        let remainder = target - nums[i]
        
        if(remainder in dict){
            return [dict[remainder], i]
        }
        
        dict[nums[i]] = i
    }
    
    // for(i=0; i<nums.length; i++){
    //     for(n=i+1; n < nums.length; n++){
    //         if(nums[i] + nums[n] == target){
    //             return [i, n]
    //         }
    //     }
    // }
};