import argparse
from biomarkqa2.interface import query_papers

def main():
    parser = argparse.ArgumentParser(description="BioMarkQA2 - Query scientific papers for biomarkers")
    parser.add_argument("query", type=str, help="The biomarker-related query")
    
    args = parser.parse_args()
    print(query_papers(args.query))

if __name__ == "__main__":
    main()
