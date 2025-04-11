from myApp import db, app, User, Stock

def setupDatabase():
    with app.app_context():
        db.create_all()
        adminUser = User.query.filter_by(username="admin").first()
        if not adminUser:
            admin = User(username="patson", password="dubai2020!", role="admin")
            testUser1 = User(username="sharafdg", password="passsw0rd!")
            testUser2 = User(username="jumbo", password="discount@123")
            testUser3 = User(username="emax", password="123456789")
            testUser4 = User(username="apple", password="moneyyy123")
            testUser5 = User(username="aryan", password="aryan@123")
            testUser6 = User(username="abdi", password="basketball")
            testUser7 = User(username="tech4uManager", password="techy1234", role='admin')
            db.session.add_all([
                admin, testUser1, testUser2, testUser3, testUser4, testUser5, testUser6, testUser7
            ])
            db.session.commit()
            print("Users added")
            
        else:
            print("Users already exists.")


        # Adding data to table Stock
        if Stock.query.first() is None:
            stock1 = Stock(name="iPad Air (3rd Generation, 2019)", manufacturer="Apple", quantity=15, price=1800.00)
            stock2 = Stock(name="Galaxy S21 5G", manufacturer="Samsung", quantity=20, price=2599.00)
            stock3 = Stock(name="27MR400-B 27-Inch IPS Monitor", manufacturer="LG", quantity=15, price=318.00)
            stock4 = Stock(name="WF-1000XM4 Noise Cancelling Earbuds", manufacturer="Sony", quantity=25, price=672.41)
            stock5 = Stock(name="Forerunner 945 Smartwatch", manufacturer="Garmin", quantity=18, price=2319.00)
            stock6 = Stock(name="Xbox Series X 1TB Console", manufacturer="Microsoft", quantity=12, price=1879.00)
            stock7 = Stock(name="Flip 5 Portable Bluetooth Speaker", manufacturer="JBL", quantity=30, price=290.00)
            stock8 = Stock(name="Expansion Portable 2TB External Hard Drive", manufacturer="Seagate", quantity=20, price=240.00)
            stock9 = Stock(name="EOS 90D DSLR Camera with 18-135mm Lens", manufacturer="Canon", quantity=10, price=7521.00)
            stock10 = Stock(name="55-Inch 4K UHD Smart LED TV (UA55AU7000)", manufacturer="Samsung", quantity=8, price=1159.99)
            stock11 = Stock(name="Nighthawk AX12 WiFi 6 Router (RAX120)", manufacturer="Netgear", quantity=15, price=1995.00)
            stock12 = Stock(name="Kindle Paperwhite Signature Edition (11th Gen)", manufacturer="Amazon", quantity=22, price=859.00)
            stock13 = Stock(name="PowerCore 20100mAh Portable Charger", manufacturer="Anker", quantity=35, price=100.00)
            stock14 = Stock(name="PRO X Mechanical Gaming Keyboard", manufacturer="Logitech", quantity=17, price=840.00)
            stock15 = Stock(name="Charge 4 Fitness and Activity Tracker", manufacturer="Fitbit", quantity=25, price=264.00)
            stock16 = Stock(name="Quest 2 VR Headset", manufacturer="Oculus", quantity=9, price=1500.00)
            stock17 = Stock(name="Hue Smart Light Bulb", manufacturer="Philips", quantity=40, price=120.00)
            stock18 = Stock(name="DR900X Dash Cam", manufacturer="BlackVue", quantity=14, price=1100.00)
            stock19 = Stock(name="Intuos Pro Graphics Tablet", manufacturer="Wacom", quantity=11, price=1800.00)
            stock20 = Stock(name="QuietComfort 35 II Noise-Canceling Headphones", manufacturer="Bose", quantity=13, price=1500.00)

            db.session.add_all([
                stock1, stock2, stock3, stock4, stock5
            ])
            # stock6, stock7, stock8, stock9, stock10,
                # stock11, stock12, stock13, stock14, stock15, stock16, stock17, stock18, stock19, stock20

            db.session.commit()
            print("Stock items added.")
        else:
            print("Stock items already exist.")
if __name__ == "__main__":
    setupDatabase()
    print("\nDatabase setup complete.")
