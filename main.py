from bs4 import BeautifulSoup
import requests
import pandas as pd

console_html = requests.get('https://www.vgchartz.com/analysis/platform_totals/Hardware/NA/').text
console_sales = BeautifulSoup(console_html)
console_list = []
north_america_list = []
europe_list = []
japan_list = []
world_list = []
globe_list = []
for i, items in enumerate(console_sales.find('table', class_='chart').find_all('tr')[1::1]):
    data = items.find_all(['th', 'td'])

    try:
        console = data[1].a.text
        console_list.append(console[console.find("(")+1:console.rfind(")")])

        north_america = data[2].text
        north_america_list.append(north_america)

        europe = data[3].text
        europe_list.append(europe)

        japan = data[4].text
        japan_list.append(japan)

        rest_of_world = data[5].text
        world_list.append(rest_of_world)

        global_sale = data[6].text
        globe_list.append(global_sale)
    except IndexError:
        pass
    print("{}\n {}|{}|{}|{}|{}".format(console, north_america, europe, japan, rest_of_world, global_sale))

dict = {'Console': console_list, 'North America': north_america_list,  'Europe': europe_list, 'Japan': japan_list,
        'Rest of the World': world_list, 'Global': globe_list}
df = pd.DataFrame(dict)
print(df)
