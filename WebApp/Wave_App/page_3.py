from h2o_wave import main, app, Q, ui, data
import occupation_distribution, edu_distribution, graph_age,age_amount, wph_amount


def add_card(q, name, card) -> None:
    q.client.cards.add(name)
    q.page[name] = card


def show_content(q:Q):
    add_card(q, 'intro_article', ui.tall_article_preview_card(
        box=ui.box('vertical', height='450px'),
        title='Visualizing Data Brilliance: Unleashing Insights through Representation',
        image='https://silvarohan18.github.io/test/artificial-intelligence-5866644.jpg',
        content='''
Data representation plays a pivotal role in the realm of information dissemination and understanding complex datasets. 
Effective data representation involves transforming raw data into visual or tabular formats that facilitate comprehension and insights. 
Graphs, charts, and infographics are widely used to showcase trends, patterns, and relationships within the data. 
They provide a quick overview of the data's characteristics, aiding decision-making processes and identifying actionable outcomes. 
Additionally, data representation enables efficient communication of findings to diverse audiences, making it an essential tool in various fields 
like business, science, and academia. By harnessing the power of data representation, organizations and individuals can unlock the full potential 
of their data and gain a competitive edge in today's data-driven world.
            '''
    ))

    add_card(q, 'occupation_article', ui.preview_card(
        name='preview_card',
        box=ui.box('vertical', height='190px'),
        image='https://silvarohan18.github.io/test/artificial-intelligence-5866644.jpg',
        title='Occupation',
        items=[
        ],
        caption='''
The Occupation Chart offers valuable insights into the dataset's occupational distribution, revealing a diverse workforce representation.The prominence of "Prof-specialty," "Craft-repair," and "Exec-managerial" suggests a significant presence of skilled and managerial professionals. 
Additionally, the substantial proportion of "Adm-clerical" and "Sales" occupations indicates the administrative and sales-oriented nature of the dataset.Notably, the "Other-service" category demonstrates a considerable segment of service-related roles.
The presence of "Machine-op-inspct," "Transport-moving," and "Handlers-cleaners" highlights the contribution of labor-intensive occupations.Overall, this data representation offers a comprehensive view of the dataset's occupational landscape, aiding in understanding the distribution and diversity of professions present.
                    ''',

        label='',
    ))

    add_card(q, 'chart_occupation', ui.plot_card(
        box=ui.box('vertical', height='500px'),
        title='Occupation Distribution',
        data=data('Occupation Count', 5, rows=occupation_distribution.rows),
        plot=ui.plot([ui.mark(type='interval', x='=Occupation', y='=Count', y_min=0)])
    ))

    add_card(q, 'exploring_article', ui.preview_card(
        name='preview_card',
        box=ui.box('vertical', height='200px'),
        image='https://silvarohan18.github.io/test/artificial-intelligence-5866644.jpg',
        title='Exploring the Diversity of Academic Attainments',
        items=[
        ],
        caption='''
The Education distribution showcases the diverse educational backgrounds within the dataset. "HS-grad" is the most common educational attainment,
representing 32.25% of the dataset, followed by Some-college at 22.39%. Bachelors accounts for 16.45% and Masters for 5.29%. 
Notably, Assoc-voc and 11th have significant representation at 4.24% and 3.61% respectively. "Assoc-acdm" and "10th" make up 3.28% and 2.87%. 
The chart also includes smaller percentages for other education levels, such as 7th-8th, Prof-school, and Doctorate.
Interestingly, Preschool and 1st-4th show the lowest representation at 0.16% and 0.52%. 
This data representation offers crucial insights into the education distribution, highlighting the varying educational backgrounds
and the workforce's academic diversity within the dataset.
                ''',

        label=''
    ))

    add_card(q, 'chart_edu', ui.plot_card(
        box=ui.box('vertical', height='500px'),
        title='Education Distribution',
        data=data('Education Count', 5, rows=edu_distribution.rows),
        plot=ui.plot([ui.mark(type='interval', x='=Education', y='=Count', y_min=0)])
    ))

    add_card(q, 'agevscount_des_article', ui.preview_card(
        name='preview_card',
        box=ui.box('vertical', height='190px'),
        image='https://silvarohan18.github.io/test/artificial-intelligence-5866644.jpg',
        title='Age vs Count',
        items=[
        ],
        caption='''
The "Age vs Count" graph is a powerful tool that offers a comprehensive view of data distribution based on age. By visualizing the number of data points within specific age ranges, it sheds light on the age demographics present in the dataset. This valuable insight aids in identifying age-related trends and patterns, providing a deeper understanding of the dataset's composition. Exploring this visualization uncovers the age distribution's nuances, enabling data analysts to make data-driven decisions and derive meaningful conclusions. From detecting age-specific patterns to gaining a holistic perspective of the data, the "Age vs Count" graph is a key component in unraveling intriguing insights from the dataset. 
                ''',

        label=''
    ))

    add_card(q, 'chart_agecount', ui.plot_card(
        box='vertical',
        title='Count vs Age',
        data=data('Age Count', 5, rows=graph_age.rows),
        plot=ui.plot([ui.mark(type='interval', x='=Age', y='=Count', y_min=0)])
    ))

    add_card(q, 'amountvsage_des_article', ui.preview_card(
        name='preview_card',
        box=ui.box('vertical', height='200px'),
        image='https://silvarohan18.github.io/test/artificial-intelligence-5866644.jpg',
        title='Amount vs Age Distribution',
        items=[
        ],
        caption='''
In this enlightening data visualization, we juxtapose the target variable "amount" against age distribution to reveal the intricate relationship between these two crucial factors. By exploring this interactive chart, users can discern how the target amount varies across different age groups. Uncover potential trends, such as whether certain age cohorts tend to have higher or lower amounts. These insights can empower businesses to tailor their offerings to specific age demographics, optimize marketing strategies, and enhance financial planning. Whether confirming existing hypotheses or unveiling novel patterns, this visualization equips users with invaluable insights to drive data-informed decisions. Step into the world of "Amount vs. Age Distribution" and unleash the transformative power of data-driven exploration.
                    ''',
        label=''
    ))

    add_card(q, 'chart_ageamount', ui.plot_card(
        box='vertical',
        title='Amount vs Age Distribution',
        data=data('category Amount Age Count', 10, rows=age_amount.rows),
        plot=ui.plot([ui.mark(type='interval', x='=Age', y='=Count', color='=Amount', stack='auto',
                              dodge='=category', y_min=0)])
    ))

    add_card(q, 'amount_vs_hpw_article', ui.preview_card(
        name='preview_card',
        box=ui.box('vertical', height='250px'),
        image='https://silvarohan18.github.io/test/artificial-intelligence-5866644.jpg',
        title='Amount vs Hours per week',
        items=[
        ],
        caption='''

In the captivating data visualization of "Amount vs. Hours per Week," we delve into the correlation between the target variable "amount" and the weekly working hours. This interactive chart allows users to explore how the target amount varies across different levels of work hours. Analyzing this relationship can reveal valuable insights, such as whether individuals who work longer hours tend to have higher or lower amounts. By understanding this connection, businesses and policymakers can make informed decisions, optimize workforce planning, and identify opportunities for financial growth or cost optimization. Whether uncovering patterns or confirming assumptions, this visualization empowers users to make data-driven choices with confidence. Explore the intricacies of this dynamic chart, unravel trends, and harness the transformative potential of data insights in shaping a prosperous future. 
                    ''',
        label=''
    ))

    add_card(q, 'chart_amount_vs_hpw', ui.plot_card(
        box='vertical',
        title='Amount vs Hours per week(HPW)',
        data=data('category country HPW Count', 10, rows=wph_amount.rows),
        plot=ui.plot([ui.mark(type='interval', x='=HPW', y='=Count',
                              color='=country', stack='auto',
                              dodge='=category', y_min=0)])
    ))
