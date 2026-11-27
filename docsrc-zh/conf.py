project = "RK3588 Vision Deployment Kit"
author = "EdgeModelLab"
release = "1.0"

extensions = ["myst_parser"]
myst_enable_extensions = ["colon_fence"]
master_doc = "index"
exclude_patterns = ["_build"]

html_theme = "sphinx_rtd_theme"
html_title = "RK3588 Vision Deployment Kit"
html_theme_options = {
    "navigation_depth": 3,
    "collapse_navigation": False,
    "titles_only": False,
}
html_baseurl = "https://anguoyang.github.io/rk3588-vision-kit-sample/zh/"
language = "zh_CN"
