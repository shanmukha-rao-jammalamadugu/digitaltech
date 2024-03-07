import http.client
import json

def get_time_stories():
    host = "time.com"
    conn = http.client.HTTPSConnection(host)
    conn.request("GET", "/")

    response = conn.getresponse()
    html_content = response.read().decode('utf-8')
    conn.close()

    stories = []
    start_marker = '<h3 class="latest-stories__item-headline">'
    end_marker = '</h3>'
    link_start_marker = '<a href="'
    link_end_marker = '">'

    index = 0
    while index < len(html_content) and len(stories) < 6:
        
        title_start = html_content.find(start_marker, index)
        if title_start == -1:
            break

        title_end = html_content.find(end_marker, title_start)
        if title_end == -1:
            break

        title = html_content[title_start + len(start_marker):title_end].strip()

        
        link_start = html_content.find(link_start_marker, title_end)
        if link_start == -1:
            break

        link_end = html_content.find(link_end_marker, link_start)
        if link_end == -1:
            break

        link = "https://" + host + html_content[link_start + len(link_start_marker):link_end].strip()

        
        stories.append({'title': title, 'link': link})
        index = link_end + len(link_end_marker)

    return stories

if __name__ == "__main__":
    latest_time_stories = get_time_stories()

    # Print the JSON response
    json_response = json.dumps(latest_time_stories, indent=2)
    print(json_response)
