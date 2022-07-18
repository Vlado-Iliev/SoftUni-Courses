from project.library import Library
from project.user import User


class Registration:

    def add_user(self, user: User, library: Library):
        for person in library.user_records:
            if person == user:
                return f"User with id = {user.user_id} already registered in the library!"
        library.user_records.append(user)

    def remove_user(self,user: User, library: Library):
        for person in library.user_records:
            if person == user:
                library.user_records.remove(user)
        return f"We could not find such user to remove!"

    def change_username(self, user_id: int, new_username: str, library: Library):
        for person in library.user_records:
            if person.user_id == user_id:
                if person.username == new_username:
                    return "Please check again the provided username - it should be different than the username used " \
                           "so far! "
                person.username = new_username
                return f"Username successfully changed to: {new_username} for user id: {user_id}"
        return f"There is no user with id = {user_id}!"
