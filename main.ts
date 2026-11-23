// Contest program for make.fun's news-image-20261122 — "Sum up
// 22 November's world news in one image". The picture itself lives in
// entry.png beside this file (rendered by draw22.py); this program's
// only job is to hand that exact file to the grader at
// /output/entry.png (or $MAKEFUN_OUTPUT_DIR when set).
// Node 22 standard library only. The grader runs it offline, twice,
// and both runs must produce identical bytes, so nothing is
// re-rendered here — the checked file is copied as-is.

import { copyFileSync, mkdirSync, readFileSync } from 'node:fs';
import { join } from 'node:path';

const PNG_MAGIC = Buffer.from([0x89, 0x50, 0x4e, 0x47, 0x0d, 0x0a, 0x1a, 0x0a]);
const IEND_TAIL = Buffer.from([
  0x00, 0x00, 0x00, 0x00, 0x49, 0x45, 0x4e, 0x44, 0xae, 0x42, 0x60, 0x82,
]);

function checkImage(bytes) {
  // The gate takes one whole PNG or JPEG, at most 1 MiB, at most
  // 1024 by 1024. Fail loudly here if the asset ever breaks a rule.
  if (bytes.length > 1_048_576) {
    throw new Error(`entry.png is ${bytes.length} bytes, over the 1 MiB limit`);
  }
  const isPng = bytes.subarray(0, 8).equals(PNG_MAGIC);
  const isJpeg =
    bytes[0] === 0xff &&
    bytes[1] === 0xd8 &&
    bytes[bytes.length - 2] === 0xff &&
    bytes[bytes.length - 1] === 0xd9;
  if (!isPng && !isJpeg) {
    throw new Error('entry.png is not a complete PNG or JPEG');
  }
  if (isPng) {
    const w = bytes.readUInt32BE(16);
    const h = bytes.readUInt32BE(20);
    if (w > 1024 || h > 1024) {
      throw new Error(`entry.png is ${w}x${h}, over the 1024x1024 limit`);
    }
    if (!bytes.subarray(bytes.length - 12).equals(IEND_TAIL)) {
      throw new Error('entry.png is missing its IEND chunk');
    }
  }
}

const here = new URL('./entry.png', import.meta.url);
const bytes = readFileSync(here);
checkImage(bytes);

const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';
mkdirSync(outDir, { recursive: true });
const dest = join(outDir, 'entry.png');
copyFileSync(here, dest);

// Read the copy back: the judge sees exactly these bytes, so prove
// the file that landed is the file that passed the checks above.
const landed = readFileSync(dest);
if (!landed.equals(bytes)) {
  throw new Error('the copied entry.png differs from the checked source');
}
console.log(`delivered entry.png (${bytes.length} bytes) to ${dest}`);
