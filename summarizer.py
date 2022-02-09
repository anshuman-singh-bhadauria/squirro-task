from gensim.summarization.summarizer import summarize
from gensim.summarization import keywords


def text_summarizer(document):
    """
    Takes a document in string format and returns a summary.
    """
    print(document)

    summary=summarize(document, word_count=50)

    return summarize(document, ratio=0.05)


