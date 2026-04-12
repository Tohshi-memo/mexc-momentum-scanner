# Filter Granularity Experiment Report

- source: `data/experiments.json`
- closed shadow trades: **5**

シャドウトレードは『現行 STRICT フィルターを通ったか否かに関わらず』
全ての急騰候補を仮想エントリーとして追跡している。各レコードは
検出時のフィルター値スナップショットを持つため、後から任意の閾値で
再評価できる。Claude (次回セッション) は本レポートと
`data/experiments.json` を読み、フィルターの粒度をチューニングできる。

---

**凡例**: W/L/E = TP_HIT / SL_HIT / EXPIRED. 
expectancy = 1トレードあたりの平均 PnL (%)。
ショート視点なので **+ が利益**, **- が損失** であることに注意。

---

## 1. Baseline

| group | n | W/L/E | win% | avg win | avg loss | expectancy | total PnL | median hold |
|-------|---|-------|------|---------|----------|------------|-----------|-------------|
| ALL candidates | 5 | 2/3/0 | 40.0% | +8.30% | -4.00% | +0.92% | +4.6% | 0.4h |
| STRICT (current) | 0 | – | – | – | – | – | – | – |
| REJECTED by STRICT | 5 | 2/3/0 | 40.0% | +8.30% | -4.00% | +0.92% | +4.6% | 0.4h |

**読み方**: STRICT が REJECTED より expectancy が高ければ現フィルターは有効。REJECTED の方が良ければフィルターを緩めるべき。

---

## 2. RSI(1h) threshold sweep

現行 STRICT は RSI ≥ 75。閾値を変えた場合の仮想成績。

| group | n | W/L/E | win% | avg win | avg loss | expectancy | total PnL | median hold |
|-------|---|-------|------|---------|----------|------------|-----------|-------------|
| RSI ≥ 60 | 4 | 1/3/0 | 25.0% | +8.54% | -4.00% | -0.86% | -3.5% | 0.4h |
| RSI ≥ 65 | 4 | 1/3/0 | 25.0% | +8.54% | -4.00% | -0.86% | -3.5% | 0.4h |
| RSI ≥ 70 | 4 | 1/3/0 | 25.0% | +8.54% | -4.00% | -0.86% | -3.5% | 0.4h |
| RSI ≥ 75 | 2 | 1/1/0 | 50.0% | +8.54% | -4.00% | +2.27% | +4.5% | 0.4h |
| RSI ≥ 80 | 1 | 0/1/0 | 0.0% | +0.00% | -4.00% | -4.00% | -4.0% | 0.4h |


---

## 3. RSI(4h) maximum sweep

現行 STRICT は 4h RSI < 70。低いほど厳しい (既存トレンドを除外)。
OFF = 4h フィルター無効。

| group | n | W/L/E | win% | avg win | avg loss | expectancy | total PnL | median hold |
|-------|---|-------|------|---------|----------|------------|-----------|-------------|
| 4h RSI < 60 | 0 | – | – | – | – | – | – | – |
| 4h RSI < 65 | 0 | – | – | – | – | – | – | – |
| 4h RSI < 70 | 1 | 1/0/0 | 100.0% | +8.06% | +0.00% | +8.06% | +8.1% | 0.6h |
| 4h RSI < 75 | 1 | 1/0/0 | 100.0% | +8.06% | +0.00% | +8.06% | +8.1% | 0.6h |
| OFF (no 4h filter) | 5 | 2/3/0 | 40.0% | +8.30% | -4.00% | +0.92% | +4.6% | 0.4h |


---

## 4. BB upper break requirement

現行 STRICT は price > BB upper(2σ) 必須。

| group | n | W/L/E | win% | avg win | avg loss | expectancy | total PnL | median hold |
|-------|---|-------|------|---------|----------|------------|-----------|-------------|
| BB break required | 0 | – | – | – | – | – | – | – |
| BB break NOT required (all) | 5 | 2/3/0 | 40.0% | +8.30% | -4.00% | +0.92% | +4.6% | 0.4h |
| BB no-break only | 5 | 2/3/0 | 40.0% | +8.30% | -4.00% | +0.92% | +4.6% | 0.4h |


---

## 5. Volume trend filter

現行 STRICT は『RISING を除外』(疲弊兆候のみショート)。

