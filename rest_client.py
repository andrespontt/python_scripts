import requests

# rest client for restful api
# Make a GET request
response = requests.get('https://dummyjson.com/products/1')

# create a class products
class Products:
    def __init__(self, id, title, price, description, discountPercentage, rating, category, stock, brand, thumbnail, images):
        self.id = id
        self.title = title
        self.price = price
        self.description = description
        self.discountPercentage = discountPercentage
        self.rating = rating
        self.category = category
        self.stock = stock
        self.brand = brand
        self.thumbnail = thumbnail
        self.images = images

    def __str__(self):
        return f'Product: {self.title}, Price: {self.price}'

    def __repr__(self):
        return f'Product: {self.title}, Price: {self.price}'
    


# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Print the response content
    # print(response.json())

    # map response to products class
    product = Products(**response.json())
    print(product)
else:
    # Print the error message
    print('Error:', response.status_code)