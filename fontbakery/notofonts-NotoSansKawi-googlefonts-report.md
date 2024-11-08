## FontBakery report

fontbakery version: 0.12.10





## Check results



<details><summary>[10] NotoSansKawi[wght].ttf</summary>
<div>
<details>
    <summary>🔥 <b>FAIL</b> Does the font have any invalid script tags? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.layout.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>The following invalid script tags were found in the font: kawi</p>
 [code: bad-script-tags]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Check for presence of an ARTICLE.en_us.html file <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.description.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>This is a Noto font but it lacks an ARTICLE.en_us.html file.</p>
 [code: missing-article]



* 🔥 **FAIL** <p>This is a Noto font but it lacks a DESCRIPTION.en_us.html file.</p>
 [code: missing-description]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Check that texts shape as per expectation <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/shaping.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>qa/shaping_tests/example.json: Expected and actual shaping not matching</p>
<ul>
<li>
<p>Shaping did not match: ๰</p>
<pre><code>Expected: None
Got     : .notdef=0+500
</code></pre>
<p>Got: <svg style="height:100px;margin:10px;" xmlns="http://www.w3.org/2000/svg" viewBox="0 -900 500 2000" transform="matrix(1 0 0 -1 0 0)"> <defs> <path id="g0" d="M50.0,-200.0L50.0,800.0L450.0,800.0L450.0,-200.0L50.0,-200.0ZM100.0,-150.0L400.0,-150.0L400.0,750.0L100.0,750.0L100.0,-150.0Z"/> </defs> <g transform="translate(0,0)"> <use href="#g0"/> </g> </svg></p>
</li>
</ul>
 [code: shaping-regression]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check GDEF mark glyph class doesn't have characters that are not marks. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.gdef.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following non-mark characters should not be in the GDEF mark glyph class:
U+11F02</p>
 [code: non-mark-chars]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Validate size, and resolution of article images, and ensure article page has minimum length and includes visual assets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.article.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>Family metadata at fonts/NotoSansKawi/googlefonts/variable-ttf does not have an article.</p>
 [code: lacks-article]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check for codepoints not covered by METADATA subsets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.subsets.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following codepoints supported by the font are not covered by
any subsets defined in the font's metadata file, and will never
be served. You can solve this by either manually adding additional
subset declarations to METADATA.pb, or by editing the glyphset
definitions.</p>
<ul>
<li>U+02D8 BREVE: try adding one of: yi, canadian-aboriginal</li>
<li>U+02D9 DOT ABOVE: try adding one of: yi, canadian-aboriginal</li>
<li>U+02DB OGONEK: try adding one of: yi, canadian-aboriginal</li>
<li>U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: coptic, cherokee, tifinagh, math</li>
<li>U+0306 COMBINING BREVE: try adding one of: old-permic, tifinagh</li>
<li>U+0307 COMBINING DOT ABOVE: try adding one of: malayalam, syriac, tai-le, hebrew, old-permic, tifinagh, todhri, canadian-aboriginal, coptic, duployan, math</li>
<li>U+030A COMBINING RING ABOVE: try adding one of: duployan, syriac</li>
<li>U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: cherokee, osage</li>
<li>U+030C COMBINING CARON: try adding one of: tai-le, cherokee</li>
<li>U+0326 COMBINING COMMA BELOW: try adding math</li>
<li>U+0327 COMBINING CEDILLA: try adding math</li>
<li>U+0328 COMBINING OGONEK: not included in any glyphset definition</li>
<li>U+25CC DOTTED CIRCLE: try adding one of: warang-citi, khmer, grantha, sharada, bengali, mende-kikakui, buginese, cham, new-tai-lue, tai-le, miao, adlam, gurmukhi, yi, limbu, chakma, syriac, dogra, khudawadi, meetei-mayek, math, psalter-pahlavi, elbasan, osage, modi, tibetan, tagalog, phags-pa, hanunoo, devanagari, myanmar, ahom, gujarati, takri, tagbanwa, soyombo, mahajani, marchen, nko, mongolian, tirhuta, hebrew, batak, masaram-gondi, pahawh-hmong, coptic, wancho, malayalam, manichaean, kaithi, music, zanabazar-square, symbols, newa, oriya, tai-tham, duployan, javanese, lao, bhaiksuki, gunjala-gondi, old-permic, canadian-aboriginal, tai-viet, balinese, syloti-nagri, siddham, sinhala, telugu, thaana, brahmi, armenian, caucasian-albanian, lepcha, khojki, hanifi-rohingya, kannada, tamil, thai, kayah-li, mandaic, sundanese, saurashtra, rejang, buhid, bassa-vah, kharoshthi, tifinagh, sogdian</li>
</ul>
<p>Or you can add the above codepoints to one of the subsets supported by the font: <code>kawi</code>, <code>latin</code>, <code>latin-ext</code></p>
 [code: unreachable-subsetting]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/shaping.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The dot of soft dotted characters used in orthographies <em>must</em> disappear in the following strings: į̀ į́ į̂ į̃ į̄ į̌</p>
