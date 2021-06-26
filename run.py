from alembic_test import app
from datetime import datetime
#app.run(debug=True, host="0.0.0.0")

if __name__== '__main__':
    #print('################### Restarting @', datetime.utcnow(), '###################')
    app.run(debug=True, host="0.0.0.0", port=5000, use_reloader=False)
