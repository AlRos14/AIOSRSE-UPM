import matplotlib.pyplot as plt
from wordcloud import WordCloud

def generate_keyword_cloud(keyword_data, output_file):
    """Generate a word cloud from the keyword data."""
    wordcloud = WordCloud(width=800, height=400, background_color="white").generate_from_frequencies(keyword_data)
    
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.savefig(output_file)
    plt.close()

def plot_figures_per_article(papers, output_file):
    """Chart of the number of figures per article"""
    figure_counts = {}

    for paper, text in papers.items():
        figure_counts[paper] = text.count("<figure") # Include the number of figures in the text (images, tables, etc.)

    plt.figure(figsize=(20, 14))
    plt.bar(figure_counts.keys(), figure_counts.values(), color="skyblue")
    plt.xticks(rotation=45, ha="right")
    plt.xlabel("Papers")
    plt.ylabel("Number of Figures")
    plt.title("Figures per Article")
    plt.tight_layout() # Adjust the plot to ensure everything fits without overlapping
    plt.savefig(output_file)
    plt.close()