<p>The dot of soft dotted characters <em>should</em> disappear in other cases, for example: į̆ į̇ į̈ į̊ į̋ į̦̀ į̦́ į̦̂ į̦̃ į̦̄ į̦̆ į̦̇ į̦̈ į̦̊ į̦̋ į̦̌ į̧̀ į̧́ į̧̂ į̧̃</p>
<p>Your font fully covers the following languages that require the soft-dotted feature: Dutch (Latn, 31,709,104 speakers), Lithuanian (Latn, 2,357,094 speakers).</p>
<p>Your font does <em>not</em> cover the following languages that require the soft-dotted feature: Ngbaka (Latn, 1,020,000 speakers), Ukrainian (Cyrl, 29,273,587 speakers), Ebira (Latn, 2,200,000 speakers), Belarusian (Cyrl, 10,064,517 speakers), Koonzime (Latn, 40,000 speakers), Mango (Latn, 77,000 speakers), Makaa (Latn, 221,000 speakers), Heiltsuk (Latn, 300 speakers), Aghem (Latn, 38,843 speakers), Lugbara (Latn, 2,200,000 speakers), Mfumte (Latn, 79,000 speakers), Nzakara (Latn, 50,000 speakers), Nateni (Latn, 100,000 speakers), Bafut (Latn, 158,146 speakers), Kaska (Latn, 125 speakers), Zapotec (Latn, 490,000 speakers), Ejagham (Latn, 120,000 speakers), Fur (Latn, 1,230,163 speakers), Ma’di (Latn, 584,000 speakers), Yala (Latn, 200,000 speakers), Bete-Bendi (Latn, 100,000 speakers), Dii (Latn, 71,000 speakers), Gulay (Latn, 250,478 speakers), Southern Kisi (Latn, 360,000 speakers), Dan (Latn, 1,099,244 speakers), Igbo (Latn, 27,823,640 speakers), Sar (Latn, 500,000 speakers), Avokaya (Latn, 100,000 speakers), Ijo, Southeast (Latn, 2,471,000 speakers), Kom (Latn, 360,685 speakers), Ekpeye (Latn, 226,000 speakers), Mundani (Latn, 34,000 speakers), Teke-Ebo (Latn, 260,000 speakers), Kpelle, Guinea (Latn, 622,000 speakers), South Central Banda (Latn, 244,000 speakers), Vute (Latn, 21,000 speakers), Cicipu (Latn, 44,000 speakers), Han (Latn, 6 speakers), Basaa (Latn, 332,940 speakers), Navajo (Latn, 166,319 speakers).</p>
 [code: soft-dotted]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Are there any misaligned on-curve points? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/outline.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs have on-curve points which have potentially incorrect y coordinates:</p>
<pre><code>* dakawi (U+11F23): X=562.0,Y=2.0 (should be at baseline 0?)

* repha_vowelAakawi.alt: X=-279.0,Y=699.0 (should be at cap-height 700?)

* visargakawi (U+11F03): X=159.0,Y=1.0 (should be at baseline 0?)

* visargakawi (U+11F03): X=159.0,Y=1.0 (should be at baseline 0?)

* sixkawi (U+11F56): X=312.0,Y=-1.0 (should be at baseline 0?)

* uni25CC (U+25CC): X=305.0,Y=-1.0 (should be at baseline 0?)

* uni25CC (U+25CC): X=373.0,Y=-1.0 (should be at baseline 0?)

* vowelI_candrabindukawi: X=98.0,Y=1101.0 (should be at ascender 1100?)

* vowelI_candrabindukawi: X=428.5,Y=1101.0 (should be at ascender 1100?)

* vowelIi_candrabindukawi: X=98.0,Y=1101.0 (should be at ascender 1100?)

* vowelIi_candrabindukawi: X=428.5,Y=1101.0 (should be at ascender 1100?)

* vowelAikawi (U+11F3F): X=127.0,Y=700.5 (should be at cap-height 700?)

