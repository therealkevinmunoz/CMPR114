import math;
people = int(input("How many people will attend the cookout "));
hotdogs_given = int(input("How many hot dogs will be given to each person "));

total_hotdogs = people * hotdogs_given;

hotdog_buns = math.ceil(total_hotdogs / 8);
hotdog_sausages = math.ceil(total_hotdogs / 10);

hotdog_buns_remaining = (hotdog_buns * 8) - total_hotdogs
hotdog_sausages_remaining = (hotdog_sausages * 10) - total_hotdogs


print("We need " + str(hotdog_buns) + " packets of hotdog buns")
print("We need " + str(hotdog_sausages) + " packets of hotdog sausages")

if(hotdog_sausages_remaining == 0):
    print("You will have no sausages remaining")
else:
    print("You will have " + str(hotdog_sausages_remaining) + " sausages remaining");
    
if(hotdog_buns_remaining == 0):
    print("You will have no buns remaining")
else:
    print("You will have " + str(hotdog_buns_remaining) + " buns remaining");
