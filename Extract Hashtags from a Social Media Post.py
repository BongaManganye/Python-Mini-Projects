#Extract Hashtags from a Social Media Post
#Extract all hashtags from: "Loving #Python and #Coding at #LkhibraAcademy"

import re

post = "Loving #Python and #Coding at #LkhibraAcademy"
hashtags = re.findall(r"#\w+", post)

print(f"Hashtags: {hashtags}")
