start = input().split(":")
end = input().split(":")
  
start_full = int(start[0])*3600 + int(start[1])*60 + int(start[2]) 
end_full = int(end[0])*3600 + int(end[1])*60 + int(end[2])
  
between = end_full - start_full

b_t = between // 3600
b_m = (between - b_t*3600) // 60
b_s = (between - b_t*3600 - b_m*60)
print(f"{b_t}:{b_m}:{b_s}")