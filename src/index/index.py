import pathlib

import jinja2
from awesome_panel_extensions.site.gallery import GalleryTemplate
from awesome_panel_extensions.site.gallery.gallery_template import TEMPLATE
from awesome_panel_extensions.site.models import Application

# Todo: Carve out GalleryTemplate to a panel-gallery package

ROOT = pathlib.Path(__file__).parent
TARGET = ROOT.parent.parent/"docs"/"index.html"
APPLICATIONS = Application.read(ROOT/ "index.yaml")
FAVICON = "https://raw.githubusercontent.com/MarcSkovMadsen/awesome-panel-assets/320297ccb92773da099f6b97d267cc0433b67c23/favicon/ap-1f77b4.ico"

index_html = GalleryTemplate(
        site="Panel",
        site_url="https://awesome-panel.org",
        title="Webassembly Apps",
        description="""  """,
        applications=APPLICATIONS,
        target="_self",
        theme="default",
        meta_name="Awesome Panel Examples",
        meta_description="   ",
        meta_keywords=(
            "Awesome, HoloViz, Panel, Gallery, Apps, Science, Data Engineering, Data Science, "
            "Machine Learning, Python"
        ),
        meta_author="Jerome Schätzle",
        accent_base_color="#1f77b4",
        favicon=FAVICON,
)

TEMPLATE = TEMPLATE.replace("{{ plot_script | indent(8) }}","")


if __name__=="__main__":
    environment = jinja2.Environment()
    template = environment.from_string(TEMPLATE)
    index_html = template.render(**index_html._render_variables)
    TARGET.write_text(index_html)
if __name__.startswith("bokeh"):
    index_html.servable()
