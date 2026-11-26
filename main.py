import os


def build_word():
    head = "Doom"
    tail = "scroll"
    return head + tail


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(build_word())


if __name__ == "__main__":
    main()
