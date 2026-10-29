
import configparser
import os

config = configparser.RawConfigParser()

# Get project root directory
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Build correct config.ini path
config_path = os.path.join(
    project_root, "Configuration", "config.ini"
)

# Read configuration file
files_read = config.read(config_path)

print("Config file path:", config_path)
print("Config file loaded:", files_read)
print("Available sections:", config.sections())


class ReadConfigClass:

    @staticmethod
    def get_data_for_email():
        return config.get("login_data", "email")

    @staticmethod
    def get_data_for_password():
        return config.get("login_data", "password")

    @staticmethod
    def get_home_url():
        return config.get("app urls", "home_url")

    @staticmethod
    def get_login_url():
        return config.get("app urls", "login_url")

    @staticmethod
    def get_registration_url():
        return config.get("app urls", "registration_url")