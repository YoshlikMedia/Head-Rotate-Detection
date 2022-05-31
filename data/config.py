from environs import Env

# Теперь используем вместо библиотеки python-dotenv библиотеку environs
env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")  # Забираем значение типа str
ADMINS = env.list("ADMINS")  # Тут у нас будет список из админов
IP = env.str("DB_HOST")  # Тоже str, но для айпи адреса хоста
CHANEL = env.str("CHANEL")  # Тоже str, но для канала