# Decision Report

- generated_at: 2026-08-31T04:46:37.776395+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13140**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.80% / filled 20/20。**
- 全期間 MARKET基準: n=13140, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.80%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |
| LIMIT_BB3S | 8/20 | 40.0% | +1.65% | **+0.66%** |
| LIMIT_2PCT | 16/20 | 80.0% | +0.40% | **+0.32%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.34% | **+0.31%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.95% | **+0.29%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.19% | **+1.07%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +0.85% | **+0.64%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +4.15% | **+0.62%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +2.82% | **+0.56%** |
| MARKET_LONG | 20/20 | 100.0% | +0.20% | **+0.20%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 194件 (TP 73 / SL 116 / EXP 5)
- 最新: SKR/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$804.75** / 初期 $100.00 (+704.75%)
- 確定: 4872件 (Win 1485 / Loss 1606 / Flat 1781) / skip 4829件
- 成長率目線: 平均log +0.000428 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ZORA/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $804.75

## 4. Robust Adaptive DryRun ($100)

- 残高: **$173.14** / 初期 $100.00 (+73.14%)
- 確定: 2167件 (Win 601 / Loss 528 / Flat 1038) / skip 4384件
- 成長率目線: 平均log +0.000253 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0800 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ZORA/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $173.14

## 5. Causal Adaptive DryRun ($100)

- 残高: **$115.89** / 初期 $100.00 (+15.89%)
- 確定: 2084件 (Win 610 / Loss 812 / Flat 662) / pending 0件 / skip 2528件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000282 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ZORA/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $115.89

## 6. Latest Market Context

- 更新: 2026-08-31T04:46:21.195569+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.24% price=77542.7
- Funnel: target 1026 → liquid 145 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 91.7 >= 65=1, 4h RSI 71.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SKR/USDT:USDT | +59.81% | $33,658,848.98 |
| ZORA/USDT:USDT | +53.09% | $4,949,655.48 |
| HEMI/USDT:USDT | +36.57% | $4,349,684.56 |
| BASECAT/USDT:USDT | +29.67% | $1,578,065.63 |
| ZKSYNC/USDT:USDT | +10.04% | $2,042,297.94 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CYS/USDT:USDT | below_1h_threshold | +2.20% | +2.44% |
| EGLD/USDT:USDT | below_1h_threshold | +1.40% | +1.64% |
| TOKYOELSTOCK/USDT:USDT | below_1h_threshold | +1.40% | +1.64% |
| XMR/USDT:USDT | below_1h_threshold | +1.35% | +1.59% |
| STRK/USDT:USDT | below_1h_threshold | +1.10% | +1.34% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
