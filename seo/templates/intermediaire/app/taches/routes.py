"""Routes tâches"""
from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from app import db
from app.taches.models import Tache

bp = Blueprint("taches", __name__, url_prefix="/taches")

@bp.route("/")
@login_required
def liste():
    taches = current_user.taches.order_by(Tache.date_creation.desc()).all()
    return render_template("taches/liste.html", taches=taches)

@bp.route("/ajouter", methods=["POST"])
@login_required
def ajouter():
    titre = request.form.get("titre")
    if titre:
        tache = Tache(titre=titre, proprietaire=current_user)
        db.session.add(tache)
        db.session.commit()
        flash("Tâche ajoutée!", "success")
    return redirect(url_for("taches.liste"))

@bp.route("/terminer/<int:id>")
@login_required
def terminer(id):
    tache = Tache.query.get_or_404(id)
    if tache.proprietaire == current_user:
        tache.termine = not tache.termine
        db.session.commit()
        flash("Tâche mise à jour!", "success")
    return redirect(url_for("taches.liste"))

@bp.route("/supprimer/<int:id>")
@login_required
def supprimer(id):
    tache = Tache.query.get_or_404(id)
    if tache.proprietaire == current_user:
        db.session.delete(tache)
        db.session.commit()
        flash("Tâche supprimée!", "success")
    return redirect(url_for("taches.liste"))
