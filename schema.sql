CREATE TABLE IF NOT EXISTS access_logs (
    log_id INTEGER PRIMARY KEY AUTOINCREMENT,
    vehicle_id TEXT NOT NULL,
    access_type TEXT NOT NULL,  -- 'ENTRY' or 'EXIT'
    person_type TEXT NOT NULL,  -- 'STAFF' or 'VISITOR'
    timestamp DATETIME NOT NULL
);