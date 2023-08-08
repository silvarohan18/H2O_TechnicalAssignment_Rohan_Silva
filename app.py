from h2o_wave import main, app, Q, ui, on, handle_on
from typing import Optional, List

import page_1, page_2, page_3, page_4, page_5, page_6, page_layout


def add_card(q, name, card) -> None:
    q.client.cards.add(name)
    q.page[name] = card


def clear_cards(q, ignore: Optional[List[str]] = []) -> None:
    if not q.client.cards:
        return
    for name in q.client.cards.copy():
        if name not in ignore:
            del q.page[name]
            q.client.cards.remove(name)


@on('#page1')
async def page1(q: Q):
    clear_cards(q)
    page_1.show_content(q)


@on('#page2')
async def page2(q: Q):
    clear_cards(q)  # When routing, drop all the cards except of the main ones (header, sidebar, meta).
    page_2.show_content(q)


@on('#page3')
async def page3(q: Q):
    clear_cards(q)  # When routing, drop all the cards except of the main ones (header, sidebar, meta).
    page_3.show_content(q)


@on('#page4')
async def handle_page4(q: Q):
    clear_cards(q, ['form'])
    page_4.show_content(q)


@on('#page5')
async def page5(q: Q):
    clear_cards(q)
    page_5.show_content(q)


@on('#page6')
async def page6(q: Q):
    clear_cards(q)
    page_6.show_content(q)


async def init(q: Q) -> None:
    q.page['meta'] = page_layout.get_meta(q)

    q.page['header'] = page_layout.get_header(q)

    q.page['footer'] = page_layout.get_footer(q)

    if q.args['#'] is None:
        await page1(q)


@app('/')
async def serve(q: Q):
    if not q.client.initialized:
        q.client.cards = set()
        await init(q)
        q.client.initialized = True

    await handle_on(q)
    await q.page.save()
