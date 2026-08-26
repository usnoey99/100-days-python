from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean

app = Flask(__name__)

# CREATE DB
class Base(DeclarativeBase):
    pass
# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

    def to_dict(self):

        return {column.name: getattr(self, column.name) for column in self.__table__.columns}

with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record
@app.route("/random", methods=["GET"])
def get_random_cafe():
    random_cafe = Cafe.query.order_by(db.func.random()).first()
    return jsonify(random_cafe.to_dict())

@app.route("/cafes", methods=["GET"])
def get_all_cafes():
    all_cafes = Cafe.query.all()
    return jsonify([cafe.to_dict() for cafe in all_cafes])

@app.route("/search", methods=["GET"])
def search_cafes():
    location = request.args.get("location")
    cafes = Cafe.query.filter(Cafe.location == location).all()

    if not cafes:
        return jsonify(error={
            "Not Found": "Sorry, no cafe with that location."
        })

    return jsonify([cafe.to_dict() for cafe in cafes])


# HTTP POST - Create Record
@app.route("/add", methods=["POST"])
def add_cafe():
    data = request.get_json()

    new_cafe = Cafe(
        name=data["name"],
        map_url=data["map_url"],
        img_url=data["img_url"],
        location=data["location"],
        seats=data["seats"],
        has_toilet=data["has_toilet"],
        has_wifi=data["has_wifi"],
        has_sockets=data["has_sockets"],
        can_take_calls=data["can_take_calls"],
        coffee_price=data["coffee_price"],
    )
    db.session.add(new_cafe)
    db.session.commit()

    return jsonify(new_cafe.to_dict())

# HTTP PUT/PATCH - Update Record
@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def update_cafe_price(cafe_id):
    cafe = Cafe.query.get(cafe_id)

    if cafe:
        new_price = request.args.get("new_price")
        cafe.coffee_price = new_price
        db.session.commit()

        return jsonify(cafe.to_dict())

    return jsonify(error={
        "Not Found": "Sorry, no cafe with that id."
    })

# HTTP DELETE - Delete Record
@app.route("/delete/<int:cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):
    api_key = request.args.get("api_key")

    if api_key == "TopSecretAPIKey":
        cafe = Cafe.query.get(cafe_id)

        if cafe:
            db.session.delete(cafe)
            db.session.commit()
            return jsonify(response={"success": "Cafe deleted successfully."})
        return jsonify(error={"Not Found": "Sorry, no cafe with that id."}), 404
    return jsonify(error={"Forbidden": "Sorry, that's not allowed. Please provide the correct API key."}), 403

if __name__ == '__main__':
    app.run(debug=True)
