import pytest


@pytest.mark.non_travis
def test_search():
    import vcr
    from we_get.modules.the_pirate_bay import the_pirate_bay
    cl = the_pirate_bay('')
    cl.search_query = 'ubuntu'
    with vcr.use_cassette('fixtures/test_the_pirate_bay_test_search.yaml', record_mode='new_episodes'):
        res = cl.search()
        assert res
        assert any('user_status' in res[k] for k in res)
        assert any('vip' == res[k]['user_status'] for k in res)
        assert any('trusted' == res[k]['user_status'] for k in res)
