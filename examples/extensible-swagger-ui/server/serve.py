import connexion
from flask import render_template
from pathlib import Path
from os import path
from specsynthase.specbuilder import SpecBuilder
from db.mongo import MongoDb


spec_dir = "./specs"
current_dir = path.dirname(__file__)
spec_path = Path(f"{current_dir}/{spec_dir}").resolve()

spec = SpecBuilder()\
    .add_spec(spec_path.joinpath("cm4.yaml")) \
    .add_spec(spec_path.joinpath("vm.yaml")) \
    .add_spec(spec_path.joinpath("flavor.yaml"))\
    .add_spec(spec_path.joinpath("image.yaml"))

app = connexion.App(__name__, specification_dir=spec_dir)
app.add_api(spec)


@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    # Sets default db connection and build
    # if it is not already generated.
    mongo = MongoDb()
    mongo.check_db()

    app.run(port=8080, debug=True)
