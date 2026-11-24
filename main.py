import os

OUTPUT_DIR = os.environ.get("OUTPUT_DIR", "/output")
LINE = (
    "Good news: I found the bug. Bad news: it was me, it is live in production, and it has already replicated into three other services and opened a ticket blaming you."
)


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    path = os.path.join(OUTPUT_DIR, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
