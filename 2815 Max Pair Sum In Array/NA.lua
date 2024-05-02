local function maxSum(nums)
    local temp = 0
    local l = #nums
    for i = 1, l - 1 do
        local num1 = math.max(tonumber(nums[i]:sub(1, 1)), tonumber(nums[i]:sub(2, 2)), tonumber(nums[i]:sub(3, 3)))
        for j = i + 1, l do
            local num2 = math.max(tonumber(nums[j]:sub(1, 1)), tonumber(nums[j]:sub(2, 2)), tonumber(nums[j]:sub(3, 3)))
            if num1 == num2 then
                temp = math.max(temp, nums[i] + nums[j])
            end
        end
    end
    return temp == 0 and -1 or temp
end

