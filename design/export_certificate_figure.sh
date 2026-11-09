#!/usr/bin/env bash
set -euo pipefail
project_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
export_dir="$(mktemp -d /tmp/cortex-figure-export.XXXXXX)"
libreoffice "-env:UserInstallation=file://${export_dir}/libreoffice" --headless --convert-to pdf --outdir "$export_dir" "$project_root/design/certificate-pathway.pptx"
# Render the PowerPoint at 300 dpi, excluding its outer white margins.
pdftoppm -r 300 -x 165 -y 90 -W 4470 -H 2061 -singlefile -png "$export_dir/certificate-pathway.pdf" "$project_root/assets/images/certificate-pathway"
