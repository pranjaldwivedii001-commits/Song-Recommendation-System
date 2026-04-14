# Songs Recommendation System
# 👉 Live Demo :  
- https://songsuggesttt.streamlit.app/
- This system will suggest 5 songs with same genres based on user input

# 🚀Features :
- Recomend songs based on user input  
- Interactive UI using Streamlit

# 🔎Tech Stack :
- Python
- Pandas
- CountVectoriztion

## Project Overview

This project implements a basic song recommendation system that suggests songs based on the similarity of their lyrical content. By analyzing the text of song lyrics, the system identifies and recommends songs that share common themes, moods, or vocabulary with a given input song.

### Deployed Application

Check out the live Streamlit application here: [Song Suggest App](https://songsuggesttt.streamlit.app/)

## Table of Contents

*   [Features](#features)
*   [How it Works](#how-it-works)
*   [Technologies Used](#technologies-used)
*   [Setup and Installation](#setup-and-installation)
*   [Usage](#usage)
*   [Example Output](#example-output)
*   [Future Enhancements](#future-enhancements)

## Features

*   **Content-Based Recommendations**: Suggests songs purely based on lyrical similarity.
*   **Text Preprocessing**: Includes steps like lowercasing, stop word removal, and stemming for robust analysis.
*   **Count Vectorization**: Transforms song lyrics into numerical feature vectors.
*   **Cosine Similarity**: Measures the similarity between song lyrics.
*   **Persisted Model**: Saves the processed data and similarity matrix for quick loading and deployment.

## How it Works

1.  **Data Loading**: Song data, including lyrics, is loaded from a CSV file.
2.  **Data Cleaning**: Irrelevant columns are dropped, and text is converted to lowercase.
3.  **Feature Extraction**: `CountVectorizer` is used to convert the cleaned song lyrics into a Bag-of-Words representation. This creates a matrix where each row represents a song, and each column represents a word from the vocabulary, with values indicating the frequency of that word in the song's lyrics.
4.  **Text Stemming**: The NLTK Porter Stemmer is applied to reduce words to their root form (e.g., "running," "ran," "runs" all become "run"), improving the accuracy of similarity calculations.
5.  **Similarity Calculation**: `cosine_similarity` is computed between all song feature vectors. Cosine similarity measures the angle between two vectors, indicating how similar their directions are. A smaller angle (closer to 1) means higher similarity.
6.  **Recommendation**: Given a song, the system identifies songs with the highest cosine similarity scores (excluding the song itself) and returns the top 5 most similar songs.

## Technologies Used

*   **Python**: The primary programming language.
*   **pandas**: For data manipulation and analysis.
*   **numpy**: For numerical operations.
*   **scikit-learn**: For `CountVectorizer` (feature extraction) and `cosine_similarity` (similarity calculation).
*   **nltk**: For natural language processing tasks, specifically `PorterStemmer` for text stemming.
*   **pickle**: For serializing and deserializing Python objects (saving the model).
*   **Streamlit**: (Implied by the live app link) For deploying the interactive web application.

## Setup and Installation

To run this project locally, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone <your-repo-link>
    cd <your-repo-name>
    ```
2.  **Install the required libraries:**
    ```bash
    pip install numpy pandas scikit-learn nltk
    ```
3.  **Download NLTK data (if not already present):**
    You might need to download `punkt` and `stopwords` data for NLTK. This can be done within a Python script or interactively:
    ```python
    import nltk
    nltk.download('punkt')
    nltk.download('stopwords')
    ```

## Usage

1.  **Run the Jupyter Notebook/Colab:**
    Open the provided `.ipynb` file in Jupyter Notebook or Google Colab.
2.  **Execute all cells:**
    Run all the cells to process the data, build the similarity matrix, and define the `Recommend` function.
3.  **Get recommendations:**
    Use the `Recommend()` function with a song title from your dataset.

    ```python
    Recommend('Bang-A-Boomerang')
    ```

## Example Output

```
Bang
Dum Dum Diddle
If You Love Me
I Love America
Falling In Love With Love
```

## Future Enhancements

*   **Improve Feature Extraction**: Experiment with TF-IDF, Word Embeddings (e.g., Word2Vec, GloVe), or transformer models (e.g., BERT) for richer text representations.
*   **Hybrid Recommendation**: Combine lyrical similarity with other factors like artist, genre, tempo, or user listening history.
*   **User Interface**: Develop a more interactive and visually appealing user interface.
*   **Scalability**: Optimize the system for larger datasets and faster similarity calculations.
*   **Performance Evaluation**: Implement metrics to evaluate the quality of recommendations.
