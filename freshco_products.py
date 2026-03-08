import requests

url = "https://dam.flippenterprise.net/flyerkit/publication/7813184/products?display_type=all&locale=en&access_token=881f0b9feea3693a704952a69b2a037a"

try:
    # request data
    response = requests.get(url)
    response.raise_for_status()

    products = response.json()

except Exception as e:
    print("Error downloading data:", e)
    exit()

rows = ""
count = 1

# limit to first 20 products
for p in products[:20]:

    name = p.get("name", "N/A")
    price = p.get("price_text", "N/A")
    pic = p.get("image_url", "")

    rows += f"""
    <tr class="h-24">
        <td>{count}</td>
        <td>{name}</td>
        <td>{price}</td>
        <td><img src="{pic}" class="w-20 h-20 object-contain mx-auto""></td>
    </tr>
    """

    count += 1


# read template
with open("template.html", "r") as file:
    template = file.read()

# insert rows
final_html = template.replace("{rows}", rows)

# create webpage
with open("index.html", "w") as file:
    file.write(final_html)

print("index.html created successfully")