from flask import Flask, jsonify
import mariadb
import time

app = Flask(__name__)

@app.route('/api/quote', methods=['GET'])
def submit():
    try:
        # create new connection
        conn = mariadb.connect(
            user="sebi",
            password="changeme",
            host="msqldb",
            port=3306,
            database="quotes"
        )
        # create new cursor, and querry DB for a random quote
        cur = conn.cursor()
        cur.execute("SELECT * FROM quotes ORDER BY RAND() LIMIT 1;")
        result = cur.fetchone()
        # if result, return result
        if result:
            return jsonify({
                "quote": result[1],
                "author": result[2]
            })
        else:
            return jsonify({})
    except:
        return jsonify("DB Error!"), 500

if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0')
