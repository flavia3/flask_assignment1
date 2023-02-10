from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def default():
    return "Hello welcome to python flask"

@app.route('/articles', methods = ["GET"])
def get_articles():
    article_details = [
        {
            "id": 1,
            "name" : "The Future of Artificial Intelligence",
            "body": "An articles about the rapidly evolving field of artificial intelligence and it's on various industries",
            "author": "John Doe"
        },
        {
            "id": 2,
            "name" : "The Benefits and Risks of Artificial Intelligence in Healthcare",
            "body": "This article analyzes the advantages and disadvantages of incorporating AI into the healthcare industry",
            "author": "Jane Doe"
        },
        {
            "id": 3,
            "name" : "Artificial Intelligence and the Future of Work",
            "body": "This article looks at the impact of AI on the future of work and the potential consequences for employment and the job market.",
            "author": "David Brown"
        },
        {
            "id": 4,
            "name" : "The Role of Artificial Intelligence in Financial Services",
            "body": "This article discusses the integration of AI in the financial services industry and its potential to transform the sector.",
            "author": " Sarah Johnson"
        }
    
    ]
    return jsonify(article_details)


if __name__ == '__main__':
    app.run(debug=True)