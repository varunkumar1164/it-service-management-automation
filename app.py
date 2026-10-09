from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tickets = []
ticket_counter = 1001

VALID_STATUSES = {"OPEN", "IN PROGRESS", "RESOLVED"}
VALID_PRIORITIES = {"LOW", "MEDIUM", "HIGH", "CRITICAL"}


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/create-ticket", methods=["POST"])
def create_ticket():
    global ticket_counter

    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip()
    issue = request.form.get("issue", "").strip()
    priority = request.form.get("priority", "LOW").upper()
    description = request.form.get("description", "").strip()

    if not all([name, email, issue, description]):
        return "All fields are required.", 400

    if priority not in VALID_PRIORITIES:
        return "Invalid priority.", 400

    ticket = {
        "id": ticket_counter,
        "name": name,
        "email": email,
        "issue": issue,
        "priority": priority,
        "description": description,
        "status": "OPEN"
    }

    tickets.append(ticket)
    ticket_counter += 1

    return redirect(url_for("dashboard"))


@app.route("/dashboard")
def dashboard():
    search = request.args.get("search", "").strip().lower()

    filtered_tickets = [
        ticket for ticket in tickets
        if search in str(ticket["id"]).lower()
        or search in ticket["name"].lower()
        or search in ticket["issue"].lower()
        or search in ticket["status"].lower()
    ]

    return render_template(
        "dashboard.html",
        tickets=filtered_tickets,
        search=search
    )


@app.route("/update/<int:ticket_id>", methods=["POST"])
def update_ticket(ticket_id):
    status = request.form.get("status", "").upper()

    if status not in VALID_STATUSES:
        return "Invalid ticket status.", 400

    for ticket in tickets:
        if ticket["id"] == ticket_id:
            ticket["status"] = status
            break

    return redirect(url_for("dashboard"))


@app.route("/delete/<int:ticket_id>", methods=["POST"])
def delete_ticket(ticket_id):
    global tickets

    tickets = [
        ticket for ticket in tickets
        if ticket["id"] != ticket_id
    ]

    return redirect(url_for("dashboard"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)