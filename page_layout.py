from h2o_wave import main, app, Q, ui


def get_header(q: Q):
    return ui.header_card(
        box='header',
        title='DataSurfer Wave',
        subtitle="Empowering Insights with DataSurfer",
        image='https://silvarohan18.github.io/test/Logo.PNG',
        secondary_items=[
            ui.tabs(
                name='tabs',
                value=f'#{q.args["#"]}' if q.args['#'] else '#page1',
                link=True,
                items=
                [
                    ui.tab(name='#page1', label='Home'),
                    ui.tab(name='#page2', label='Census Data'),
                    ui.tab(name='#page3', label='Data Representation'),
                    ui.tab(name='#page4', label='ML Predictions'),
                    ui.tab(name='#page5', label='Results'),
                    ui.tab(name='#page6', label='Insights'),
                ]),
        ],
        items=
        [
            ui.persona(
                title='Rohan Silva',
                subtitle='Devops Engineer',
                size='xs',
                image='https://lh3.googleusercontent.com/a/AAcHTtdyNUrHvsivS27GAXnD2tbP9vhrvEGK4TLolJIglI5OwZgv=s360-c-no'),
        ]
    )


def get_footer(q: Q):
    return ui.footer_card(
        box='footer',
        caption='![wave-logo](https://silvarohan18.github.io/test/footer.PNG)',
        items=[
            ui.inline(justify='end', items=[
                ui.links(label='On Social Media', width='200px', items=[
                    ui.link(label='LinkedIn', path='https://www.h2o.ai/', target='_blank'),
                    ui.link(label='FaceBook', path='https://www.h2o.ai/', target='_blank'),
                    ui.link(label='Instagram', path='https://www.h2o.ai/', target='_blank'),
                    ui.link(label='Twitter', path='https://www.h2o.ai/', target='_blank'),
                    ui.link(label='G-Plus', path='https://www.h2o.ai/', target='_blank'),
                    ui.link(label='Blog', path='https://www.h2o.ai/', target='_blank'),
                    ui.link(label='Threads', path='https://www.h2o.ai/', target='_blank'),
                    ui.link(label='TikTok', path='https://www.h2o.ai/', target='_blank'),
                ]),
                ui.links(label='News & Info', width='200px', items=[
                    ui.link(label='Accesibility', path='https://www.h2o.ai/', target='_blank'),
                    ui.link(label='Terms & Conditions', path='https://www.h2o.ai/', target='_blank'),
                    ui.link(label='Ongoing Projects', path='https://www.h2o.ai/', target='_blank'),
                    ui.link(label='Latest Trends', path='https://www.h2o.ai/', target='_blank'),
                    ui.link(label='Contact Us', path='https://www.h2o.ai/', target='_blank'),
                    ui.link(label='Ideas & Innovations', path='https://www.h2o.ai/', target='_blank'),
                    ui.link(label='DataWave Community', path='https://www.h2o.ai/', target='_blank'),
                ]),
            ]),
        ]
    )


def get_meta(q: Q):
    return ui.meta_card(box='vertical',
                        layouts=[ui.layout(breakpoint='xs', min_height='300vh',
                                           zones=[
                                               ui.zone('header'),
                                               ui.zone('content',
                                                       zones=[
                                                           ui.zone('horizontal', direction=ui.ZoneDirection.ROW),
                                                           ui.zone('vertical'),
                                                           ui.zone('grid', direction=ui.ZoneDirection.ROW,
                                                                   wrap='stretch',
                                                                   justify='center'),
                                                       ]),

                                               ui.zone('footer')
                                           ])])
