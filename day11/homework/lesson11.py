#მომხარებელს შემოატანინეთ მშობლების ასაკი, დედის და მამის ასაკი, შემდეგ თუ დედის ასაკი მეტი იქნება მამის ასაკზე
        #დაგვიბეჭდოს რომ დედა დიდი მამაზე, თუ პირიქით მამის ასაკი მეტი იქნება დედის ასაკზე მაგ შემთხვევაში დაგვიბეჭდოს 
        #რომ მამა დიდია დედაზე. მინიშნება დაგჭირდებათ (if)


parent_mom = int(input("what is your mom's age?:  "))
parent_dad = int(input("what is your dad's age?:  "))


if parent_mom > parent_dad:
    print("mom is older")

if  parent_mom < parent_dad:
    print("dad is older")