"""
Script to update the database with new fields and tables
"""
import sqlite3
import os
from hotel import create_app, db

app = create_app()

with app.app_context():
    # Get database path
    db_path = os.path.join(app.instance_path, 'hotel.db')

    print(f"Updating database at: {db_path}")

    # Connect to database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    try:
        # Check if columns already exist
        cursor.execute("PRAGMA table_info(bookings)")
        columns = [column[1] for column in cursor.fetchall()]

        # Add new columns to bookings table if they don't exist
        if 'actual_check_in_time' not in columns:
            cursor.execute("ALTER TABLE bookings ADD COLUMN actual_check_in_time DATETIME")
            print("✓ Added actual_check_in_time column to bookings table")
        else:
            print("- actual_check_in_time column already exists")

        if 'actual_check_out_time' not in columns:
            cursor.execute("ALTER TABLE bookings ADD COLUMN actual_check_out_time DATETIME")
            print("✓ Added actual_check_out_time column to bookings table")
        else:
            print("- actual_check_out_time column already exists")

        # Create services table if it doesn't exist
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS services (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                booking_id INTEGER NOT NULL,
                service_type VARCHAR(50) NOT NULL,
                service_name VARCHAR(100) NOT NULL,
                quantity INTEGER DEFAULT 1,
                price FLOAT NOT NULL,
                total_price FLOAT NOT NULL,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                notes TEXT,
                FOREIGN KEY (booking_id) REFERENCES bookings(id)
            )
        """)
        print("✓ Created/verified services table")

        # Commit changes
        conn.commit()
        print("\n✅ Database updated successfully!")

    except Exception as e:
        conn.rollback()
        print(f"\n❌ Error updating database: {e}")
        raise
    finally:
        conn.close()

