import requests
import json

#API request for articles containing drug name only
"""
def search_pubmed(drug_name, max_results=6):
    base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    params = {
        "db": "pubmed",
        "term": drug_name,
        "retmode": "json",
        "retmax": max_results  # Number of articles to retrieve
    }
    response = requests.get(base_url, params=params)
    article_ids = response.json()['esearchresult']['idlist']
    return article_ids
"""
#API request for articles containing drug name AND Alzheimer disease
def search_pubmed(drug_name, max_results=6):
    base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    query = f'"{drug_name}"[Title/Abstract] AND "alzheimer disease"[MeSH Terms]'
    params = {
        "db": "pubmed",
        "term": query,
        "retmode": "json",
        "retmax": max_results
    }

    #print api response for debug
    response = requests.get(base_url, params=params)
    print("API response: ", response.json())

    response = requests.get(base_url, params=params)
    article_ids = response.json()['esearchresult']['idlist']
    return article_ids

#requests from BERN2 using pmids as a STRING
def query_bern2(pmids, url="http://bern2.korea.ac.kr/pubmed"):
    return requests.get(url + "/" + (pmids)).json()


if __name__ == "__main__":
    drug_name = input("Enter the drug name: ")

    pubmed_ids = search_pubmed(drug_name)
    print("PubMed IDs of relevant articles:", pubmed_ids)

    #converts the pmid data from list type into string type
    pmids = ','.join(pubmed_ids)

    #writes the BERN2 request to JSON file
    json_object = json.dumps(query_bern2(pmids), indent=4)
    with open("output.json", "w") as outfile:
       outfile.write(json_object)

    
