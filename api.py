import matplotlib.pyplot as plt
import requests

def main():

    endpoint_url = "https://content.guardianapis.com/search"
    query = "?q=Covid"
    api_key = "&api-key=90081d1c-3e0b-4985-b813-d693354a4fd3"

    # No content with the tag Covid
    # response = requests.get("https://content.guardianapis.com/search?tag=Covid" + api_key)

    # Create a graph that would show the number of articles that were published per
    # month over the year 2022 that contain the word or pertain to “Covid”

    days_in_the_month_2022 = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 
                              7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    
    articles_published_per_month_in_2022 = {}

    data = open("guardian_covid_articles_2022_by_month.txt", "w")

    for month, days_in_the_month in days_in_the_month_2022.items():
        if(len(str(month))) == 1:
            dates = "&from-date=2022-0" + str(month) + "-01&to-date=2022-0" + str(month) + "-" + str(days_in_the_month)
        else:
            dates = "&from-date=2022-" + str(month) + "-01&to-date=2022-" + str(month) + "-" + str(days_in_the_month)
        
        url = endpoint_url + query + dates + api_key
        response = requests.get(url)

        articles_published = response.json()["response"]["total"]
        articles_published_per_month_in_2022[month] = articles_published

        if month != 12:
            data.write(str(month) + "-" + str(articles_published) + "\n")
        else:
            data.write(str(month) + "-" + str(articles_published))

    data.close()

    plt.title("Guardian Articles Containing \"Covid\" in 2022")
    plt.xlabel("Month")
    plt.ylabel("# Articles")
    plt.show()


if __name__ == "__main__":
    main()