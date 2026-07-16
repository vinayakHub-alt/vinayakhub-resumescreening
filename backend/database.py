import sqlite3

DB_NAME = "candidates.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS candidates (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            skills TEXT,
            experience INTEGER,
            education TEXT,
            score REAL
        )
    """)
    conn.commit()
    conn.close()

def insert_candidate(name, skills, experience, education, score):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO candidates (name, skills, experience, education, score)
        VALUES (?, ?, ?, ?, ?)
    """, (name, skills, experience, education, score))
    conn.commit()
    conn.close()

def fetch_candidates():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT name, skills, experience, education, score FROM candidates")
    rows = cursor.fetchall()
    conn.close()

    # Convert tuples to dictionaries
    candidates = []
    for r in rows:
        candidates.append({
            "name": r[0],
            "skills": r[1],
            "experience": r[2],
            "education": r[3],
            "score": r[4]
        })
    return candidates
