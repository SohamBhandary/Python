device_status="active"
temp=38
if device_status=="active":
    if temp>35:
        print("high temp")
    else:
        print("normal")
else:
    print("offline")