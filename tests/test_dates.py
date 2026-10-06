import duckdb
def test_dates():
    dateCheck = duckdb.sql("SELECT COUNT(*), FROM read_csv('tests/good_companies.csv', types={'IncorporationDate': 'VARCHAR'}) WHERE (try_strptime(IncorporationDate, '%d/%m/%Y') IS NULL OR current_date < try_strptime(IncorporationDate, '%d/%m/%Y'))").fetchone()
    assert dateCheck[0] == 0