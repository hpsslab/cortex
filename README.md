# CoRTEX

Jekyll website for CoRTEX: Certificate of Experience on Semiconductor Training Readiness Through Experiential Learning at Colorado School of Mines, with related SMILE training tools.

Uses the [Minima 2.5 theme](https://github.com/jekyll/minima/tree/v2.5.2) (MIT), with local layout and style overrides. The restrained typography, navigation, and mobile layout are intended for an academic project site. Minima is installed as a gem; its upstream license remains in the dependency.

## Preview locally

Requires Ruby 3.2+ and Bundler.

```sh
bundle install
bundle exec jekyll serve
```

Open `http://localhost:4000/cortex/`. To preview at the domain root, use `bundle exec jekyll serve --baseurl ''`.

## Publish on GitHub Pages

1. Push these files to the `main` branch of `hpsslab/cortex`.
2. In repository **Settings → Pages**, choose **GitHub Actions** as the source.
3. The included workflow builds and deploys the site on pushes to `main`, or when run manually.

The expected URL is `https://hpsslab.github.io/cortex/`. If publishing from a different account or repository, update `url` and `baseurl` in `_config.yml`. The workflow obtains the build base path from GitHub Pages. A custom domain also requires updating `url` and the repository's Pages settings.

## Edit content

- `index.html`: overview
- `certificate.md`: requirements and application
- `smile.md`: tools and research
- `project.md`: scope and planned milestones
- `contact.md`: contacts
- `_config.yml`: identity and navigation
- `assets/css/site.scss`: visual overrides

The final editable pathway figure is in `design/certificate-pathway.pptx`. Rebuild it with `design/create_certificate_figure.py` (requires python-pptx). Photo sources and licenses are recorded in `design/source-images/README.md` and on the website’s photo credits page.

The favicon adapts the [Bootstrap Icons cpu-fill icon](https://icons.getbootstrap.com/icons/cpu-fill/) (v1.13.1), using CoRTEX navy and white. Its MIT license is retained in `assets/licenses/bootstrap-icons.txt`.

Program logos are in `assets/branding/`: `cortex-logo.svg` includes the full program name, `cortex-wordmark.svg` is the compact header version, and `cortex-logo.png` is a transparent PNG for slides and documents. The symbol combines a semiconductor chip with a three-stage learning path.
