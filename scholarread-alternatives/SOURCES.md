# Sources, revisions, and license review

Reviewed on 2026-10-31. Revisions are pinned to full Git commit identifiers so future updates can be audited rather than silently replacing the snapshot.

| Skill | Upstream | Reviewed revision | License evidence | Notes |
|---|---|---|---|---|
| `paper-reading` | [techdou/paper-reading](https://github.com/techdou/paper-reading) | `1271fbfbe84c6e69506f2c56c94599f0d6d427da` | Upstream `LICENSE` declares Apache-2.0; `NOTICE.md` is preserved | Includes local HTML validators and a loopback-first annotation bridge. Non-loopback binding requires a token. |
| `scholarly-deep-research` | [Tw6249/scholarly-deep-research](https://github.com/Tw6249/scholarly-deep-research) | `4a77b32c753a1a2789bfdb80e0a41ef74b709df9` | No `LICENSE`/`COPYING` file and no GitHub license declaration observed | Source is intentionally not copied into this repository. The descriptor pins the reviewed upstream revision for direct installation. Its scripts call scholarly APIs and may use optional API keys. |
| `academic-paper-review` | [bytedance/deer-flow](https://github.com/bytedance/deer-flow/tree/main/skills/public/academic-paper-review) | `eb5d1e1880f221051957f797d8119b075348fcb3` | Repository root `LICENSE` declares MIT | Only the public skill directory is copied; the repository license is included beside it. The skill is instruction-only. |
| `deep-paper-reading-skill` | [Zero-stargazer/deep-paper-reading-skill](https://github.com/Zero-stargazer/deep-paper-reading-skill) | `1a09e86235f4c64fa6b31a14c285e631ced923da` | Upstream `LICENSE` declares MIT | The installable skill directory is copied with its license. The skill is instruction-only. |

## Update policy

Before updating a snapshot:

1. Compare the old and new upstream revisions.
2. Recheck `SKILL.md`, scripts, network destinations, credential handling, and license metadata.
3. Preserve required license and notice files.
4. Update this ledger and rerun `tests/validate_bundle.py` plus relevant upstream tests.

Do not convert `scholarly-deep-research` into a redistributed snapshot unless its author adds a clear license or grants explicit permission.
