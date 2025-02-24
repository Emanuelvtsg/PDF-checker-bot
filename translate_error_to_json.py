import json

with open("./data/error.log", "r", encoding="utf-8") as log_file:
    last_article = ''
    for line in log_file:
        data = line.split("/")
        journal = data[1]
        article = data[3]

        if last_article != article:
            last_article = article
            data_for_json = {
                "journal": journal,
                "article": article
            }
            with open('data.json', 'a', encoding="utf-8") as file:
                json.dump(data_for_json, file, indent=4)
                file.write(",\n")