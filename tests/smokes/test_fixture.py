import requests




def test_run_server(local_server_url, root):
    from time import sleep
    sleep(2.0)
    print(requests.get(local_server_url).text)
    assert requests.get(local_server_url).text == 'kek'
