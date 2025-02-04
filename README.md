📌 Crypto Market Analysis & Prediction

🚀 A professional cryptocurrency analysis project using Python, Pandas, Matplotlib, Seaborn, and Deep Learning (LSTM).

🔹 Key Features:

    📊 Fetch real-time crypto data from Binance API
    📈 Visualize price trends and moving averages
    🤖 Predict Bitcoin prices using LSTMs (Deep Learning)
    📰 Analyze sentiment from Twitter (positive/negative crypto sentiment)
    🔥 Compare Bitcoin vs Ethereum market trends
    🏆 Showcase-ready project for employers & recruiters

📂 Project Structure

crypto-analysis/
│── data/                # Raw & processed data
│── notebooks/           # Jupyter Notebooks for analysis
│── scripts/             # Python scripts for data processing
│── models/              # Trained LSTM models
│── dashboard/           # Streamlit interactive dashboard
│── README.md            # Project documentation
│── requirements.txt     # Python dependencies
│── .gitignore           # Ignore unnecessary files

💡 How to Use the Project
1️⃣ Install Dependencies

First, create a virtual environment and install required libraries:

python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows

pip install -r requirements.txt

2️⃣ Fetch Crypto Data

python scripts/fetch_crypto_data.py

✔️ This will save Bitcoin price data in data/btc_data.csv.
3️⃣ Visualize Price Trends

python scripts/visualize_data.py

✔️ Generates Bitcoin price charts with moving averages.
4️⃣ Predict Bitcoin Prices (LSTM)

python scripts/lstm_model.py

✔️ Trains a Deep Learning model to forecast Bitcoin prices.
5️⃣ Analyze Twitter Sentiment

python scripts/sentiment_analysis.py

✔️ Uses Twitter API to determine if crypto sentiment is positive/negative.
6️⃣ Run the Streamlit Dashboard

streamlit run dashboard/app.py

✔️ Opens an interactive dashboard to explore crypto trends & sentiment.
📊 Sample Visualizations
Bitcoin Price Trend

Sentiment Analysis of Crypto Tweets

🔬 Technologies Used

    Python 🐍
    Pandas & NumPy for data analysis
    Matplotlib & Seaborn for visualization
    TensorFlow/Keras for Deep Learning (LSTM model)
    Streamlit for interactive dashboards
    Tweepy for Twitter sentiment analysis
    Binance API for real-time crypto data

🛠️ Future Improvements

✅ Add more machine learning models (Random Forest, XGBoost)
✅ Integrate Reddit sentiment analysis for more insights
✅ Build a live trading bot using Moving Average strategies
📝 Author

👤 Alex Nkusi
🔗 https://www.linkedin.com/in/ankusi/
📧 nkusialex@gmail.com

💬 Want to collaborate? Feel free to reach out! 🚀