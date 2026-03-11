# Bailian Model Studio Skill Expansion Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Add the first batch of newly released Bailian Model Studio skills that are missing from this repository.

**Architecture:** Add new skill folders under `skills/ai/**` using existing Model Studio patterns: `SKILL.md`, optional lightweight helper script, `references/sources.md`, `agents/openai.yaml`, and a mirrored smoke-test skill under `tests/ai/**`. Update the Model Studio entry skill and existing skill model lists, then regenerate README skill indexes from frontmatter.

**Tech Stack:** Markdown skills, Python helper scripts, repository README index generator

---

### Task 1: Add missing audio and multimodal skills

**Files:**
- Create: `skills/ai/audio/alicloud-ai-audio-asr-realtime/**`
- Create: `skills/ai/audio/alicloud-ai-audio-livetranslate/**`
- Create: `skills/ai/multimodal/alicloud-ai-multimodal-qwen-omni/**`
- Create: `skills/ai/multimodal/alicloud-ai-multimodal-qvq/**`
- Create: `tests/ai/audio/alicloud-ai-audio-asr-realtime-test/SKILL.md`
- Create: `tests/ai/audio/alicloud-ai-audio-livetranslate-test/SKILL.md`
- Create: `tests/ai/multimodal/alicloud-ai-multimodal-qwen-omni-test/SKILL.md`
- Create: `tests/ai/multimodal/alicloud-ai-multimodal-qvq-test/SKILL.md`

**Step 1: Write the failing test**

Add the new smoke-test skill documents first so repository coverage reflects the missing capability before the implementation files exist.

**Step 2: Run test to verify it fails**

Run: `find tests/ai -maxdepth 3 -name SKILL.md | rg 'asr-realtime|livetranslate|qwen-omni|qvq'`

Expected: no matches before file creation.

**Step 3: Write minimal implementation**

Add the new skill directories with:
- clear frontmatter
- exact model names
- minimal validation command
- one helper script that prepares a request payload

**Step 4: Run test to verify it passes**

Run: `find tests/ai -maxdepth 3 -name SKILL.md | rg 'asr-realtime|livetranslate|qwen-omni|qvq'`

Expected: new test skills are listed.

### Task 2: Add missing embedding, rerank, and video edit skills

**Files:**
- Create: `skills/ai/search/alicloud-ai-search-text-embedding/**`
- Create: `skills/ai/search/alicloud-ai-search-rerank/**`
- Create: `skills/ai/video/alicloud-ai-video-wan-edit/**`
- Create: `tests/ai/search/alicloud-ai-search-text-embedding-test/SKILL.md`
- Create: `tests/ai/search/alicloud-ai-search-rerank-test/SKILL.md`
- Create: `tests/ai/video/alicloud-ai-video-wan-edit-test/SKILL.md`

**Step 1: Write the failing test**

Add the mirrored smoke-test skill files first.

**Step 2: Run test to verify it fails**

Run: `find tests/ai -maxdepth 3 -name SKILL.md | rg 'text-embedding|rerank|wan-edit'`

Expected: no matches before file creation.

**Step 3: Write minimal implementation**

Add the skill files and helper scripts with pinned recommended model lists.

**Step 4: Run test to verify it passes**

Run: `find tests/ai -maxdepth 3 -name SKILL.md | rg 'text-embedding|rerank|wan-edit'`

Expected: new test skills are listed.

### Task 3: Update existing routing and model coverage

**Files:**
- Modify: `skills/ai/entry/alicloud-ai-entry-modelstudio/SKILL.md`
- Modify: `skills/ai/image/alicloud-ai-image-qwen-image/SKILL.md`
- Modify: `skills/ai/image/alicloud-ai-image-qwen-image-edit/SKILL.md`
- Modify: `skills/ai/multimodal/alicloud-ai-multimodal-qwen-vl/SKILL.md`
- Modify: `skills/ai/video/alicloud-ai-video-wan-video/SKILL.md`

**Step 1: Write the failing test**

Use repository grep as the failing check.

**Step 2: Run test to verify it fails**

Run: `rg -n 'qwen-image-2.0|qwen-vl-ocr|wan2.2-t2v|asr-realtime|livetranslate|omni|qvq|embedding|rerank|wan-edit' skills/ai/entry skills/ai/image skills/ai/multimodal skills/ai/video`

Expected: several intended additions are absent before edits.

**Step 3: Write minimal implementation**

Update the routing table, common missing capability notes, and model lists.

**Step 4: Run test to verify it passes**

Run the same `rg` command and confirm the new references exist.

### Task 4: Regenerate indexes and verify

**Files:**
- Modify: `README.md`
- Modify: `README.zh-CN.md`
- Modify: `README.zh-TW.md`

**Step 1: Run generation**

Run: `python3 scripts/generate_skill_index.py`

**Step 2: Verify generated docs and scripts**

Run:

```bash
for f in \
  skills/ai/audio/alicloud-ai-audio-asr-realtime/scripts/*.py \
  skills/ai/audio/alicloud-ai-audio-livetranslate/scripts/*.py \
  skills/ai/multimodal/alicloud-ai-multimodal-qwen-omni/scripts/*.py \
  skills/ai/multimodal/alicloud-ai-multimodal-qvq/scripts/*.py \
  skills/ai/search/alicloud-ai-search-text-embedding/scripts/*.py \
  skills/ai/search/alicloud-ai-search-rerank/scripts/*.py \
  skills/ai/video/alicloud-ai-video-wan-edit/scripts/*.py; do
    python3 -m py_compile "$f"
done
```

Expected: exit 0.
