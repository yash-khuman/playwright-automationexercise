from dataclasses import dataclass
from faker import Faker
from uuid import uuid4

fake = Faker("en_IN")
uuid = uuid4().hex[:8]

@dataclass
class User:
    username : str
    lastname : str
    email : str
    password : str
    gender : str
    birth_date : str
    birth_month : str
    birth_year : str
    company_name : str
    address1 : str
    address2 : str
    state : str
    city : str
    zipcode : str
    mobile_number : str

temp_user = User(
    username=f"{uuid}_{fake.first_name()}",
    lastname=f"{uuid}_{fake.last_name()}",
    email=f"{uuid}_{fake.email()}",
    password=f"{uuid}_{fake.password()}",
    gender="Male",
    birth_date="1",
    birth_month="8",
    birth_year="2004",
    company_name=fake.company(),
    address1=fake.address(),
    address2=fake.address(),
    state=fake.state(),
    city=fake.city(),
    zipcode=str(fake.pincode_in_state()),
    mobile_number=fake.phone_number()
)

main_user = User(
    username="testmainuser",
    lastname="test",
    email="testmainuser@test.com",
    password="test123",
    gender="Male",
    birth_date="1",
    birth_month="8",
    birth_year="2004",
    company_name="test_company",
    address1="test_add1",
    address2="test_add2",
    state="maharashtra",
    city="mumbai",
    zipcode="123456",
    mobile_number="1234567890"
)