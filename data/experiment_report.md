# Filter Granularity Experiment Report

- source: `data/experiments.json`
- closed shadow trades: **18**

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
| ALL candidates | 18 | 8/10/0 | 44.4% | +10.26% | -4.00% | +2.34% | +42.1% | 0.5h |
| STRICT (current) | 0 | – | – | – | – | – | – | – |
| REJECTED by STRICT | 18 | 8/10/0 | 44.4% | +10.26% | -4.00% | +2.34% | +42.1% | 0.5h |

**読み方**: STRICT が REJECTED より expectancy が高ければ現フィルターは有効。REJECTED の方が良ければフィルターを緩めるべき。

---

## 2. RSI(1h) threshold sweep

現行 STRICT は RSI ≥ 75。閾値を変えた場合の仮想成績。

| group | n | W/L/E | win% | avg win | avg loss | expectancy | total PnL | median hold |
|-------|---|-------|------|---------|----------|------------|-----------|-------------|
| RSI ≥ 60 | 12 | 5/7/0 | 41.7% | +10.37% | -4.00% | +1.99% | +23.8% | 0.4h |
| RSI ≥ 65 | 10 | 5/5/0 | 50.0% | +10.37% | -4.00% | +3.18% | +31.8% | 0.4h |
| RSI ≥ 70 | 9 | 4/5/0 | 44.4% | +10.90% | -4.00% | +2.62% | +23.6% | 0.4h |
| RSI ≥ 75 | 6 | 3/3/0 | 50.0% | +9.82% | -4.00% | +2.91% | +17.5% | 0.4h |
| RSI ≥ 80 | 4 | 2/2/0 | 50.0% | +10.46% | -4.00% | +3.23% | +12.9% | 0.4h |


---

## 3. RSI(4h) maximum sweep

現行 STRICT は 4h RSI < 70。低いほど厳しい (既存トレンドを除外)。
OFF = 4h フィルター無効。

| group | n | W/L/E | win% | avg win | avg loss | expectancy | total PnL | median hold |
|-------|---|-------|------|---------|----------|------------|-----------|-------------|
| 4h RSI < 60 | 5 | 1/4/0 | 20.0% | +8.51% | -4.00% | -1.50% | -7.5% | 0.7h |
| 4h RSI < 65 | 7 | 1/6/0 | 14.3% | +8.51% | -4.00% | -2.21% | -15.5% | 0.7h |
| 4h RSI < 70 | 9 | 3/6/0 | 33.3% | +8.27% | -4.00% | +0.09% | +0.8% | 0.7h |
| 4h RSI < 75 | 10 | 4/6/0 | 40.0% | +9.62% | -4.00% | +1.45% | +14.5% | 0.6h |
| OFF (no 4h filter) | 18 | 8/10/0 | 44.4% | +10.26% | -4.00% | +2.34% | +42.1% | 0.5h |


---

## 4. BB upper break requirement

現行 STRICT は price > BB upper(2σ) 必須。

| group | n | W/L/E | win% | avg win | avg loss | expectancy | total PnL | median hold |
|-------|---|-------|------|---------|----------|------------|-----------|-------------|
| BB break required | 4 | 1/3/0 | 25.0% | +9.45% | -4.00% | -0.64% | -2.6% | 0.5h |
| BB break NOT required (all) | 18 | 8/10/0 | 44.4% | +10.26% | -4.00% | +2.34% | +42.1% | 0.5h |
| BB no-break only | 14 | 7/7/0 | 50.0% | +10.38% | -4.00% | +3.19% | +44.6% | 0.5h |


---

## 5. Volume trend filter

現行 STRICT は『RISING を除外』(疲弊兆候のみショート)。

| group | n | W/L/E | win% | avg win | avg loss | expectancy | total PnL | median hold |
|-------|---|-------|------|---------|----------|------------|-----------|-------------|
| ALL volume trends | 18 | 8/10/0 | 44.4% | +10.26% | -4.00% | +2.34% | +42.1% | 0.5h |
| NOT RISING (current) | 17 | 8/9/0 | 47.1% | +10.26% | -4.00% | +2.71% | +46.1% | 0.5h |
| DECLINING only (strictest) | 13 | 5/8/0 | 38.5% | +9.41% | -4.00% | +1.16% | +15.0% | 0.5h |
| FLAT only | 4 | 3/1/0 | 75.0% | +11.68% | -4.00% | +7.76% | +31.0% | 0.7h |
| RISING only | 1 | 0/1/0 | 0.0% | +0.00% | -4.00% | -4.00% | -4.0% | 0.3h |


---

## 6. Relative strength (vs BTC) threshold sweep

現行スキャナーは alt_1h - btc_1h ≥ 5.0% でフィルター。
閾値を変えた場合の仮想成績。

| group | n | W/L/E | win% | avg win | avg loss | expectancy | total PnL | median hold |
|-------|---|-------|------|---------|----------|------------|-----------|-------------|
| rel strength ≥ 0% | 18 | 8/10/0 | 44.4% | +10.26% | -4.00% | +2.34% | +42.1% | 0.5h |
| rel strength ≥ 3% | 18 | 8/10/0 | 44.4% | +10.26% | -4.00% | +2.34% | +42.1% | 0.5h |
| rel strength ≥ 5% | 18 | 8/10/0 | 44.4% | +10.26% | -4.00% | +2.34% | +42.1% | 0.5h |
| rel strength ≥ 7% | 9 | 4/5/0 | 44.4% | +8.64% | -4.00% | +1.62% | +14.6% | 0.4h |
| rel strength ≥ 10% | 4 | 3/1/0 | 75.0% | +8.83% | -4.00% | +5.62% | +22.5% | 0.7h |


