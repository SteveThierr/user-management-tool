from flask import Flask, render_template, request, redirect, url_for, flash
from users import get_all_users, add_user, delete_user
from utils import summarise, top_two, filter_by_name_length, count_vowels  # ← count_vowels here

app = Flask(__name__)
app.secret_key = "userdb-secret-123"
app.jinja_env.filters["count_v"] = count_vowels  # ← this line registers the filter
@app.route("/")
def index():
    all_users = get_all_users()
    return render_template("index.html", users=all_users)

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        name  = request.form.get("name", "")
        email = request.form.get("email", "")
        role  = request.form.get("role", "Viewer")

        result = add_user(name, email, role)

        if result["success"]:
            flash(f"{result['user']['name']} added successfully.", "success")
            return redirect(url_for("index"))
        else:
            return render_template("add.html", errors=result["errors"],
                                   form={"name": name, "email": email, "role": role})

    return render_template("add.html", errors={}, form={})

@app.route("/delete/<int:user_id>", methods=["POST"])
def delete(user_id):
    delete_user(user_id)
    flash("User removed.", "info")
    return redirect(url_for("index"))

@app.route("/analytics")
def analytics():
    all_users = get_all_users()
    stats     = summarise(all_users)
    top       = top_two(all_users)
    return render_template("analytics.html", stats=stats, top=top, users=all_users)

if __name__ == "__main__":
    app.run(debug=True)