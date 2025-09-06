pk =2026
a_count=0
b_count=0
c_count=0
d_count=0
e_count=0
n_count=0

tot  =a_count + b_count + c_count+d_count+e_count+n_count
def win():
    if(a_count>b_count and a_count>c_count and a_count>d_count and a_count>e_count):
        print("The winner is ADMK, the total vote is", a_count)

    elif(b_count>a_count and b_count>c_count and b_count>d_count and b_count>e_count):
        print("The winner is DMK, the total vote is", b_count)

    elif (c_count > a_count and c_count > b_count and c_count > d_count and c_count > e_count):
        print("The winner is TVK, the total vote is", c_count)

    elif (d_count > a_count and d_count > b_count and d_count > c_count and d_count > e_count):
        print("The winner is BJP, the total vote is", d_count)

    elif (e_count > a_count and e_count > b_count and e_count > c_count and e_count > d_count):
        print("The winner is CON, the total vote is", e_count)

while True:
    vote=input("Select the partis\n"
               "1.ADMK\n"
               "2.DMK\n"
               "3.TVK\n"
               "4.BJP\n"
               "5.CON\n"
               "6.NOTA\n"
               "7.EXIT\n")
    if (vote=="ADMK"):
        a_count+=1

    elif (vote=="DMK"):
        b_count+=1

    elif (vote=="TVK"):
        c_count+=1

    elif (vote=="BJP"):
        d_count+=1
    elif (vote=="CON"):
        e_count+=1

    elif (vote=="NOTA"):
        n_count+=1

    elif (vote=="EXIT"):
        get=int(input("Enter the secret passkey:"))
        if (get==pk):
            print("The total count of ADMK:",a_count)
            print("The total count of DMK:", b_count)
            print("The total count of TVK:", c_count)
            print("The total count of BJP:", d_count)
            print("The total count of CON:", e_count)
            print("The total count of NOTA:", n_count)
            tot = a_count + b_count + c_count + d_count + e_count + n_count
            print("The total vote in this booth:", tot)
            win()

            break
        else:
            print("incorrect Password!")

    else:
        print("Please Select the Proper parties!")
