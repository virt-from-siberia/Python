def log(tag="", message=""):
    with open("log.txt", "w+") as logger:
        logger.write(f"{tag}: {message}\n")
