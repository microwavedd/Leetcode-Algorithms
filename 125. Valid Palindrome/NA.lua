local function isPalindrome(s)
    local y = {}
    for i = 1, #s do
        if string.match(s:sub(i, i), "%a") or string.match(s:sub(i, i), "%d") then
            table.insert(y, s:sub(i, i))
        end
    end
    local str = table.concat(y)
    return string.lower(str) == string.reverse(string.lower(str))
end

