from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)
CORS(app)

# Load and prepare data
csv_path = 'scheme_entities (1).csv'
df = pd.read_csv(csv_path)
df['Details'] = df['Details'].fillna("")

def remove_duplicates(df, threshold=0.95):
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(df['Details'])
    sim_matrix = cosine_similarity(tfidf_matrix)
    to_drop = set()
    for i in range(len(sim_matrix)):
        for j in range(i + 1, len(sim_matrix)):
            if sim_matrix[i][j] > threshold:
                to_drop.add(j)
    return df.drop(df.index[list(to_drop)]).reset_index(drop=True)

df = remove_duplicates(df, threshold=0.95)

vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(df['Details'])

def recommend_from_query(query, top_n=5):
    query_vec = vectorizer.transform([query])
    sim_scores = cosine_similarity(query_vec, tfidf_matrix).flatten()
    top_indices = sim_scores.argsort()[::-1][:top_n]
    return df[['Scheme Name', 'Details']].iloc[top_indices].to_dict(orient='records')

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.json
    query = f"{data.get('gender','')} {data.get('occupation','')} {data.get('state','')} {data.get('income','')} {data.get('age','')} {data.get('custom_query','')}"
    recommendations = recommend_from_query(query, top_n=5)
    return jsonify(recommendations)

@app.route('/voice-recommend', methods=['POST'])
def voice_recommend():
    data = request.json
    query = data.get('query', '')
    recommendations = recommend_from_query(query, top_n=5)
    return jsonify({
        'recommendations': recommendations
    })

if __name__ == '__main__':
    app.run(port=5002) 