| group | n | W/L/E | win% | avg win | avg loss | expectancy | total PnL | median hold |
|-------|---|-------|------|---------|----------|------------|-----------|-------------|
| ALL volume trends | 5 | 2/3/0 | 40.0% | +8.30% | -4.00% | +0.92% | +4.6% | 0.4h |
| NOT RISING (current) | 5 | 2/3/0 | 40.0% | +8.30% | -4.00% | +0.92% | +4.6% | 0.4h |
| DECLINING only (strictest) | 5 | 2/3/0 | 40.0% | +8.30% | -4.00% | +0.92% | +4.6% | 0.4h |
| FLAT only | 0 | – | – | – | – | – | – | – |
| RISING only | 0 | – | – | – | – | – | – | – |


---

## 6. Relative strength (vs BTC) threshold sweep

現行スキャナーは alt_1h - btc_1h ≥ 5.0% でフィルター。
閾値を変えた場合の仮想成績。

| group | n | W/L/E | win% | avg win | avg loss | expectancy | total PnL | median hold |
|-------|---|-------|------|---------|----------|------------|-----------|-------------|
| rel strength ≥ 0% | 5 | 2/3/0 | 40.0% | +8.30% | -4.00% | +0.92% | +4.6% | 0.4h |
| rel strength ≥ 3% | 5 | 2/3/0 | 40.0% | +8.30% | -4.00% | +0.92% | +4.6% | 0.4h |
| rel strength ≥ 5% | 5 | 2/3/0 | 40.0% | +8.30% | -4.00% | +0.92% | +4.6% | 0.4h |
| rel strength ≥ 7% | 4 | 2/2/0 | 50.0% | +8.30% | -4.00% | +2.15% | +8.6% | 0.5h |
| rel strength ≥ 10% | 1 | 1/0/0 | 100.0% | +8.54% | +0.00% | +8.54% | +8.5% | 0.4h |


---

## 7. Market regime breakdown

BTC 1h change によるレジーム別の成績。

| group | n | W/L/E | win% | avg win | avg loss | expectancy | total PnL | median hold |
|-------|---|-------|------|---------|----------|------------|-----------|-------------|
| BEARISH | 2 | 1/1/0 | 50.0% | +8.06% | -4.00% | +2.03% | +4.1% | 0.5h |
| STAGNANT | 2 | 1/1/0 | 50.0% | +8.54% | -4.00% | +2.27% | +4.5% | 0.5h |
| BULLISH | 1 | 0/1/0 | 0.0% | +0.00% | -4.00% | -4.00% | -4.0% | 0.3h |


---

## 8. Combined filters

代表的なフィルターの組み合わせの仮想成績。

| group | n | W/L/E | win% | avg win | avg loss | expectancy | total PnL | median hold |
|-------|---|-------|------|---------|----------|------------|-----------|-------------|
| STRICT (RSI≥75 & 4h<70 & ¬RISING) | 0 | – | – | – | – | – | – | – |
| RSI≥70 & 4h<70 & ¬RISING | 0 | – | – | – | – | – | – | – |
| RSI≥70 & 4h<75 & ¬RISING | 0 | – | – | – | – | – | – | – |
| RSI≥70 & ¬RISING (no 4h) | 4 | 1/3/0 | 25.0% | +8.54% | -4.00% | -0.86% | -3.5% | 0.4h |
| RSI≥65 & 4h<70 & DECLINING | 0 | – | – | – | – | – | – | – |


---

## 9. Indicator distribution: winners vs losers

TP_HIT と SL_HIT の指標平均。乖離が大きい指標が予測力を持つ可能性あり。

| indicator | wins (avg) | losses (avg) | delta |
|-----------|------------|--------------|-------|
| RSI(1h) | +68.76 | +77.34 | -8.58 |
| RSI(4h) | +80.33 | +85.52 | -5.19 |
| price/BB upper | +0.93 | +0.91 | +0.02 |
| volume ratio | +0.59 | +0.49 | +0.10 |
| ATR% | +7.33 | +7.33 | +0.00 |
| change_1h | +10.67 | +6.14 | +4.53 |
| rel strength | +11.79 | +6.61 | +5.18 |
| btc 1h change | -1.12 | -0.47 | -0.65 |

