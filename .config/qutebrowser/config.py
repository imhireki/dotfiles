# type: ignore
# Documentation:
#  -> qute://help/configuring.html
#  -> qute://help/settings.html

import catppuccin
catppuccin.setup(c, 'macchiato')

# Change the argument to True to still load settings configured via autoconfig.yml
config.load_autoconfig(False)

# Cookies: all, no-3rdparty, no-unknown-3rdparty, never
config.set('content.cookies.accept', 'all', 'chrome-devtools://*')
config.set('content.cookies.accept', 'all', 'devtools://*')

# Headers
# config.set('content.headers.user_agent', 'Mozilla/5.0 ({os_info}) AppleWebKit/{webkit_version} (KHTML, like Gecko) {upstream_browser_key}/{upstream_browser_version} Safari/{webkit_version}', 'https://web.whatsapp.com/')
# config.set('content.headers.accept_language', '', 'https://matchmaker.krunker.io/*')

# Load images automatically in web pages.
config.set('content.images', True, 'chrome-devtools://*')
config.set('content.images', True, 'devtools://*')

# Enable JavaScript.
config.set('content.javascript.enabled', True, 'chrome-devtools://*')
config.set('content.javascript.enabled', True, 'devtools://*')
config.set('content.javascript.enabled', True, 'chrome://*/*')
config.set('content.javascript.enabled', True, 'qute://*/*')

# Keybindings
config.bind('<Ctrl-y>', 'hint links spawn --detach mpv --title=browser_player {hint-url}')
config.bind('<Ctrl-l>', 'hint links yank')

# Background color for webpages if unset (or empty to use the theme's color).
c.colors.webpage.bg = '#1e1e2e'

# Pages
c.url.default_page = 'https://searx.be'
c.url.start_pages = 'https://searx.be'

# Search engines
c.url.searchengines = {
    "DEFAULT": "https://searx.be/search?q={}",

    "yt": "https://www.youtube.com/results?search_query={}",
    "py": "https://docs.python.org/3/search.html?q={}",
    "dj": "https://docs.djangoproject.com/en/4.1/search/?q={}",
    "aw": "https://wiki.archlinux.org/index.php?search={}",

    "it": "https://searx.be/search?q={}&categories=it",
    "ma": "https://searx.be/search?q={}&categories=map",
    "ne": "https://searx.be/search?q={}&categories=news",
    "im": "https://searx.be/search?q={}&categories=images",
    "fi": "https://searx.be/search?q={}&categories=files",
}

