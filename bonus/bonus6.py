contents = ["carrots are sliced",
            "reportedly the carrots were sliced",
             "the presentation of carrots"]

filenames = ["doc.txt", "report.txt", "presentation.txt"]

for content, filename in zip(contents, filenames):
    file = open(f"../files/{filename}", "w")
    file.write(content)