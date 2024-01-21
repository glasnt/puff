import pathlib
import sqlite_utils
import sys
import re

root = pathlib.Path(__file__).parent.resolve()

index_re = re.compile(r"<!\-\- index starts \-\->.*<!\-\- index ends \-\->", re.DOTALL)

def titleify(str): 
    return str.title().replace("_", " ")

if __name__ == "__main__":

    # load topics
    db = sqlite_utils.Database(root / "til.db")
    by_topic = {}
    for row in db["til"].rows_where(order_by="created_utc"):
        by_topic.setdefault(row["topic"], []).append(row)
    index = ["<!-- index starts -->"]

    # alphabetize the topics
    topics = list(by_topic.keys())

    # write topics to list
    for topic in topics:
        index.append("## {}\n".format(titleify(topic)))
        rows = by_topic[topic]
        for row in rows:
            index.append(
                "* [{title}]({url}) - {date}".format(
                    date=row["created"].split("T")[0], **row
                )
            )
        index.append("")
    if index[-1] == "":
        index.pop()
    index.append("<!-- index ends -->")

    
    if "--rewrite" in sys.argv:
        # write results
        readme = root / "README.md"
        index_txt = "\n".join(index).strip()
        readme_contents = readme.open().read()
        readme.open("w").write(index_re.sub(index_txt, readme_contents))
    else:
        # preview results
        print("\n".join(index))