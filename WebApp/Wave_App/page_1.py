from h2o_wave import main, app, Q, ui


def add_card(q, name, card) -> None:
    q.client.cards.add(name)
    q.page[name] = card


def show_content(q: Q):
    add_card(q, 'intro_article', ui.tall_article_preview_card(
        box=ui.box('vertical', height='620px', ), title='Welcome to DataSurfer Wave',
        image='https://silvarohan18.github.io/test/artificial-intelligence-5866644.jpg',
        content=

        '''
Embark on an exhilarating journey of discovery with DataSurfer Wave! Unleash the full potential of your data and ride the waves of insights like never before. Our powerful Wave App empowers you to navigate through the vast ocean of information effortlessly, uncovering hidden patterns, trends, and correlations that shape your world. With visually captivating charts, graphs, and statistics, DataSurfer Wave makes data exploration a thrilling and rewarding experience. Whether you're a seasoned data expert or a curious novice, our user-friendly interface ensures you can confidently surf through your data and make informed decisions that drive success. Dive in and ride the waves of knowledge with DataSurfer Wave, and chart your course towards data-driven excellence!
        '''
    ))

    add_card(q, 'data_preview_article', ui.preview_card(
        name='preview_card',
        box=ui.box('vertical', height='250px'),
        image='https://silvarohan18.github.io/test/data2.jpg',
        title='Census Data Preview',
        items=[
        ],
        caption='''
    Uncover intriguing insights from vast demographic data, embark on an exploration journey, and visualize data with dynamic charts. Make informed decisions using interactive features, predictive analytics, and real-time updates. Experience the transformative power of census data, driving progress and shaping the future.           
                        ''',
        label=''
    ))

    add_card(q, 'data_representation_article', ui.preview_card(
        name='preview_card',
        box=ui.box('vertical', height='250px'),
        image='https://silvarohan18.github.io/test/Data.jpg',
        title='Data Representation',
        items=[
        ],
        caption='''
    Data representation is crucial for disseminating information and understanding complex datasets. It involves converting raw data into visual or tabular formats to facilitate comprehension and insights. Graphs, charts, and infographics showcase trends, aiding decision-making and identifying actionable outcomes. Efficiently communicating findings to diverse audiences makes it essential in business, science, and academia. Utilizing data representation unlocks data's potential and offers a competitive edge in the data-driven world.
                        ''',
        label=''
    )
             )

    add_card(q, 'ml_prediction_article', ui.preview_card(
        name='preview_card',
        box=ui.box('vertical', height='250px'),
        image='https://silvarohan18.github.io/test/ML.jpg',
        title='ML Predictions',
        items=[
        ],
        caption='''
    Your gateway to uncovering intriguing insights from the vast world of demographic data!
    Dive into the depths of census data and embark on a data exploration journey like never before. Our powerful Wave App, Census Data Explorer, 
    empowers you to navigate through a wealth of demographic information effortlessly. Discover the fascinating patterns and trends that shape societies,

                        ''',
        label=''
    ))

    add_card(q, 'chatbot_article', ui.preview_card(
        name='preview_card',
        box=ui.box('vertical', height='250px'),
        image='https://silvarohan18.github.io/test/location.jpeg',
        title='Results',
        items=[
        ],
        caption='''
Data Surfer Wave is your beacon in the landscape of predictive analytics. By seamlessly integrating your trained model with real-world test data, it empowers strategic action from insights. Embrace informed choices and ride the waves of data-driven success. This seamless synergy enhances user experience, transforming machine learning aspirations into tangible outcomes, propelling you into actionable foresight 

                        ''',
        label=''
    ))

    add_card(q, 'insight_article', ui.preview_card(
        name='preview_card',
        box=ui.box('vertical', height='250px'),
        image='https://silvarohan18.github.io/test/Data.jpg',
        title='Insights',
        items=[
        ],
        caption='''
Your gateway to uncovering intriguing insights from the vast world of demographic data!
Dive into the depths of census data and embark on a data exploration journey like never before. Our powerful Wave App, Census Data Explorer, 
empowers you to navigate through a wealth of demographic information effortlessly. Discover the fascinating patterns and trends that shape societies,

                        ''',
        label=''
    ))
