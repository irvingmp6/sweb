def get_help_menu() -> dict:
    menu = {}
    menu['debug'] = """Shows errors as standard out"""
    menu['desc'] = """A command-line tool that returns results from mainstream search engines."""
    menu['exclude-domains'] = """Specifies the domain(s) the search should exclude"""
    menu['only-domains'] = """Specifies the domain(s) the search should focus on"""
    menu['only-domains-from-file'] = """Specifies the domain(s) the search should focus on from txt file"""
    menu['timeout'] = """Specifies the timeout threshold per search request"""
    menu['verbose'] = """Shows activity as standard out"""
    menu['save-results'] = """Writes the text from each visited page to file called chips.txt"""
    menu['save-urls'] = """Writes the urls from each visited page to a file called all_urls.txt"""
    menu['search-engines'] = """list of specific search engines to be queried"""
    menu['search_phrase'] = """Phrases you would normally enter in the search bar."""
    return menu
