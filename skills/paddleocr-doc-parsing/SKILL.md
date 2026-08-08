---
name: paddleocr-doc-parsing
description: >-
  Use this skill to extract structured Markdown/JSON from PDFs and document images—tables with
  cell-level precision, formulas as LaTeX, figures, seals, charts, headers/footers, multi-column
  layout and correct reading order.
  Trigger terms: 文档解析, 版面分析, 版面还原, 表格提取, 公式识别, 多栏排版, 扫描件结构化,
  发票, 财报, 复杂 PDF, PDF转Markdown, 图表, 阅读顺序; reading order, formula, LaTeX,
  layout parsing, structure extraction, PP-StructureV3, PaddleOCR-VL.
---

# PaddleOCR Document Parsing

Before processing unpublished manuscripts, read [references/provenance-and-privacy.md](references/provenance-and-privacy.md).

## When to Use This Skill

**Use this skill for**:

- Documents with tables (invoices, financial reports, spreadsheets)
- Documents with mathematical formulas (academic papers, scientific documents)
- Documents with charts and diagrams
- Multi-column layouts (newspapers, magazines, brochures)
- Complex document structures requiring layout analysis

## Usage

### Basic Document Parsing

From URL:

```bash
paddleocr api \
  --model_type doc_parsing \
  --file_url "https://example.com/report.pdf"
```

From local file:

```bash
paddleocr api \
  --model_type doc_parsing \
  --file_path "./document.pdf"
```

### Common Options

```bash
# With specific model
paddleocr api \
  --model_type doc_parsing \
  --model PP-StructureV3 \
  --file_path "./report.pdf"

# Disable preprocessing (faster, for flat/well-oriented images)
paddleocr api \
  --model_type doc_parsing \
  --file_path "./document.pdf" \
  --use_doc_unwarping False \
  --use_doc_orientation_classify False

# With page ranges
paddleocr api \
  --model_type doc_parsing \
  --file_path "./large.pdf" \
  --page_ranges "1-5,10,15-20"

# Save result and resources
paddleocr api \
  --model_type doc_parsing \
  --file_url "https://..." \
  --output result.json \
  --save_resources ./resources

# Prettify markdown output
paddleocr api \
  --model_type doc_parsing \
  --file_path "./document.pdf" \
  --prettify_markdown True
```

### Output Format

```json
{
  "jobId": "job-xxx",
  "pages": [
    {
      "markdownText": "# Title\n\nContent...",
      "markdownImages": {"img1": "https://..."},
      "outputImages": {"layout1": "https://..."}
    }
  ]
}
```

## Important Notes

Keep preprocessing enabled when the document is curved, distorted, or rotated.

Display complete results unless content exceeds 10,000 characters. Report authentication, quota,
and no-content errors explicitly instead of silently falling back.

Run `paddleocr api --help` for the CLI reference. Full documentation:
https://www.paddleocr.ai/latest/en/version3.x/inference_deployment/serving/paddleocr_official_api/cli.html
