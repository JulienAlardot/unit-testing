from main import ConnectionDatabaseError, TestDbError, connect_to_db, get_users_list_from_db, add

def test_ConnectionDatabaseError():
    assert issubclass(ConnectionDatabaseError, Exception)