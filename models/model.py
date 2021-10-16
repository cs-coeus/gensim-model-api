import gensim.downloader as api

from models.ModelInterface import ModelInterface


class ModelGensim(ModelInterface):
    model = None

    def __init__(self):
        ModelGensim.model = api.load('word2vec-google-news-300')

    @staticmethod
    def get_similarity_two_word_by_w2v(word1: str, word2: str):
        try:
            similarity = ModelGensim.model.similarity(word1, word2)
        except KeyError:
            similarity = 0
        return similarity

    @staticmethod
    def get_wmd(word1: str, word2: str):
        return ModelGensim.model.wmdistance(word1, word2)

    @staticmethod
    def get_word_embedding(word: str):
        try:
            word_embedded = ModelGensim.model[word]
            return word_embedded.tolist()
        except KeyError:
            return f"{word} not in vocabulary"

    @staticmethod
    def predict(input: str) -> None:
        return None
