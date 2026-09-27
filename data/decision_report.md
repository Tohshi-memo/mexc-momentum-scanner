# Decision Report

- generated_at: 2026-09-27T03:36:22.865279+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15635**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.45% / filled 20/20。**
- 全期間 MARKET基準: n=15635, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.45%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.45% | **+0.45%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 7/15 | 46.7% | +2.86% | **+1.33%** |
| LIMIT_2PCT | 17/20 | 85.0% | +1.45% | **+1.23%** |
| LIMIT_1PCT | 19/20 | 95.0% | +1.23% | **+1.17%** |
| LIMIT_7PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_ATR | 13/20 | 65.0% | +0.75% | **+0.49%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +2.61% | **+0.91%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +1.89% | **+0.85%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +3.27% | **+0.65%** |
| LIMIT_8PCT_LONG | 5/20 | 25.0% | +2.40% | **+0.60%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +1.39% | **+0.55%** |

## 2. $100 Live Portfolio

- 残高: **$120.87** / 初期 $100.00 (+20.87%)
- 確定トレード: 224件 (TP 82 / SL 135 / EXP 7)
- 最新: UNI/USDT:USDT EXPIRED PnL +1.69% 残高後 $120.87
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,239.61** / 初期 $100.00 (+1139.61%)
- 確定: 5978件 (Win 1766 / Loss 1923 / Flat 2289) / skip 6218件
- 成長率目線: 平均log +0.000421 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: TRIA/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $1,239.61

## 4. Robust Adaptive DryRun ($100)

- 残高: **$263.08** / 初期 $100.00 (+163.08%)
- 確定: 3533件 (Win 974 / Loss 812 / Flat 1747) / skip 5513件
- 成長率目線: 平均log +0.000274 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_FIB1272` (selected_by_robust_growth_score) / robust_score -0.0502 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: RARE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $263.08

## 5. Causal Adaptive DryRun ($100)

- 残高: **$119.00** / 初期 $100.00 (+19.00%)
- 確定: 3218件 (Win 946 / Loss 1275 / Flat 997) / pending 2件 / skip 3885件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000100 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: QNT/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $119.00

## 6. Latest Market Context

- 更新: 2026-09-27T03:36:11.791515+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.04% price=84379.4
- Funnel: target 1070 → liquid 142 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| QNT/USDT:USDT | +47.88% | $67,654,035.80 |
| GRASS/USDT:USDT | +9.16% | $5,257,995.80 |
| RUNE/USDT:USDT | +6.62% | $3,327,004.32 |
| ZEC/USDT:USDT | +5.84% | $876,349,870.94 |
| GRAM/USDT:USDT | +5.11% | $6,456,755.96 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| RUNE/USDT:USDT | below_1h_threshold | +2.23% | +2.27% |
| JTO/USDT:USDT | below_1h_threshold | +1.92% | +1.96% |
| STX/USDT:USDT | below_1h_threshold | +1.48% | +1.52% |
| DASH/USDT:USDT | below_1h_threshold | +1.10% | +1.15% |
| GRASS/USDT:USDT | below_1h_threshold | +0.89% | +0.93% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
