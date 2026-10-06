import duckdb
def test_duplicate():
    dupl = duckdb.sql("SELECT COUNT(DISTINCT CompanyNumber) FROM 'tests/good_companies.csv'  ").fetchone()
    count = duckdb.sql("SELECT COUNT(*) FROM 'tests/good_companies.csv'").fetchone()
    assert dupl[0] == count[0]