---

## 7. Market regime breakdown

BTC 1h change によるレジーム別の成績。

| group | n | W/L/E | win% | avg win | avg loss | expectancy | total PnL | median hold |
|-------|---|-------|------|---------|----------|------------|-----------|-------------|
| BEARISH | 2 | 1/1/0 | 50.0% | +8.06% | -4.00% | +2.03% | +4.1% | 0.5h |
| STAGNANT | 11 | 5/6/0 | 45.5% | +9.68% | -4.00% | +2.22% | +24.4% | 0.5h |
| BULLISH | 5 | 2/3/0 | 40.0% | +12.80% | -4.00% | +2.72% | +13.6% | 0.4h |


---

## 8. Fundamental / news

ファンダメンタル分析は confirmed シグナルのみに実行される。
UNKNOWN = ファンダ未取得 (rejected 候補)。

### By short conviction

| group | n | W/L/E | win% | avg win | avg loss | expectancy | total PnL | median hold |
|-------|---|-------|------|---------|----------|------------|-----------|-------------|
| HIGH | 0 | – | – | – | – | – | – | – |
| MEDIUM | 0 | – | – | – | – | – | – | – |
| LOW | 0 | – | – | – | – | – | – | – |
| AVOID | 0 | – | – | – | – | – | – | – |
| UNKNOWN | 18 | 8/10/0 | 44.4% | +10.26% | -4.00% | +2.34% | +42.1% | 0.5h |

### By catalyst type

| group | n | W/L/E | win% | avg win | avg loss | expectancy | total PnL | median hold |
|-------|---|-------|------|---------|----------|------------|-----------|-------------|
| NONE | 0 | – | – | – | – | – | – | – |
| POSITIVE | 0 | – | – | – | – | – | – | – |
| NEGATIVE | 0 | – | – | – | – | – | – | – |
| WEAK | 0 | – | – | – | – | – | – | – |
| UNKNOWN | 18 | 8/10/0 | 44.4% | +10.26% | -4.00% | +2.34% | +42.1% | 0.5h |

ファンダ取得済み: 0 件, 未取得: 18 件


---

## 9. Combined filters

代表的なフィルターの組み合わせの仮想成績。

| group | n | W/L/E | win% | avg win | avg loss | expectancy | total PnL | median hold |
|-------|---|-------|------|---------|----------|------------|-----------|-------------|
| STRICT (RSI≥75 & 4h<70 & ¬RISING) | 0 | – | – | – | – | – | – | – |
| RSI≥70 & 4h<70 & ¬RISING | 0 | – | – | – | – | – | – | – |
| RSI≥70 & 4h<75 & ¬RISING | 0 | – | – | – | – | – | – | – |
| RSI≥70 & ¬RISING (no 4h) | 8 | 4/4/0 | 50.0% | +10.90% | -4.00% | +3.45% | +27.6% | 0.4h |
| RSI≥65 & 4h<70 & DECLINING | 1 | 1/0/0 | 100.0% | +8.24% | +0.00% | +8.24% | +8.2% | 1.4h |


---

## 10. Entry strategy comparison

成行 (MARKET), ask 価格 (ASK), 指値 (LIMIT_1PCT/2PCT) の仮想成績。
指値は検出後に価格がエントリー指定値まで上がったら約定。
上がらなければ unfilled (filled 列の分母に含まれるが PnL は 0)。

### Spread statistics

- スプレッドデータなし (order book 未取得の古いレコード)

### Strategy PnL

| strategy | filled | n (w/ pnl) | avg PnL | total PnL | win% |
|----------|--------|------------|---------|-----------|------|
| MARKET | 0/0 | 0 | – | – | – |
| ASK | 0/0 | 0 | – | – | – |
| LIMIT_1PCT | 0/0 | 0 | – | – | – |
| LIMIT_2PCT | 0/0 | 0 | – | – | – |

**解釈**:
- MARKET vs ASK の差 = スプレッドコスト。ASK の方が PnL 低ければスプレッドが痛い。
- LIMIT の方が avg PnL 高ければ「もう少し上がってから入る」方が有利。
  ただし filled 率が低ければ機会損失とのトレードオフ。


---

## 11. Indicator distribution: winners vs losers

TP_HIT と SL_HIT の指標平均。乖離が大きい指標が予測力を持つ可能性あり。

| indicator | wins (avg) | losses (avg) | delta |
|-----------|------------|--------------|-------|
| RSI(1h) | +71.42 | +67.56 | +3.86 |
| RSI(4h) | +76.77 | +67.88 | +8.89 |
| price/BB upper | +0.93 | +0.94 | -0.01 |
| volume ratio | +0.76 | +0.70 | +0.06 |
| ATR% | +8.09 | +6.75 | +1.34 |
| change_1h | +9.11 | +7.75 | +1.36 |
| rel strength | +9.34 | +7.86 | +1.48 |
| btc 1h change | -0.23 | -0.10 | -0.13 |

