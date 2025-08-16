import requests

OUTPUT_URL = (
    "https://raw.githubusercontent.com/bigbio/quantms/HEAD/docs/output.md"
)


def download_file(url, save_path, timeout=20):
    """
    Download a file from a URL and save it to the specified path.

    Args:
        url (str): URL of the file to download
        save_path (str): Path where the downloaded file will be saved
        timeout (int): Timeout for the download request in seconds

    Returns:
        bool: True if download was successful, False otherwise
    """

    # Send GET request
    response = requests.get(url, stream=True, timeout=timeout)
    response.raise_for_status()  # Raise exception for HTTP errors

    # Write content to file
    with open(save_path, "wb") as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)

    print(f"Successfully downloaded: {url} to {save_path}")
    return True


def _md_to_rst(md_text: str) -> str:
    """Best-effort Markdown (GitHub) to simple reStructuredText conversion for Sphinx.

    This handles basic headings, links, code blocks, and a few internal anchors used in quantms_output.md.
    It is not a general-purpose converter but good enough for our generated page.
    """
    import re

    lines = md_text.splitlines()
    rst_lines = []
    in_code = False
    code_buffer = []

    def flush_code():
        nonlocal code_buffer
        if code_buffer:
            rst_lines.append(".. code-block:: text")
            rst_lines.append("")
            rst_lines.extend(["    " + l for l in code_buffer])
            rst_lines.append("")
            code_buffer = []

    for line in lines:
        # code fences
        if line.strip().startswith("```"):
            if not in_code:
                in_code = True
                continue
            else:
                in_code = False
                flush_code()
                continue
        if in_code:
            code_buffer.append(line)
            continue

        # convert headings ###, ##, # to rst
        m = re.match(r"^(#{1,6})\s+(.*)$", line)
        if m:
            level = len(m.group(1))
            title = m.group(2).strip()
            rst_lines.append(title)
            underline = "=" if level == 1 else ("-" if level in (2, 3) else "~")
            rst_lines.append(underline * len(title))
            rst_lines.append("")
            continue

        # transform internal anchors like (#consensusxml) to :ref:`consensusxml`
        line = re.sub(r"\]\(#([^)]+)\)", r"</:ref:`\1`>", line)

        # convert [text](url) to `text <url>`_
        line = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r"`\1 <\2>`_", line)

        # post-fix accidental patterns such as [Name</:ref:`anchor`>]
        line = re.sub(r"\[([^\]]+)</:ref:`([a-z0-9\-]+)`>", r":ref:`\2`", line)

        rst_lines.append(line)

    flush_code()
    # Ensure top title
    if rst_lines and not rst_lines[0].strip():
        rst_lines = rst_lines[1:]
    if rst_lines and not any(ch == "=" for ch in rst_lines[1:2]):
        title = "quantms outputs"
        rst_lines = [title, "=" * len(title), ""] + rst_lines
    return "\n".join(rst_lines)


def download_output(output_path="quantms_output.rst"):
    """
    Download the output file from the specified URL and save it locally to use
    for Sphinx documentation purposes.
    """
    # new folders would need to be created if necessary

    # Download the upstream Markdown file to a temporary location
    tmp_md = output_path if output_path.endswith(".md") else "quantms_output.md"
    assert download_file(OUTPUT_URL, tmp_md)  # prints success message

    with open(tmp_md, "r") as f:
        md_text = f.read()
    assert md_text.strip(), "Downloaded file is empty"

    # Convert to reStructuredText
    rst_text = _md_to_rst(md_text)

    # Write to .rst for Sphinx to pick up
    rst_path = output_path if output_path.endswith(".rst") else "quantms_output.rst"
    with open(rst_path, "w") as f:
        f.write(rst_text)

    # Remove temporary md file to avoid duplicate docnames
    try:
        if tmp_md != rst_path:
            import os
            os.remove(tmp_md)
    except OSError:
        pass


if __name__ == "__main__":
    download_output()
