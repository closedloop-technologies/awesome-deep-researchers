import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from scripts.validate_manifest import is_safe_relative_path, validate_manifest


def valid_manifest():
    return {
        "corpus_id": "demo",
        "research_question": "What does the private corpus say?",
        "allowed_sources": ["gdoc-1", "yt-1", "local-1", "s3-1", "arxiv-1"],
        "sources": [
            {
                "source_id": "gdoc-1",
                "source_type": "google_drive",
                "title": "Notes",
                "citation_anchor": "file ID plus heading",
                "file_id": "1abc",
                "web_url": "https://docs.google.com/document/d/1abc",
                "modified_time": "2026-06-23T00:00:00Z",
            },
            {
                "source_id": "yt-1",
                "source_type": "youtube",
                "title": "Interview",
                "citation_anchor": "video timestamp",
                "video_id": "abc123",
                "url": "https://www.youtube.com/watch?v=abc123",
                "published_at": "2026-01-01",
            },
            {
                "source_id": "local-1",
                "source_type": "local_file",
                "title": "Report",
                "citation_anchor": "path and page",
                "path": "docs/report.pdf",
                "sha256": "abc",
                "modified_time": "2026-01-01T00:00:00Z",
            },
            {
                "source_id": "s3-1",
                "source_type": "s3",
                "title": "Object",
                "citation_anchor": "bucket key and etag",
                "bucket": "bucket",
                "key": "prefix/object.json",
                "etag": "abc",
            },
            {
                "source_id": "arxiv-1",
                "source_type": "arxiv",
                "title": "Paper",
                "citation_anchor": "arXiv version and page",
                "arxiv_id": "2401.01234",
                "version": "v2",
                "pdf_url": "https://arxiv.org/pdf/2401.01234v2",
            },
        ],
    }


def test_valid_manifest_passes():
    assert validate_manifest(valid_manifest()) == []


def test_missing_citation_anchor_fails():
    manifest = valid_manifest()
    del manifest["sources"][0]["citation_anchor"]

    errors = validate_manifest(manifest)

    assert any("missing required field citation_anchor" in error for error in errors)


def test_unsupported_source_type_fails():
    manifest = valid_manifest()
    manifest["sources"][0]["source_type"] = "unsupported"

    errors = validate_manifest(manifest)

    assert any("unsupported source_type" in error for error in errors)


def test_safe_relative_path_rejects_absolute_and_dot_segments():
    assert is_safe_relative_path("docs/report.pdf") is True
    assert is_safe_relative_path("/docs/report.pdf") is False
    assert is_safe_relative_path("../report.pdf") is False
    assert is_safe_relative_path("docs/../report.pdf") is False
    assert is_safe_relative_path("./report.pdf") is False


def test_local_and_csv_paths_must_be_safe_relative_paths():
    manifest = valid_manifest()
    manifest["sources"][2]["path"] = "../private/report.pdf"
    manifest["sources"].append(
        {
            "source_id": "csv-1",
            "source_type": "csv",
            "title": "Rows",
            "citation_anchor": "row id",
            "path": "/tmp/export.csv",
            "sha256": "abc",
            "schema": {"id": "string"},
        }
    )

    errors = validate_manifest(manifest)

    assert any("local-1: path must be a safe relative path" in error for error in errors)
    assert any("csv-1: path must be a safe relative path" in error for error in errors)


def test_s3_key_must_be_safe_relative_path():
    manifest = valid_manifest()
    manifest["sources"][3]["key"] = "exports/../private.json"

    errors = validate_manifest(manifest)

    assert any("s3-1: key must be a safe relative path" in error for error in errors)
