from langchain_core.messages import HumanMessage, SystemMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from schema import RestaurantDetails
import base64, os, getpass, csv, json
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

if "GOOGLE_API_KEY" not in os.environ:
    os.environ["GOOGLE_API_KEY"] = getpass.getpass("Enter your Google AI API key: ")

model = ChatGoogleGenerativeAI(model = "gemini-2.5-flash-preview-05-20")

llm_with_structured_output = model.with_structured_output(RestaurantDetails)


def pass_image(image):

    encoded_image = base64.b64encode(image.read()).decode("utf-8")

    return encoded_image


def create_prompt(encoded_image):

    messages = [
    SystemMessage(
        content="""
                You need to perform structured data extraction from given image. Only Parse the fields that are non-ambiguous and can be validated accurately.
                Use below information for determinig type of item:
                In India, vegetarian and non-vegetarian foods are distinguished using specific symbols. Vegetarian foods are marked with a green symbol, \
                while non-vegetarian foods are marked with a reddish-brown symbol. These symbols are mandated by the Indian government and appear on packaged food products. 
        """
        ),
    HumanMessage(
        content=[
        {"type": "text", "text": "Analyse the image for the purpose of structured data extraction"},
        {"type": "image_url", "image_url": f"data:image/png;base64,{encoded_image}"},
            ]
        )
    ]

    return messages


def call_llm(prompt):

    response = llm_with_structured_output.invoke(prompt)

    return response.model_dump()


def response_to_dataframe(response):

    rows = []

    restaurant_id = "REST_001"
    restaurant_name = response.get("name", "Unknown Restaurant")
    restaurant_area = response.get("area", "Unknown Area")

    category_counter = 1
    item_counter = 1

    for category in response.get("categories", []):
        category_id = f"CAT_{category_counter:03d}"
        category_name = category.get("name", "Unknown Category")
        category_counter += 1

        for item in category.get("items", []):
            item_id = f"ITEM_{item_counter:03d}"
            item_counter += 1

            item_name = item.get("name", "")
            description = item.get("description", "").replace("+", ", ") if item.get("description") else ""
            price = item.get("price", [None])[0]
            item_type = item.get("type", "")

            add_ons = item.get("add_ons", [])
            if not add_ons:
                rows.append([
                    restaurant_id, restaurant_name, restaurant_area,
                    category_id, category_name,
                    item_id, item_name, description, price, item_type,
                    None, None 
                ])
            else:
                for add_on in add_ons:
                    rows.append([
                        restaurant_id, restaurant_name, restaurant_area,
                        category_id, category_name,
                        item_id, item_name, description, price, item_type,
                        add_on.get("name", ""), add_on.get("add_on_price", "")
                    ])

    columns = [
        "restaurant_id", "restaurant_name", "restaurant_area",
        "category_id", "category_name",
        "item_id", "item_name", "description", "price", "type",
        "add_on_name", "add_on_price"
    ]

    df = pd.DataFrame(rows, columns=columns)

    return df





