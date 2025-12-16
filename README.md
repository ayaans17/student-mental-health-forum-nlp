🧠 Online Forum for Students’ Life Problems and Depressive Users Detection System

An interactive online forum that helps college students discuss life challenges, relationships, and academic stress while integrating Natural Language Processing (NLP) to detect signs of depression in user posts. The system promotes mental well-being by connecting students with verified teachers and psychiatrists who can provide professional guidance.

🌟 Features

💬 Student Forum – Students can post personal or academic problems and receive support from peers and verified experts.

🧠 Depression Detection (Sentiment Analysis) – NLP models analyze post polarity and subjectivity to flag depressive users.

👩‍🏫 Verified Professionals – Teachers and psychiatrists register with ID/licence verification to ensure safety.

🤖 Chatbot Support – ML-based chatbot using neural intents assists users with navigation and tracks emotional tone.

🤖 Asynchronous Messaging – Asynchronous Web Chatting using Web Sockets.

📊 User Analytics Dashboard – Visual graphs show positivity, negativity, and subjectivity trends of user posts.

🔒 Privacy & Ethics – Maintains confidentiality and focuses on emotional support, not clinical diagnosis.

🧩 System Overview

The system detects potentially depressive users through sentiment analysis and connects them with mental-health professionals. It uses TextBlob and VADER for polarity scoring, and a chatbot built using machine learning and lemmatization to interact with users.

🔧 Workflow

Users register (student or professional).

Students post problems or use the chatbot.

NLP model computes sentiment polarity (–1 to +1).

Users with high negative sentiment (≤ –0.6) are flagged.

Verified professionals can review profiles and reach out privately.

⚙️ Tech Stack
Component	Technology
Frontend / UI	Django Templates (HTML, CSS, JS)
Backend Framework	Django (Python)
Programming Language	Python
Database	SQLite / MySQL
Sentiment Analysis Libraries	TextBlob, VADER
Chatbot / NLP Libraries	NLTK, spaCy, scikit-learn
🧠 NLP & Sentiment Analysis
TextBlob

Calculates polarity and subjectivity for each post.

Uses a lexicon-based averaging approach with intensifiers (e.g., “not great”).

VADER

Designed for social-media text; uses heuristics like punctuation, capitalization, and degree modifiers.

Produces sentiment scores between –1 (most negative) and +1 (most positive).

Chatbot (Neural Intents)

Tokenizes and lemmatizes user input using WordNetLemmatizer().

Classifies intent with an error threshold of 0.25.

Saves conversations for further sentiment evaluation.

💻 Installation and Setup
1. Clone the Repository
git clone https://github.com/ayaans17/student-mental-health-forum-nlp.git

2. Navigate to the Project
cd student-mental-health-forum-nlp

3. Install Requirements
pip install -r requirements.txt

4. Run the Django Development Server
python manage.py runserver

5. Access the Application

Open http://127.0.0.1:8000/ in your browser.

🧾 Dataset

Source: Student review datasets (college and university reviews, 1,111 samples).

Preprocessing: URL removal, punctuation stripping, tokenization, lemmatization, stopword removal.

Additional Inputs: Chatbot conversations and user forum posts.

📊 Analysis and Outputs

Graphs display positivity, negativity, and neutrality across posts.

Word-frequency plots reveal the most common emotionally charged terms.

Sentiment trends help professionals evaluate a user’s mental health state.

Users with polarity ≤ –0.6 are flagged as borderline depressed.

🚀 Future Enhancements

Voice and image sentiment analysis for multimodal understanding.

Video call integration between users and verified professionals.

Explainable AI (XAI) to make sentiment predictions transparent.

Cloud deployment for scalability across universities.

⚖️ Ethical Considerations

All user data is anonymized and securely stored.

The system provides emotional support, not medical diagnosis.

Only verified professionals can contact at-risk users.

Adheres to data privacy and consent regulations.

🧩 Contributors
Name	        Role	                  Institution
Ayaan Shaikh	Developer / Researcher	Dublin City University
