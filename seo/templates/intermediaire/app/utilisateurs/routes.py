"""Routes utilisateurs (auth, profil, etc.)"""
from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from app import db
from app.utilisateurs.models import User

bp = Blueprint("utilisateurs", __name__, url_prefix="/auth")

@bp.route("/connexion", methods=["GET", "POST"])
def connexion():
    if current_user.is_authenticated:
        return redirect(url_for("taches.liste"))
    
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            login_user(user)
            flash("Connexion réussie!", "success")
            next_page = request.args.get("next")
            return redirect(next_page or url_for("taches.liste"))
        else:
            flash("Identifiants invalides", "error")
    
    return render_template("utilisateurs/connexion.html")

@bp.route("/deconnexion")
@login_required
def deconnexion():
    logout_user()
    flash("Déconnexion réussie", "info")
    return redirect(url_for("utilisateurs.connexion"))
