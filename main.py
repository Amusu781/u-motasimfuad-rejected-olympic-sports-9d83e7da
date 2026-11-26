import os
import shutil

LINE = "Competitive Apology: two Canadians, one parking spot, first to stop saying sorry is disqualified."

OUT = os.environ.get("MAKEFUN_OUT", "/output")


def main():
    os.makedirs(OUT, exist_ok=True)
    for name in os.listdir(OUT):
        path = os.path.join(OUT, name)
        if os.path.isdir(path):
            shutil.rmtree(path)
        else:
            os.remove(path)
    assert 1 <= len(LINE) <= 200, "entry must be 1 to 200 characters"
    assert LINE.strip(), "entry must not be only whitespace"
    with open(os.path.join(OUT, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