* vowelAikawi (U+11F3F): X=301.0,Y=699.0 (should be at cap-height 700?)

* G (U+0047): X=537.0,Y=-1.0 (should be at baseline 0?)

* Gbreve (U+011E): X=537.0,Y=-1.0 (should be at baseline 0?)

* uni0122 (U+0122): X=537.0,Y=-1.0 (should be at baseline 0?)

* Gdotaccent (U+0120): X=537.0,Y=-1.0 (should be at baseline 0?)

* uni1E9E (U+1E9E): X=326.5,Y=-1.5 (should be at baseline 0?)

* S (U+0053): X=136.0,Y=-1.0 (should be at baseline 0?)

* S (U+0053): X=169.5,Y=702.0 (should be at cap-height 700?)

* Sacute (U+015A): X=136.0,Y=-1.0 (should be at baseline 0?)

* Sacute (U+015A): X=169.5,Y=702.0 (should be at cap-height 700?)

* Scaron (U+0160): X=136.0,Y=-1.0 (should be at baseline 0?)

* Scaron (U+0160): X=169.5,Y=702.0 (should be at cap-height 700?)

* Scedilla (U+015E): X=136.0,Y=-1.0 (should be at baseline 0?)

* Scedilla (U+015E): X=169.5,Y=702.0 (should be at cap-height 700?)

* uni0218 (U+0218): X=136.0,Y=-1.0 (should be at baseline 0?)

* uni0218 (U+0218): X=169.5,Y=702.0 (should be at cap-height 700?)

* Uogonek (U+0172): X=449.0,Y=1.0 (should be at baseline 0?)

* a (U+0061): X=433.0,Y=502.0 (should be at x-height 500?)

* a (U+0061): X=105.0,Y=499.0 (should be at x-height 500?)

* ae (U+00E6): X=710.5,Y=-1.5 (should be at baseline 0?)

* atilde (U+00E3): X=132.5,Y=699.5 (should be at cap-height 700?)

* braceleft (U+007B): X=150.0,Y=1.0 (should be at baseline 0?)

* colon (U+003A): X=177.5,Y=2.0 (should be at baseline 0?)

* colon (U+003A): X=90.0,Y=2.0 (should be at baseline 0?)

* e (U+0065): X=408.0,Y=-1.5 (should be at baseline 0?)

* eacute (U+00E9): X=408.0,Y=-1.5 (should be at baseline 0?)

* ecaron (U+011B): X=408.0,Y=-1.5 (should be at baseline 0?)

* ecircumflex (U+00EA): X=408.0,Y=-1.5 (should be at baseline 0?)

* edieresis (U+00EB): X=408.0,Y=-1.5 (should be at baseline 0?)

* edotaccent (U+0117): X=408.0,Y=-1.5 (should be at baseline 0?)

* egrave (U+00E8): X=408.0,Y=-1.5 (should be at baseline 0?)

* ellipsis (U+2026): X=177.5,Y=2.0 (should be at baseline 0?)

* ellipsis (U+2026): X=90.0,Y=2.0 (should be at baseline 0?)

* ellipsis (U+2026): X=439.5,Y=2.0 (should be at baseline 0?)

* ellipsis (U+2026): X=352.0,Y=2.0 (should be at baseline 0?)

* ellipsis (U+2026): X=700.5,Y=2.0 (should be at baseline 0?)

* ellipsis (U+2026): X=613.0,Y=2.0 (should be at baseline 0?)

* emacron (U+0113): X=408.0,Y=-1.5 (should be at baseline 0?)

* eogonek (U+0119): X=408.0,Y=-1.5 (should be at baseline 0?)

* Euro (U+20AC): X=468.5,Y=-0.5 (should be at baseline 0?)

* exclam (U+0021): X=177.5,Y=2.0 (should be at baseline 0?)

* exclam (U+0021): X=90.0,Y=2.0 (should be at baseline 0?)

* germandbls (U+00DF): X=317.0,Y=-1.0 (should be at baseline 0?)

* h (U+0068): X=488.0,Y=498.5 (should be at x-height 500?)

* m (U+006D): X=809.0,Y=499.5 (should be at x-height 500?)

* n (U+006E): X=488.0,Y=499.5 (should be at x-height 500?)

* ntilde (U+00F1): X=160.5,Y=699.5 (should be at cap-height 700?)

* oe (U+0153): X=791.0,Y=-1.5 (should be at baseline 0?)

