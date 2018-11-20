input = nil

if File.basename(Dir.getwd).match?(/day\d\d$/) then
    input = File.readlines('input.txt')
else
    input = File.readlines('day02/input.txt')
end

checksum = 0
# puts input
input.each do |line|
    max = -1
    min = -1

    line.split("\t").each do |val|
        val_int = val.to_i
        max = (max == -1 || max < val_int) ? val_int : max
        min = (min == -1 || min > val_int) ? val_int : min
        puts max, min
    end

    checksum += max - min
end

puts checksum