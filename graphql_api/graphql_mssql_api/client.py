import requests
from pprint import pprint

url = "http://localhost:4000/graphql"

def read_data():
    query = """
    {
      books {
        id
        title
        author {
          name
        }
      }
    }
    """

    query = """
    {
      authors {
        id
        name
        books {
          title
        }
      }
    }
    """

    try:
        response = requests.post(url,
            json={"query": query},
            headers={"Content-Type": "application/json"})
        if response.status_code == 200:
            pprint(response.json())
        else:
            print(f"Error: {response.status_code}")
    except Exception as e:
        print("run the server from current directory: node .\init.js")

def write_data():
    # Define your mutation and variables
    mutation = """
    mutation addBook($title: String!, $authorId: ID!) {
      addBook(title: $title, authorId: $authorId) {
        id
        title
        author {
          name
        }
      }
    }
    """

    variables = {
        "title": "GraphQL with Python",
        "authorId": "1"  # make sure this ID exists in your DB
    }
    try:
        # Send the mutation
        response = requests.post(
            url,
            json={
                "query": mutation,
                "variables": variables
            },
            headers={"Content-Type": "application/json"}
        )
        # Output the result
        print(response.json())
    except Exception as e:
        print("run server ")

#write_data()

read_data()