* otilde (U+00F5): X=154.5,Y=699.5 (should be at cap-height 700?)

* period (U+002E): X=177.5,Y=2.0 (should be at baseline 0?)

* period (U+002E): X=90.0,Y=2.0 (should be at baseline 0?)

* question (U+003F): X=222.0,Y=2.0 (should be at baseline 0?)

* question (U+003F): X=134.5,Y=2.0 (should be at baseline 0?)

* s (U+0073): X=123.5,Y=-1.0 (should be at baseline 0?)

* sacute (U+015B): X=123.5,Y=-1.0 (should be at baseline 0?)

* scaron (U+0161): X=123.5,Y=-1.0 (should be at baseline 0?)

* scedilla (U+015F): X=123.5,Y=-1.0 (should be at baseline 0?)

* uni0219 (U+0219): X=123.5,Y=-1.0 (should be at baseline 0?)

* three (U+0033): X=137.0,Y=-1.5 (should be at baseline 0?)

* three (U+0033): X=143.5,Y=702.0 (should be at cap-height 700?)

* tilde (U+02DC): X=74.5,Y=699.5 (should be at cap-height 700?)

* tildecomb (U+0303): X=-456.5,Y=699.5 (should be at cap-height 700?)

* two (U+0032): X=152.5,Y=699.5 (should be at cap-height 700?)

* w (U+0077): X=258.0,Y=1.0 (should be at baseline 0?)

* w (U+0077): X=158.0,Y=1.0 (should be at baseline 0?)

* w (U+0077): X=626.0,Y=1.0 (should be at baseline 0?)

* w (U+0077): X=523.0,Y=1.0 (should be at baseline 0?)

* wacute (U+1E83): X=258.0,Y=1.0 (should be at baseline 0?)

* wacute (U+1E83): X=158.0,Y=1.0 (should be at baseline 0?)

* wacute (U+1E83): X=626.0,Y=1.0 (should be at baseline 0?)

* wacute (U+1E83): X=523.0,Y=1.0 (should be at baseline 0?)

* wcircumflex (U+0175): X=258.0,Y=1.0 (should be at baseline 0?)

* wcircumflex (U+0175): X=158.0,Y=1.0 (should be at baseline 0?)

* wcircumflex (U+0175): X=626.0,Y=1.0 (should be at baseline 0?)

* wcircumflex (U+0175): X=523.0,Y=1.0 (should be at baseline 0?)

* wdieresis (U+1E85): X=258.0,Y=1.0 (should be at baseline 0?)

* wdieresis (U+1E85): X=158.0,Y=1.0 (should be at baseline 0?)

* wdieresis (U+1E85): X=626.0,Y=1.0 (should be at baseline 0?)

* wdieresis (U+1E85): X=523.0,Y=1.0 (should be at baseline 0?)

* wgrave (U+1E81): X=258.0,Y=1.0 (should be at baseline 0?)

* wgrave (U+1E81): X=158.0,Y=1.0 (should be at baseline 0?)

* wgrave (U+1E81): X=626.0,Y=1.0 (should be at baseline 0?)

* wgrave (U+1E81): X=523.0,Y=1.0 (should be at baseline 0?)

* y (U+0079): X=217.0,Y=-2.0 (should be at baseline 0?)

* yacute (U+00FD): X=217.0,Y=-2.0 (should be at baseline 0?)

* ycircumflex (U+0177): X=217.0,Y=-2.0 (should be at baseline 0?)

* ydieresis (U+00FF): X=217.0,Y=-2.0 (should be at baseline 0?)

* ygrave (U+1EF3): X=217.0,Y=-2.0 (should be at baseline 0?)
</code></pre>
 [code: found-misalignments]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure variable fonts include an avar table. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.varfont.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>This variable font does not have an avar table.</p>
 [code: missing-avar]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.meta.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>This font file does not have a 'meta' table.</p>
 [code: lacks-meta-table]



</div>
</details>
</div>
</details>




### Summary

| 💥 ERROR | ☠ FATAL | 🔥 FAIL | ⚠️ WARN | ⏩ SKIP | ℹ️ INFO | ✅ PASS | 🔎 DEBUG | 
| ---|---|---|---|---|---|---|---|
| 0 | 0 | 3 | 7 | 96 | 7 | 138 | 0 | 
| 0% | 0% | 1% | 3% | 38% | 3% | 55% | 0% | 



**Note:** The following loglevels were omitted in this report:


* SKIP
* INFO
* PASS
* DEBUG
