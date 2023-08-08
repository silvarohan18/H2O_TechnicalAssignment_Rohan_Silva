from h2o_wave import main, app, Q, ui
import table_config


def add_card(q, name, card) -> None:
    q.client.cards.add(name)
    q.page[name] = card


def show_content(q: Q):
    add_card(q, 'welcome_article', ui.tall_article_preview_card(
        box=ui.box('vertical', height='450px'), title='Welcome to the Census Data!',
        image='https://silvarohan18.github.io/test/artificial-intelligence-5866644.jpg',

        content='''

Welcome to Census Data Explorer, your gateway to uncovering intriguing insights from the vast world of demographic data! 
Dive into the depths of census data and embark on a data exploration journey like never before. Our powerful Wave App, Census Data Explorer, 
empowers you to navigate through a wealth of demographic information effortlessly. 
Discover the fascinating patterns and trends that shape societies, visualize data with dynamic charts, and make informed decisions with interactive
features. With predictive analytics, real-time updates, and mobile-friendly access, Census Data Explorer ensures a seamless and secure exploration 
experience. Join us on this data-driven voyage, and experience the transformative power of census data in driving progress and shaping the future. 
Unlock a world of fascinating insights with Census Data Explorer, your ultimate destination for illuminating the depths of demographic data. 
Immerse yourself in the rich tapestry of census information and embark on an unparalleled data exploration odyssey. 
Experience the magic of dynamic chart visualizations, predictive analytics, and real-time updates, all seamlessly accessible through our powerful Wave App.
Join us on this enthralling data-driven journey as we unravel the transformative potential of census data in shaping societies and driving a brighter future.

                '''
    ))

    add_card(q, 'preview_article', ui.preview_card(
        name='preview_card',
        box=ui.box('vertical', height='200px'),
        image='https://silvarohan18.github.io/test/artificial-intelligence-5866644.jpg',
        title='Preview of the Census Data',
        items=[
        ],
        caption='''
In the DataSurfer Wave App, you have the opportunity to unleash the full potential of your census data by effortlessly uploading the attached dataset (census_data.csv) to our platform. Once uploaded, the app intelligently displays a preview of the dataset, allowing you to get a quick glimpse of its structure and contents. This intuitive feature saves you time and effort, as you can easily assess the data before diving into in-depth analysis. The preview provides a sneak peek into the key data points, enabling you to understand the distribution of data and identify any immediate patterns or trends. You can interact with this subset of the data, exploring different columns and values, and even apply basic filtering to refine your data exploration. With a user-friendly and visually engaging interface, the DataSurfer Wave App makes data handling and visualization a breeze. The seamless preview experience ensures you can make informed decisions about how to proceed with your analysis, setting the stage for a successful and insightful data exploration journey.

                            ''',
        label=''
    ))

    add_card(q, 'table', ui.form_card(box=ui.box('vertical'), items=[ui.table(
        name='table',
        downloadable=True,
        resettable=True,
        groupable=True,
        columns=table_config.column,
        rows=[ui.table_row(
            name=str(row),
            cells=[str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]),
                   str(row[7]),
                   str(row[8]), str(row[9]), str(row[10]), str(row[11]), str(row[12]), str(row[13]), str(row[14]), ]
        ) for index, row in table_config.subset_df[0:200].iterrows()])
    ]))
