import argparse
import logging
from src.grobid_client import process_papers
from src.text_processing import extract_abstract_keywords
from src.visualization import generate_keyword_cloud, plot_figures_per_article
from src.link_extractor import extract_links

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def main():
    parser = argparse.ArgumentParser(
        description='Process PDF papers and generate visualizations.\n' +
        'Este script procesa los archivos PDF en la carpeta data/ y genera visualizaciones en la carpeta output/'
    )
    parser.parse_args()

    
    logging.info("Iniciando el análisis de artículos...")

    # Paso 1: Process PDFs
    papers = process_papers("data/") 

    # Paso 2: Extract abstract keywords
    keyword_data = extract_abstract_keywords(papers)

    # Paso 3: Generate keyword cloud
    generate_keyword_cloud(keyword_data, "output/keyword_cloud.png")

    # Paso 4: Count figures per article
    plot_figures_per_article(papers, "output/figures_per_article.png")

    # Paso 5: Extract links
    links = extract_links(papers)
    
    # Save links to file
    with open("output/links.txt", "w") as f:
        for paper, link_list in links.items():
            f.write(f"{paper}:\n")
            for link in link_list:
                f.write(f"  - {link}\n")

    logging.info("Análisis completado. Resultados guardados en la carpeta output/")

if __name__ == "__main__":
    main()

