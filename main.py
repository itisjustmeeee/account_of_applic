from models.requests import add_request, show_my_requests
from models.users import login_user, register_user
from storage import load_data, save_data


def main() -> None:
    """Запускает приложение."""

    users = load_data("data/users.json")
    requests = load_data("data/requests.json")

    print("Сервис учета заявок")


if __name__ == "__main__":
    main()
