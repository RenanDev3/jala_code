from src.file_helper import search_files, read_data


def test_search_files_dummyextension_returns_non_empty_list():
    path = r'C:\workspace\Jala\Python\dev_demos\demo2\test_files'
    extension = 'dummy'
    files = search_files(path, extension)
    assert files is not None, 'expected non null list'


def test_search_files_json_extension_returns_non_empty_list():
    path = r'C:\workspace\Jala\Python\dev_demos\demo2\test_files'
    extension = 'json'
    files = search_files(path, extension)
    assert files is not None, 'expected non null list'
    assert type(files) is list, 'expected a list'

    assert len(files) == 2, 'expected 2 elements'


def test_read_data_known_filenames_returns_non_empty_list():
    files = [
        r'C:\workspace\Jala\Python\dev_demos\demo2\test_files\data_page_09012022000000.json',
        r'C:\workspace\Jala\Python\dev_demos\demo2\test_files\data_page_09302022000000.json']
    data = read_data(files)
    assert data is not None, 'expected non null list'
    assert type(data) is list, 'expected a list'
    assert len(data) > 0, 'expected non empty list'


def test_read_data_dummy_filenames_returns_empty_list():
    files = [
        r'C:\workspace\Jala\Python\dev_demos\demo2\doesnt_exist\data_page_09012022000000.json',
        r'C:\workspace\Jala\Python\dev_demos\demo2\doesnt_exist\data_page_09302022000000.json']
    data = read_data(files)
    assert data is not None, 'expected non null list'
    assert type(data) is list, 'expected a list'
    assert len(data) == 0, 'expected empty list'
