
# Welfare Scheme Recommender – Hat Matrix (SMART AMI Hackathon 2025)

## 🧠 Overview

India has over **3400+ welfare schemes** run by central and state governments, yet a majority of citizens—especially in rural or marginalized communities—remain unaware of the benefits they are eligible for. Manual discovery of these schemes is tedious, and current systems lack intelligent, dynamic recommendation features.

Our project, **"Empowering Citizens: Streamlining Access to Government Welfare Schemes,"** solves this with a **multilingual AI-powered recommendation engine** that scrapes official data, matches citizen profiles to eligible schemes, and supports voice-based interaction.

---

## 🚀 Key Features

- 🔎 **Automated Scheme Scraping** using Selenium and BeautifulSoup
- 🧩 **TF-IDF + Cosine Similarity Recommender Engine**
- 🗣️ **Multilingual Voice Assistant** (Hindi & English) for inclusive access
- 📦 **Structured MongoDB Storage** with regular cron updates
- 🌐 **React-based User Interface** for easy profile input
- 🔄 **Real-time Scheme Matching** based on user demographics and eligibility

---

## 🛠️ Tech Stack

- **Frontend**: HTML / React
- **Backend**: Python, Flask
- **ML/NLP**: scikit-learn, SpaCy, TF-IDF Vectorizer, Cosine Similarity
- **Web Scraping**: Selenium, BeautifulSoup
- **Voice Input**: PyAudio, WebRTC-VAD
- **Database**: MongoDB
- **Scheduler**: Crontab

---

## 📊 Architecture

```
[User Input (Form/Voice)] --> [NLP Processing + NER] --> [TF-IDF Recommender]
           |                                            |
     [Voice-to-Text]                          [Welfare Scheme Corpus]
           |                                            |
    [Speech-to-Text Engine]                     [Cosine Similarity Score]
```

---

## 💡 How It Works

1. **Data Collection**: Scrapes scheme metadata from 3400+ portals (name, eligibility, benefits, etc.).
2. **Preprocessing**: Text cleaning, lowercasing, stemming, and lemmatization.
3. **Recommendation Engine**: Matches user demographics with scheme eligibility using TF-IDF + Cosine Similarity.
4. **Voice Assistant**: Captures spoken queries in English or Hindi and feeds them into the model.
5. **Output**: Top-5 most relevant schemes displayed to the user.

---

## ✅ Results

- 🔍 Successfully scraped and structured thousands of schemes
- 🎯 Delivered 90%+ relevant scheme matches
- 🗣️ Real-time bilingual voice input with robust text mapping
- 📈 Indexed MongoDB for high-performance querying

---

## 🧠 Challenges

| Challenge | Mitigation |
|----------|-------------|
| Inconsistent web layouts | Site-specific scraping logic |
| Dynamic JavaScript pages | Selenium with ChromeDriver |
| Voice noise/errors | Pause detection + VAD |
| Weekly updates | Crontab with MongoDB pipeline |

---

## 🔮 Future Enhancements

- Integrate LLM-based chatbot for Q&A support
- Android mobile app for rural deployment
- Feedback loop to refine recommendations
- Bhashini/Dialogflow-based NLP enhancements

---

## 👨‍💻 Contributors

Team Hat Matrix:
- Himani Grover
- Harsh Tantak
- Sayali Mahurkar

---

## 📎 References

- Selenium, BeautifulSoup
- scikit-learn, SpaCy
- MongoDB PyMongo
- PyAudio, WebRTC-VAD
