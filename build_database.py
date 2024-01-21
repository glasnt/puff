from datetime import timezone
import git
import pathlib
import sqlite_utils

"""
Based on https://github.com/williln/til, 
who in turn cribbed from https://github.com/simonw/til
"""

root = pathlib.Path(__file__).parent.resolve()
DATABASE = root / "til.db"


def created_changed_times(repo_path, ref="latest"):
    created_changed_times = {}
    repo = git.Repo(repo_path, odbt=git.GitDB)
    commits = reversed(list(repo.iter_commits(ref)))
    for commit in commits:
        dt = commit.committed_datetime
        affected_files = list(commit.stats.files.keys())
        for filepath in affected_files:
            if filepath not in created_changed_times:
                created_changed_times[filepath] = {
                    "created": dt.isoformat(),
                    "created_utc": dt.astimezone(timezone.utc).isoformat(),
                }
            created_changed_times[filepath].update(
                {
                    "updated": dt.isoformat(),
                    "updated_utc": dt.astimezone(timezone.utc).isoformat(),
                }
            )
    return created_changed_times


def build_database(repo_path):
    all_times = created_changed_times(repo_path)
    
    # delete existing database, if exists. 
    if DATABASE.exists():
        pathlib.Path.unlink(DATABASE)

    # create new database 
    db = sqlite_utils.Database(repo_path / "til.db")
    table = db.table("til", pk="path")

    # rebuild database contents
    for filepath in root.glob("*/*.md"):
        fp = filepath.open()
        title = fp.readline().lstrip("#").strip()
        body = fp.read().strip()
        path = str(filepath.relative_to(root))
        url = "https://github.com/glasnt/puff/blob/latest/{}".format(path)
        record = {
            "path": path.replace("/", "_"),
            "topic": path.split("/")[0],
            "title": title,
            "url": url,
            "body": body,
        }
        record.update(all_times[path])
        table.insert(record)
    
    # ??
    if "til_fts" not in db.table_names():
        table.enable_fts(["title", "body"])


if __name__ == "__main__":
    build_database(root)
