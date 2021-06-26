from alembic_test import app


@app.route('/')
def test():
    return 'It works'

