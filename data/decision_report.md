# Decision Report

- generated_at: 2026-05-29T19:49:42.970638+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5070**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.88% / filled 20/20。**
- 全期間 MARKET基準: n=5070, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=+0.88%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.88% | **+0.88%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 9/16 | 56.2% | +2.58% | **+1.45%** |
| ASK | 20/20 | 100.0% | +0.89% | **+0.89%** |
| LIMIT_6PCT | 6/20 | 30.0% | +2.94% | **+0.88%** |
| MARKET | 20/20 | 100.0% | +0.88% | **+0.88%** |
| LIMIT_7PCT | 4/20 | 20.0% | +3.70% | **+0.74%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 6/20 | 30.0% | +2.91% | **+0.87%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +0.82% | **+0.78%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +1.30% | **+0.58%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +0.55% | **+0.41%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.07% | **+0.31%** |

## 2. $100 Live Portfolio

- 残高: **$98.60** / 初期 $100.00 (-1.40%)
- 確定トレード: 74件 (TP 22 / SL 49 / EXP 3)
- 最新: LIT/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.60
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$125.68** / 初期 $100.00 (+25.68%)
- 確定: 740件 (Win 175 / Loss 226 / Flat 339) / skip 891件
- 成長率目線: 平均log +0.000309 / 幾何平均 +0.031% per trade / maxDD +4.72%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CTR/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $125.68

## 4. Latest Market Context

- 更新: 2026-05-29T19:49:37.593427+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.39% price=73625.4
- Funnel: target 774 → liquid 153 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=1, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 88.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| GUA/USDT:USDT | +18.92% | $6,552,869.32 |
| LAB/USDT:USDT | +11.49% | $108,237,998.03 |
| GRASS/USDT:USDT | +10.03% | $3,865,774.19 |
| XLM/USDT:USDT | +9.04% | $381,049,824.64 |
| HEI/USDT:USDT | +7.41% | $8,382,051.38 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LIT/USDT:USDT | below_relative_strength | +5.10% | +4.72% |
| LAB/USDT:USDT | below_1h_threshold | +4.78% | +4.39% |
| TRIA/USDT:USDT | below_1h_threshold | +3.44% | +3.05% |
| CRWVSTOCK/USDT:USDT | below_1h_threshold | +2.97% | +2.58% |
| ASTSSTOCK/USDT:USDT | below_1h_threshold | +2.56% | +2.18% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
