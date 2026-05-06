import psycopg2

DB_CONFIG = dict(
    dbname="snake_db",
    user="postgres",
    password="071017",
    host="localhost",
    port="5432",
)


def _connect():
    return psycopg2.connect(**DB_CONFIG)


def init_db():
    # Auto-create the database if it doesn't exist
    try:
        conn = _connect()
    except psycopg2.OperationalError:
        # Connect to the default 'postgres' database to create snake_db
        temp = psycopg2.connect(
            dbname="postgres",
            user=DB_CONFIG["user"],
            password=DB_CONFIG["password"],
            host=DB_CONFIG["host"],
            port=DB_CONFIG["port"],
        )
        temp.autocommit = True
        cur = temp.cursor()
        cur.execute("CREATE DATABASE snake_db")
        cur.close()
        temp.close()
        conn = _connect()

    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS players (
            id SERIAL PRIMARY KEY,
            username VARCHAR(50) UNIQUE NOT NULL
        );
    """)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS game_sessions (
            id SERIAL PRIMARY KEY,
            player_id INTEGER REFERENCES players(id),
            score INTEGER NOT NULL,
            level_reached INTEGER NOT NULL,
            played_at TIMESTAMP DEFAULT NOW()
        );
    """)
    conn.commit()
    cur.close()
    conn.close()


def get_or_create_player(username):
    username = username.strip().lower()
    conn = _connect()
    cur = conn.cursor()
    cur.execute("SELECT id FROM players WHERE username = %s", (username,))
    row = cur.fetchone()
    if row:
        cur.close(); conn.close()
        return row[0]
    cur.execute("INSERT INTO players (username) VALUES (%s) RETURNING id", (username,))
    player_id = cur.fetchone()[0]
    conn.commit()
    cur.close(); conn.close()
    return player_id


def save_game(player_id, score, level):
    conn = _connect()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO game_sessions (player_id, score, level_reached) VALUES (%s, %s, %s)",
        (player_id, score, level),
    )
    conn.commit()
    cur.close(); conn.close()


def get_top_scores(limit=10):
    conn = _connect()
    cur = conn.cursor()
    cur.execute("""
        SELECT p.username, s.score, s.level_reached, s.played_at
        FROM game_sessions s
        JOIN players p ON p.id = s.player_id
        ORDER BY s.score DESC
        LIMIT %s
    """, (limit,))
    rows = cur.fetchall()
    cur.close(); conn.close()
    return rows


def get_top():
    conn = _connect()
    cur = conn.cursor()
    cur.execute("""
        SELECT p.username,
               MAX(s.score)         AS best_score,
               MAX(s.level_reached) AS best_level,
               MAX(s.played_at)     AS last_play
        FROM game_sessions s
        JOIN players p ON p.id = s.player_id
        GROUP BY p.username
        ORDER BY best_score DESC
        LIMIT 10
    """)
    rows = cur.fetchall()
    cur.close(); conn.close()
    return rows


def get_best(player_id):
    conn = _connect()
    cur = conn.cursor()
    cur.execute("SELECT MAX(score) FROM game_sessions WHERE player_id = %s", (player_id,))
    result = cur.fetchone()[0]
    cur.close(); conn.close()
    return result or 0