from config import db, app
from models import Tech, Car, Part, Note, Image

with app.app_context():
    Tech.query.delete()
    Car.query.delete()
    Part.query.delete()
    Note.query.delete()
    Image.query.delete()

    t = Tech(name = "Mark", rate = 25)
    db.session.add(t)
    db.session.commit()

    t = Tech(name = "ex", rate = 7.25)
    db.session.add(t)
    db.session.commit()

    c = Car(
        make = "Subaru",
        model = "WRX",
        year = 2005,
        tech_id = 1,
        owner = "Mark",
    )
    db.session.add(c)
    db.session.commit()

    c = Car(
        make = "Toyota",
        model = "Celica",
        year = 1998,
        tech_id = 2,
        owner = "Customer 1"
    )
    db.session.add(c)
    db.session.commit()

    p = Part(
        name = "turbo",
        price = 1600,
        hours = 5,
        car_id = 1,
    )
    db.session.add(p)
    db.session.commit()

    p = Part(
        name = "injectors",
        price = 500,
        hours = 2,
        car_id = 2
    )
    db.session.add(p)
    db.session.commit()

    n = Note(
        note = "lalalala",
        car_id = 1,
        tech_id = 1,
    )
    db.session.add(n)
    db.session.commit()

    n = Note(
        note = "hahahaha",
        car_id = 2,
        tech_id = 2,
    )
    db.session.add(n)
    db.session.commit()

    #_____________________CHATGPTvvvvv_____________________________

    # Creating Techs
    tech1 = Tech(name="Tech1", rate=30)
    tech2 = Tech(name="Tech2", rate=35)
    db.session.add(tech1)
    db.session.add(tech2)
    db.session.commit()

    # Creating Cars for Tech1
    car1_tech1 = Car(
        make="Honda",
        model="Civic",
        year=2010,
        tech_id=tech1.id,  # Assuming tech_id is auto-assigned
        owner="Owner1"
    )
    car2_tech1 = Car(
        make="Mazda",
        model="3",
        year=2015,
        tech_id=tech1.id,
        owner="Owner2"
    )
    db.session.add(car1_tech1)
    db.session.add(car2_tech1)
    db.session.commit()

    # Creating Cars for Tech2
    car1_tech2 = Car(
        make="Ford",
        model="Focus",
        year=2018,
        tech_id=tech2.id,
        owner="Owner3"
    )
    car2_tech2 = Car(
        make="Chevrolet",
        model="Malibu",
        year=2020,
        tech_id=tech2.id,
        owner="Owner4"
    )
    db.session.add(car1_tech2)
    db.session.add(car2_tech2)
    db.session.commit()

    # Creating Parts for Car1 and Car2 of Tech1
    part1_car1_tech1 = Part(
        name="Brake Pads",
        price=150,
        hours=2,
        car_id=car1_tech1.id
    )
    part2_car1_tech1 = Part(
        name="Oil Filter",
        price=25,
        hours=1,
        car_id=car1_tech1.id
    )
    part1_car2_tech1 = Part(
        name="Battery",
        price=100,
        hours=1.5,
        car_id=car2_tech1.id
    )
    part2_car2_tech1 = Part(
        name="Spark Plugs",
        price=50,
        hours=1,
        car_id=car2_tech1.id
    )
    db.session.add(part1_car1_tech1)
    db.session.add(part2_car1_tech1)
    db.session.add(part1_car2_tech1)
    db.session.add(part2_car2_tech1)
    db.session.commit()

    # Creating Parts for Car1 and Car2 of Tech2
    part1_car1_tech2 = Part(
        name="Transmission Fluid",
        price=120,
        hours=3,
        car_id=car1_tech2.id
    )
    part2_car1_tech2 = Part(
        name="Air Filter",
        price=30,
        hours=0.5,
        car_id=car1_tech2.id
    )
    part1_car2_tech2 = Part(
        name="Headlights",
        price=200,
        hours=2,
        car_id=car2_tech2.id
    )
    part2_car2_tech2 = Part(
        name="Tail Lights",
        price=80,
        hours=1.5,
        car_id=car2_tech2.id
    )
    db.session.add(part1_car1_tech2)
    db.session.add(part2_car1_tech2)
    db.session.add(part1_car2_tech2)
    db.session.add(part2_car2_tech2)
    db.session.commit()

    # Creating Notes for Car1 and Car2 of Tech1
    note1_car1_tech1 = Note(
        note="Replaced brake pads and oil filter.",
        car_id=car1_tech1.id,
        tech_id=tech1.id
    )
    note2_car1_tech1 = Note(
        note="Oil change and new brake pads installed.",
        car_id=car1_tech1.id,
        tech_id=tech1.id
    )
    note1_car2_tech1 = Note(
        note="Installed new battery and spark plugs.",
        car_id=car2_tech1.id,
        tech_id=tech1.id
    )
    note2_car2_tech1 = Note(
        note="Battery replacement and spark plug installation completed.",
        car_id=car2_tech1.id,
        tech_id=tech1.id
    )
    db.session.add(note1_car1_tech1)
    db.session.add(note2_car1_tech1)
    db.session.add(note1_car2_tech1)
    db.session.add(note2_car2_tech1)
    db.session.commit()

    # Creating Notes for Car1 and Car2 of Tech2
    note1_car1_tech2 = Note(
        note="Transmission fluid change and air filter replacement.",
        car_id=car1_tech2.id,
        tech_id=tech2.id
    )
    note2_car1_tech2 = Note(
        note="Changed transmission fluid and air filter.",
        car_id=car1_tech2.id,
        tech_id=tech2.id
    )
    note1_car2_tech2 = Note(
        note="Replaced headlights and tail lights.",
        car_id=car2_tech2.id,
        tech_id=tech2.id
    )
    note2_car2_tech2 = Note(
        note="Installed new headlights and tail lights.",
        car_id=car2_tech2.id,
        tech_id=tech2.id
    )
    db.session.add(note1_car1_tech2)
    db.session.add(note2_car1_tech2)
    db.session.add(note1_car2_tech2)
    db.session.add(note2_car2_tech2)
    db.session.commit()