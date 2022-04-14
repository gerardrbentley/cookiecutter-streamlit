from pathlib import Path
from datetime import date

license = Path.cwd() / 'LICENSE'
license_content = license.read_text()
current_year = str(date.today().year)

license.write_text(license_content.replace('LICENSE_YEAR', current_year))