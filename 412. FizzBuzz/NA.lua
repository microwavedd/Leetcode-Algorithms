function fizzBuzz(n)
    local x = {}
    for i = 1, n do
        if i % 5 == 0 and i % 3 == 0 then
            table.insert(x, "FizzBuzz")
        elseif i % 5 == 0 then
            table.insert(x, "Buzz")
        elseif i % 3 == 0 then
            table.insert(x, "Fizz")
        else
            table.insert(x, tostring(i))
        end
    end
    return x
end

