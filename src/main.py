import salyk
import logger
import dotenv


if __name__ == '__main__':
    dotenv.load_dotenv()
    logger.setup_logger()
    salyk.run()
