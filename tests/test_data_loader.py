# pylint: disable=C0114,C0116
import zipfile

from automotive.data_loader import unzip_raw_data


def create_archive(directory):
    archive_path = directory / "data.zip"
    with zipfile.ZipFile(archive_path, "w") as archive:
        archive.writestr("nested/first.txt", "first file")
        archive.writestr("second.txt", "second file")
    return archive_path


def test_extracts_files_to_destination_and_returns_their_paths(tmp_path):
    archive_path = create_archive(tmp_path)
    destination = tmp_path / "extracted"
    destination.mkdir()

    extracted_files = unzip_raw_data(archive_path, destination)

    assert extracted_files == [
        destination / "nested/first.txt",
        destination / "second.txt",
    ]
    assert extracted_files[0].read_text() == "first file"
    assert extracted_files[1].read_text() == "second file"


def test_defaults_destination_to_archive_parent(tmp_path):
    archive_path = create_archive(tmp_path)

    extracted_files = unzip_raw_data(archive_path)

    assert extracted_files == [
        tmp_path / "nested/first.txt",
        tmp_path / "second.txt",
    ]


def test_returns_empty_list_and_reports_missing_archive(tmp_path, capsys):
    missing_archive = tmp_path / "missing.zip"

    extracted_files = unzip_raw_data(missing_archive)

    assert extracted_files == []
    assert f"Path {missing_archive} does not exists!" in capsys.readouterr().out


def test_returns_empty_list_and_reports_missing_destination(tmp_path, capsys):
    archive_path = create_archive(tmp_path)
    missing_destination = tmp_path / "missing"

    extracted_files = unzip_raw_data(archive_path, missing_destination)

    assert extracted_files == []
    assert f"Path {missing_destination} does not exists!" in capsys.readouterr().out
