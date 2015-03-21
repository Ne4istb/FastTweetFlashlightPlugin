import urllib
import json
import i18n


def results(parsed, original_query):

    angular_specs = [
        ["~query", "https://docs.angularjs.org/api"]
    ]
    for key, url in angular_specs:
        if key in parsed:
            search_query = parsed[key].encode('UTF-8')
            title = i18n.localstr("Search in Angular Docs '{0}'").format(search_query)
            return {
                "title": title,
                "run_args": [url],
                "html": """
                <script>
                setTimeout(function() {
                    window.location = %s;
                    setTimeout(function() {
                        alert('directive');
                        var searchInput = document.getElementsByClassName('search-query');
                        var scope = angular.element(searchInput).scope();
                        scope.q = 'directive';
                        scope.search = 'directive';
                    }, 1000);
                }, 500);
                </script>
                """ % (json.dumps(url)),
                "webview_user_agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 7_0 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Version/7.0 Mobile/11A465 Safari/9537.53",
                "webview_links_open_in_browser": True
            }


def run(url):
    import os
    os.system('open "{0}"'.format(url))
