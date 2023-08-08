from h2o_wave import main, app, Q, ui
import test_table_config


def add_card(q, name, card) -> None:
    q.client.cards.add(name)
    q.page[name] = card


def show_content(q: Q):
    add_card(q, 'intro_article', ui.tall_article_preview_card(
        box=ui.box('vertical', height='450px'), title='Empower Your Decision-Making',
        subtitle='',
        image='https://silvarohan18.github.io/test/artificial-intelligence-5866644.jpg',

        content='''
As the horizon of data-driven decision-making expands, Data Surfer Wave emerges as your trusted guide in the landscape of predictive analytics. Seamlessly integrating your trained model with real-world test data, it becomes an essential tool for translating insights into strategic actions. Ride the waves of data-driven success and embrace the future of informed choices. The seamless integration of test data import and model predictions not only enhances user experience but also empowers them to actualize their machine learning endeavors with tangible outcomes.Embark on a transformative journey where the synergy of test data and a trained Random Forest model comes to life within Data Surfer Wave. This harmonious fusion propels you beyond data exploration into the realm of actionable foresight. Uncover hidden nuances, make confident decisions, and navigate the currents of innovation. Your machine learning aspirations materialize into impactful results, with test data import and model predictions seamlessly bridging the gap between theory and practice.
  
               ''',
    ))

    add_card(q, 'article8', ui.preview_card(
        name='preview_card',
        box=ui.box('vertical', height='200px'),
        image='https://silvarohan18.github.io/test/artificial-intelligence-5866644.jpg',
        title='Test Data',
        items=[
        ],
        caption='''
 Import test data seamlessly into Data Surfer Wave and set the stage for informed decisions. With your trained Random Forest model, harness predictive power and transform data into actionable insights. This streamlined process bridges the gap between theoretical potential and real-world impact, revolutionizing your decision-making paradigm            
 ''',

        label=''
    ))

    add_card(q, 'table_1', ui.form_card(box=ui.box('vertical', height='400px'), items=[ui.table(
        name='table',
        downloadable=False,
        resettable=False,
        groupable=False,
        columns=test_table_config.column,
        rows=[ui.table_row(
            name='ss',
            cells=[str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]),
                   str(row[7]),
                   str(row[8]), str(row[9]), str(row[10]), str(row[11]), str(row[12]), str(row[13]), str(row[14]), ]
        ) for index, row in test_table_config.subset_df.iterrows()])
    ]))

    add_card(q, 'button', ui.form_card(box='vertical', items=[
        ui.button(name='button', label='Let\'s See The Results')
    ]))

    if q.args.button:
        add_card(q, 'article1', ui.preview_card(
            name='preview_card',
            box=ui.box('vertical', height='150px'),
            image='https://silvarohan18.github.io/test/artificial-intelligence-5866644.jpg',
            title='Predicted Results',
            items=[
            ],
            caption='''
Elevate your data-driven journey with Data Surfer Wave's Predicted Results Table—an invaluable tool translating predictive power into actionable insights. Seamlessly organized, this table illuminates the correlation between your trained Random Forest model's predictions and real-world data. Explore predictions with clarity, from individual instances to trends across scenarios. Make informed decisions as you delve into the nuances of model performance, validating hypotheses and identifying outliers. As a bridge between theoretical potential and practical outcomes, the Predicted Results Table empowers strategic action, enabling you to navigate the waves of success armed with data-backed foresight. Embrace a future of precision decision-making today.
                                
                                   ''',
            label=''
        ))

        add_card(q, 'table1', ui.form_card(box='vertical', items=[ui.table(
            name='table1',
            downloadable=False,
            resettable=False,
            groupable=False,
            columns=[
                ui.table_column(name='actual', label='Actual Value'),
                ui.table_column(name='predicted', label='Predicted Value'),
                ui.table_column(name='tag', label='Status', filterable=False, cell_type=ui.tag_table_cell_type(
                    name='tags',
                    tags=[
                        ui.tag(label='NOT-PREDICTED', color='$red'),
                        ui.tag(label='PREDICTED', color='$mint'),
                    ]
                ))
            ],
            rows=[
                ui.table_row(name='row1', cells=['<=50K', '<=50K', 'PREDICTED']),
                ui.table_row(name='row2', cells=['<=50K', '<=50K', 'PREDICTED']),
                ui.table_row(name='row2', cells=['>50K', '<=50K', 'NOT-PREDICTED']),
                ui.table_row(name='row2', cells=['>50K', '>50K', 'PREDICTED']),

            ])
        ]))





