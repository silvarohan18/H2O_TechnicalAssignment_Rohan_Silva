from h2o_wave import main, app, Q, ui, data
import test_table_config

button1_clicked=False
button2_clicked=False


def add_card(q, name, card) -> None:
    q.client.cards.add(name)
    q.page[name] = card


def show_content(q:Q):
    add_card(q, 'intro_article', ui.tall_article_preview_card(
        box=ui.box('vertical', height='450px'), title='Prophets of Data: Unleashing the Power of ML Predictions',
        subtitle='',
        image='https://silvarohan18.github.io/test/artificial-intelligence-5866644.jpg',

        content='''
Welcome to the ML Prediction Tab, where data and intelligence converge to shape the future of your business. Seamlessly integrated into the DataSurfer Wave App, this revolutionary feature from h2o.ai empowers you to make accurate predictions with ease. Unleash the power of machine learning, unraveling complex patterns and identifying hidden trends. From predicting customer churn to optimizing marketing strategies, the ML Prediction Tab propels your business towards unprecedented success. At h2o.ai, we believe in the transformative potential of data-driven decision-making. Our cutting-edge machine learning technology enables you to harness the full power of your data, unlocking actionable foresight and driving informed choices. With a user-friendly interface and robust capabilities, the ML Prediction Tab puts the future in your hands. Explore the synergy of data exploration and machine learning, and watch as your business transcends limits and unlocks untapped opportunities. The ML Prediction Tab serves as a catalyst for innovation, empowering you to stay ahead in today’s competitive landscape. Embrace the future of business intelligence with h2o.ai’s ML Prediction Tab and embark on a journey of success, driven by the precision and foresight of machine learning. Let your data tell the story of tomorrow, and be the prophet of your business’s destiny. Your path to data-driven success starts here, with h2o.ai's ML Prediction Tab as your guide.
           '''
    ))

    add_card(q, 'article1', ui.preview_card(
        name='preview_card1',
        box=ui.box('vertical', height='200px'),
        image='https://silvarohan18.github.io/test/artificial-intelligence-5866644.jpg',
        title='Random Forest with DataSurfer',
        items=[
        ],
        caption='''
The Random Forest algorithm is a versatile and widely used machine learning technique for both classification and regression tasks. It belongs to the ensemble learning family, where multiple individual models are combined to create a more robust and accurate predictive model. In the case of Random Forest, a collection of decision trees is built during training. Each tree is trained on a random subset of the training data and makes predictions independently. The final prediction is then determined by aggregating the predictions of all the individual trees, often through a majority vote (for classification) or averaging (for regression). Random Forest is known for its ability to handle complex data relationships, handle large datasets, and reduce overfitting, making it a popular choice in various domains.

In this web app "Data Surfer Wave," you have utilized the Random Forest algorithm to predict results. This algorithm's ability to provide accurate predictions while minimizing overfitting can be beneficial for your application's predictive tasks. If you're considering enhancing your app's capabilities, integrating it with H2O Wave ML could streamline the process of building, deploying, and managing your machine learning models within a dynamic web-based environment.
                      ''',
        label=''
    ))

    add_card(q, 'button', ui.form_card(box='vertical', items=[
        ui.button(name='button', label='Let\'s Train The Model With Data Surfer')
    ]))

    #Train data button
    if q.args.button:
        button1_clicked=True

        add_card(q, 'article', ui.preview_card(
            name='preview_card2',
            box=ui.box('vertical', height='180px'),
            image='https://silvarohan18.github.io/test/artificial-intelligence-5866644.jpg',
            title='Variable vs Importance',
            items=[
            ],
            caption='''

        Discover the heart of machine learning with Data Surfer Wave's Deviance vs. Number of Trees graph—an artistic masterpiece that unveils the intricate dance between accuracy and ensemble size. Immerse yourself in a symphony of insights as each line weaves a story of your model's evolution, guiding you to the optimal point where predictions flourish. With intuitive elegance, seamlessly integrated into our user-friendly interface, this graph empowers both seasoned data virtuosos and newcomers to craft predictions that resonate with the future. Elevate your predictive analytics journey today and let the graph paint the path to precision.
                            ''',

            label=''
        ))

        add_card(q, 'plot1', ui.plot_card(
            box='vertical',
            title='Variable vs Importance',
            data=data('variable scaled_importance', 5, rows=[
                ('sex', 0.0654),
                ('race', 0.0753),
                ('native-country', 0.1609),
                ('capital-loss', 0.2079),
                ('workclass', 0.2276),
                ('education', 0.3597),
                ('hours-per-week', 0.3630),
                ('fnlwgt', 0.4150),
                ('education-num', 0.5265),
                ('occupation', 0.5648),
                ('age', 0.6262),
                ('capital-gain', 0.6929),
                ('relationship', 0.8229),
                ('martial-status', 1),

            ]),
            plot=ui.plot([ui.mark(type='interval', x_title='Scaled Importance', y_title='Variable',
                                  x='=scaled_importance', y='=variable', y_min=0)])
        ))

        add_card(q, 'article6', ui.preview_card(
            name='preview_card',
            box=ui.box('vertical', height='180px'),
            image='https://silvarohan18.github.io/test/artificial-intelligence-5866644.jpg',
            title='Deviance vs. Number of Trees',
            items=[
            ],
            caption='''

Discover the heart of machine learning with Data Surfer Wave's Deviance vs. Number of Trees graph—an artistic masterpiece that unveils the intricate dance between accuracy and ensemble size. Immerse yourself in a symphony of insights as each line weaves a story of your model's evolution, guiding you to the optimal point where predictions flourish. With intuitive elegance, seamlessly integrated into our user-friendly interface, this graph empowers both seasoned data virtuosos and newcomers to craft predictions that resonate with the future. Elevate your predictive analytics journey today and let the graph paint the path to precision.
                    ''',

            label=''
        ))

        add_card(q, 'plot2', ui.plot_card(
            box='vertical',
            title='Deviance',
            data=data('training_deviance number_of_trees', 10,
                      rows=[
                          (0.1492, 1),
                          (0.1475, 2),
                          (0.1398, 3),
                          (0.1351, 4),
                          (0.1290, 5),
                          (0.1255, 6),
                          (0.1220, 7),
                          (0.1193, 8),
                          (0.1165, 9),
                          (0.1141, 10),
                          (0.1122, 11),
                          (0.1111, 12),
                          (0.1097, 13),
                          (0.1087, 14),
                          (0.1082, 15),
                          (0.1073, 16),
                          (0.1065, 17),
                          (0.1056, 18),
                          (0.1050, 19),
                          (0.1043, 20),
                          (0.1040, 21),
                          (0.1036, 22),
                          (0.1031, 23),
                          (0.1026, 24),
                          (0.1021, 25),
                          (0.1019, 26),
                          (0.1017, 27),
                          (0.1014, 28),
                          (0.1012, 29),
                          (0.1011, 30),
                          (0.1010, 31),
                          (0.1007, 32),
                          (0.1005, 33),
                          (0.1003, 34),
                          (0.1003, 35),
                          (0.1001, 36),
                          (0.1001, 37),
                          (0.1000, 38),
                          (0.1000, 39),
                          (0.0997, 40),
                          (0.0995, 41),
                          (0.0994, 42),
                          (0.0992, 43),
                          (0.0991, 44),
                          (0.0986, 50),
                      ]
                      ),
            plot=ui.plot([ui.mark(type='point', x_title='Number of Trees', y_title='Training Deviance',
                                  x='=number_of_trees', y='=training_deviance')])
        ))




