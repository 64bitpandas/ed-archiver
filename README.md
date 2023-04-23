# Ed Archiver

A simple Python script to export Ed course discussions as JSON using the unofficial [edapi](https://github.com/smartspot2/edapi) package.


## Usage

**Requirements:** Python >=3.5

1. Run `pip install -r requirements.txt`.
2. Go to https://edstem.org/us/settings/api-tokens and generate an API token.
3. Save the API token to a `.env` file in this directory (see `.env.sample` for an example of formatting).
4. Run `python archive.py`
5. Enter the course ID to archive. This can be found in the URL. For example, the ID for `https://edstem.org/us/courses/23247/discussion/` would be `23247`.
6. All threads from that course will be saved to `out/COURSEID.json`.


