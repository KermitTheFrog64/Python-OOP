from classes import *

Alice = Teacher("Alice", 4, "ICT", 763)
Alice.set_age(36)
Alice.display_info()
Alice.premium()
Alice.address = Address(
    '121 Admin Rd',
    'Concord',
    'NH',
    '03301'
)

Bob = Student("Bob", 3, "Clouds")
Bob.set_age(20)
Bob.display_info()
Bob.grant()
