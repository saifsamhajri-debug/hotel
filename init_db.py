from datetime import datetime, timedelta
from hotel import create_app, db
from hotel.models import User, Room, Customer, Booking
from hotel.models import ROLE_ADMIN, ROLE_GUEST
from hotel.models import ROOM_TYPE_SINGLE, ROOM_TYPE_DOUBLE, ROOM_TYPE_SUITE, ROOM_TYPE_DELUXE

def init_db():
    app = create_app()
    with app.app_context():
        # Drop all tables
        db.drop_all()

        # Create all tables
        db.create_all()

        # Create admin user
        admin = User(
            username='admin',
            email='admin@hotel.com',
            password='admin123',
            role=ROLE_ADMIN
        )

        # Create guest user
        guest = User(
            username='guest',
            email='guest@example.com',
            password='guest123',
            role=ROLE_GUEST
        )

        db.session.add(admin)
        db.session.add(guest)

        # Create rooms
        rooms = [
            Room(room_number='101', room_type=ROOM_TYPE_SINGLE, price_per_night=100, capacity=1,
                 description='غرفة مفردة مع سرير واحد وحمام خاص وتلفزيون وواي فاي'),
            Room(room_number='102', room_type=ROOM_TYPE_SINGLE, price_per_night=100, capacity=1,
                 description='غرفة مفردة مع سرير واحد وحمام خاص وتلفزيون وواي فاي'),
            Room(room_number='201', room_type=ROOM_TYPE_DOUBLE, price_per_night=180, capacity=2,
                 description='غرفة مزدوجة مع سريرين وحمام خاص وتلفزيون وواي فاي وثلاجة صغيرة'),
            Room(room_number='202', room_type=ROOM_TYPE_DOUBLE, price_per_night=180, capacity=2,
                 description='غرفة مزدوجة مع سريرين وحمام خاص وتلفزيون وواي فاي وثلاجة صغيرة'),
            Room(room_number='301', room_type=ROOM_TYPE_SUITE, price_per_night=300, capacity=4,
                 description='جناح فاخر مع غرفة نوم وصالة وحمامين وتلفزيون وواي فاي وثلاجة'),
            Room(room_number='302', room_type=ROOM_TYPE_DELUXE, price_per_night=500, capacity=4,
                 description='جناح ديلوكس مع غرفتي نوم وصالة وحمامين وتلفزيون وواي فاي وثلاجة ومطبخ صغير')
        ]

        for room in rooms:
            db.session.add(room)

        # لا نقوم بإنشاء عملاء افتراضيين

        # Commit to get IDs
        db.session.commit()

        # لا نقوم بإنشاء حجوزات افتراضية

        # Commit all changes
        db.session.commit()

        print('Database initialized with sample data!')

if __name__ == '__main__':
    init_db()
