from src.bot import handle_mentions
from utils.logger import log_info

if __name__ == '__main__':
    log_info("Twitter bot started")
    handle_mentions()
    log_info("Twitter bot completed cycle")
