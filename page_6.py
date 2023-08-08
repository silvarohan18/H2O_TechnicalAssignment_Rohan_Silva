
from h2o_wave import main, app, Q, ui

def add_card(q, name, card) -> None:
    q.client.cards.add(name)
    q.page[name] = card



def show_content(q:Q):
    add_card(q, 'article', ui.tall_article_preview_card(
        box=ui.box('vertical', height='400px'), title='Empowering Insights for Informed Business Decisions',
        image='https://silvarohan18.github.io/test/artificial-intelligence-5866644.jpg',
        content='''
The Data Surfer Wave App is a game-changer in the world of data exploration and analysis. Designed to empower users with valuable insights, this app is a treasure trove of information derived from extensive census data analysis. With its intuitive interface and interactive visualizations, users can effortlessly navigate through the complexities of demographic trends and patterns.From businesses seeking location-based strategies to nonprofits focused on social impact analysis, the Data Surfer Wave App caters to a diverse range of industries. Its machine learning capabilities enable users to predict outcomes, making it a powerful tool for informed decision-making.Beyond its functional prowess, the app offers a delightful user experience. Its captivating visuals, user-friendly design, and seamless navigation ensure that users stay engaged and find value in every interaction.With the Data Surfer Wave App at their disposal, users can explore, analyze, and draw meaningful conclusions from data, leading to data-driven insights and transformative outcomes. Whether you're a data enthusiast, a business analyst, or a decision-maker, this app is the key to unlocking the true potential of census data and propelling your success to new heights.
                   '''
    ))
    add_card(q, 'article1', ui.tall_article_preview_card(
        box=ui.box('vertical', height='450px'), title='Market Segmentation',
        image='https://silvarohan18.github.io/test/analysis.jpg',
        content='''
Step into the world of precision marketing with Data Surfer Wave, where market segmentation becomes a breeze. Unravel the diverse demographic characteristics, including age, education, income, and location, and gain a deeper understanding of your audience. Data Surfer Wave empowers you to identify distinct market segments and their unique preferences and behaviors. Tailor your marketing campaigns and product offerings to resonate with each segment, enhancing customer engagement and loyalty. With a user-friendly interface and powerful insights, Data Surfer Wave transforms your data into actionable marketing strategies. Embrace the art of segmentation and witness your business soar to new heights of success. Ride the wave of data-driven decision-making and leave a lasting impact on your target market.
      '''
    ))

    add_card(q, 'article2', ui.tall_article_preview_card(
        box=ui.box('vertical', height='500px'), title='Workforce Planning',
        image='https://silvarohan18.github.io/test/workfoce.png',
        content='''
Data Surfer Wave is your compass for strategic workforce planning, providing valuable age distribution and educational background insights. Sail into the future with confidence, as you analyze age distribution to prepare for upcoming talent needs and potential retirements. Seamlessly transition knowledge and skills within your organization, ensuring a steady course of success. With Data Surfer Wave, explore the educational background of your workforce, identifying areas for upskilling and targeted hiring. Stay ahead of the competition by aligning your team's expertise with your business objectives. Embark on a transformative journey of workforce optimization and chart a course towards a dynamic, agile, and future-ready organization. Data Surfer Wave is your ultimate navigator for informed decision-making in the ever-changing workforce landscape.
               '''
    ))

    add_card(q, 'article3', ui.tall_article_preview_card(
        box=ui.box('vertical', height='550px'), title='Employee Retention',
        image='https://silvarohan18.github.io/test/Employee.png',
        content='''
In the dynamic world of workforce management, the Data Surfer Wave App is a game-changer for businesses seeking to understand and enhance employee retention. With the Census Data Explorer, gain valuable insights into employee demographics, job categories, and work hours, all critical factors influencing job satisfaction and retention rates. Armed with this knowledge, companies can craft targeted employee engagement initiatives to boost satisfaction and loyalty. For instance, leveraging data on work hours, a technology firm may introduce flexible schedules and remote work options to promote work-life balance and reduce burnout, leading to a more content and committed workforce. Harness the power of data-driven decision-making with Data Surfer Wave, paving the way for a stable and motivated team, driving business prosperity. Unlock a world of possibilities with Data Surfer Wave as your compass, navigating the seas of workforce data to steer your organization towards higher employee retention and lasting success.              
                    '''
    ))

    add_card(q, 'article4', ui.tall_article_preview_card(
        box=ui.box('vertical', height='600px'), title='Location-Based Strategies',
        image='https://silvarohan18.github.io/test/location.jpeg',
        content=
        '''
In the vast ocean of data, Data Surfer Wave equips businesses with an essential compass: Location-Based Strategies. By diving into population density and household composition insights, companies can chart their course towards the most promising locations for new stores or service centers. Understanding the demographic makeup of different regions empowers businesses to tailor offerings to local demands and preferences with precision. For instance, a grocery chain can use these insights to strategically open larger stores with diverse family-oriented products in regions with a higher percentage of households with children. This data-driven approach propels businesses to seize market opportunities, ride the waves of success with increased foot traffic, higher sales, and soaring customer loyalty. Let Data Surfer Wave be your strategic guide to navigate the ever-changing tides of the market and unlock the treasure trove of location-based opportunities.
                       '''
    ))

    add_card(q, 'article5', ui.tall_article_preview_card(
        box=ui.box('vertical', height='600px'), title='Social Impact Analysis',
        image='https://silvarohan18.github.io/test/Social_Impact.jpg',
        content='''

Data Surfer Wave, an ingenious data exploration tool, holds the key to profound social impact analysis by unraveling demographic trends encompassing education, income, and occupation. This revolutionary platform equips businesses and organizations to evaluate the effectiveness of social programs and policies while pinpointing areas for targeted interventions. Non-profit organizations can harness its vast potential to identify regions with low education levels, driving the development of tailored educational initiatives that uplift communities. As a visionary change-maker, ride the waves of Data Surfer Wave, illuminating a path towards a more equitable and prosperous future for all. Let data be your guide, as you embark on a transformative journey of informed, impactful decisions, steering society towards lasting, inclusive progress. Embrace Data Surfer Wave and ride the data-driven wave to a brighter, more equitable future. Explore, analyze, and make well-informed choices with the abundance of insights at your disposal, and steer your business towards success!
    '''
    ))