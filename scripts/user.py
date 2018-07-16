import click
from src import app, db
from flask.cli import AppGroup
from src.models.user import User, UserType

user_command = AppGroup("user")


@user_command.command("create")
@click.argument("username")
@click.argument("email")
@click.argument("password")
def create_user(username, email, password):
    user = User(username=username, email=email)
    try:
        user.set_password(password)
        user.account_type = UserType.USER
        db.session.add(user)
        db.session.commit()
        print("User {} created".format(user.username))
    except Exception:
        print("Unable to create user")


@user_command.command("promote-moderator")
@click.argument("username")
def promote_mod(username):
    user = User.query.filter_by(username=username).first()
    try:
        if (
            user.account_type != UserType.MODERATOR
            and user.account_type != UserType.ADMIN
        ):
            user.account_type = UserType.MODERATOR
            db.session.commit()
            return print("User {} promoted as moderator".format(user.username))
        return print(
            "User already have the priviledges, use demote command to demote user"
        )
    except AttributeError:
        return print("No user {}".format(username))


@user_command.command("promote-admin")
@click.argument("username")
def promote_admin(username):
    user = User.query.filter_by(username=username).first()
    try:
        if user.account_type != UserType.ADMIN:
            user.account_type = UserType.ADMIN
            db.session.commit()
            return print("User {} promoted as administrator".format(user.username))
        return print("User already administrator")
    except AttributeError:
        return print("No user {}".format(username))


@user_command.command("demote")
@click.argument("username")
def demote(username):
    user = User.query.filter_by(username=username).first()
    if user.account_type == UserType.ADMIN:
        user.account_type = UserType.MODERATOR
        db.session.commit()
        return print("User {} demoted to moderator".format(user.username))
    if user.account_type == UserType.MODERATOR:
        user.account_type = UserType.USER
        db.session.commit()
        return print("User {} demoted to common user".format(user.username))
    else:
        return print("User {} cannot be demoted".format(user.username))


@user_command.command("status")
@click.argument("username")
def get_status(username):
    user = User.query.filter_by(username=username).first()
    try:
        return print("User {} is {}".format(username, user.account_type.value))
    except AttributeError:
        return print("User not found")


app.cli.add_command(user_command)
