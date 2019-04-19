local available = "$AVAILABLE$"
local randomized = "$RANDOMIZED$"
local hashstring = "$HASHSTRING$"
local rand_ord = '$RANDORD$'

local DEF_LEN = 260

local seed_func = os.time
local function to_table(str)

	local res = {}
	for i = 1, #str do
		res[i] = str:sub(i, i)
	end

	return res

end

local function get_pos(val, table)

	for k, v in pairs(table) do
		if v == val then
			return k
		end
	end
	return false

end

local function get_sum(value)

	local sums = 0

	for k, v in ipairs(to_table(value)) do
		sums = sums + string.byte(v) + (k-1) --0, 1, 2, 3, 4....
	end

	return sums

end


local function get_request()

	math.randomseed(seed_func())
	local strlen = math.random(50, 80)

	local pos = math.random(1, DEF_LEN-strlen)+1
	local substr = hashstring:sub(pos+1, pos+strlen)
	local rand_ord_local = math.random(1, rand_ord) + 1
	--print(pos)
	--print(substr)
	--print(rand_ord_local)

	local moved_av = randomized:sub(rand_ord_local, -1) .. randomized:sub(1, rand_ord_local-1)

	local newstr = ""
	for _, v in pairs(to_table(substr)) do

		local indx = get_pos(v, to_table(randomized))
		newstr = newstr .. moved_av:sub(indx, indx)
	end

	return randomized:sub(rand_ord_local, rand_ord_local) .. string.format("%.2x", pos) .. newstr

end

local function check_activation_code(request, activation)

	local request_tab = to_table(request)
	local activation_tab = to_table(activation)

	if not get_pos(request_tab[1], to_table(randomized)) or request:len() < 10 then
		return false
	end

	if tonumber(request:sub(2, 3), 16) == nil then
		return false
	end

	local rand_ord_local = get_pos(request_tab[1], to_table(randomized))
	local pos = tonumber(request:sub(2, 3), 16)
	--print(rand_ord_local)
	--print(pos)

	local moved_av = randomized:sub(rand_ord_local, -1) .. randomized:sub(1, rand_ord_local-1)
	--print(moved_av)

	local oldstr = ""
	for _, i in pairs(to_table(request:sub(4, -1))) do
		local indx = get_pos(i, to_table(moved_av))
		oldstr = oldstr .. randomized:sub(indx, indx)
	end
	--print("---")
	--print(oldstr)
	--print("---")

	local ln = oldstr:len()
	if hashstring:sub(pos+1, pos+ln) ~= oldstr then
		return false
	end

	local sumsr = 0
	for k, v in pairs(to_table(oldstr)) do
		sumsr = sumsr + string.byte(v) + (k-1) + pos
	end

	local sums = get_sum(hashstring)
	sumsr = sums - sumsr
	--print(sumsr)

	local actpos = get_pos(activation_tab[1], to_table(randomized)) + 1
	--print(actpos)

	local code = activation:sub(actpos, actpos + 3)
	--print(code)

	local hexad = ""
	for i = 1, #code do
		hexad = hexad .. string.format("%x", get_pos(code:sub(i, i), to_table(randomized)) - i)
	end

	--print(hexad)
	
	local ax = activation:sub(-1, -1)
	local sumnstrlen = get_pos(ax, to_table(randomized))-1
	local sumstr = activation:sub(-(sumnstrlen+1), -2)
	local strsum = ""
	for i, v in pairs(to_table(sumstr)) do
		strsum = strsum..tostring(get_pos(v, to_table(randomized))-1)
	end

	--print(sumnstrlen, sumstr, strsum, get_sum(activation:sub(1, -(sumnstrlen+2))) )
	return tonumber(hexad, 16) == sumsr and tonumber(strsum) == get_sum(activation:sub(1, -(sumnstrlen+2)))

end

print("Your request code is:")
print(get_request())
print()
print("Enter request code:")
request = io.read()
print("Enter activation code:")
activation = io.read()
print("")
print("Your code is:")
print(check_activation_code(request, activation) and "Valid" or "Invalid")