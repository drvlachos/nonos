##  ΑΥΤΟ ΕΔΩ ΕΙΝΑΙ ΓΙΑ ΝΑ ΕΧΟΥΜΕ ΜΙΑ ΣΕΛΙΔΑ #
##  ΑΡΧΙΚΗ, ΚΑΙ ΑΠΟ ΕΚΕΙ ΝΑ ΣΥΝΔΕΟΝΤΑΙ Ή ΓΙΑ #
#  ΤΙΣ ΒΛΑΒΕΣ - ΟΔΗΓΟΥΣ Ή ΟΤΙ ΑΛΛΟ ΦΤΙΑΞΟΥΜΕ #

from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("/logineor.html");



if __name__ == "__main__":
    app.run(debug=True)