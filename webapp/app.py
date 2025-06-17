from flask import Flask, jsonify, request
import mariadb
import os
import uuid

app = Flask(__name__)
uuid = uuid.uuid4().hex

@app.route('/api/quote', methods=['GET'])
def get_quote():
    try:
        # create new connection
        conn = mariadb.connect(
            user=os.getenv('DB_USER', 'default'),
            password=os.getenv('DB_PASSWORD', 'default'),
            host=os.getenv('DB_HOST', 'mysqldb'),
            port=3306,
            database=os.getenv('DB_DATABASE', 'quotes')
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

@app.route('/api/quote', methods=['POST'])
def submit_quote():
    data = request.get_json()
    quote = data.get('quote')
    author = data.get('author')

    if not quote or not author:
        return jsonify({"error": "Both 'quote' and 'author' are required."}), 400

    try:
        conn = mariadb.connect(
            user=os.getenv('DB_USER', 'default'),
            password=os.getenv('DB_PASSWORD', 'default'),
            host=os.getenv('DB_HOST', 'mysqldb'),
            port=3306,
            database=os.getenv('DB_DATABASE', 'quotes')
        )
        cur = conn.cursor()
        cur.execute("INSERT INTO quotes (quote, author) VALUES (?, ?)", (quote, author))
        conn.commit()
        return jsonify({"message": "Quote added successfully."}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/health', methods=['GET'])
def health():
    return("ok", 200)

@app.route('/uuid', methods=['GET'])
def get_uuid():
    return(uuid, 200)

if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0')
