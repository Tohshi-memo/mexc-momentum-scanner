# Decision Report

- generated_at: 2026-09-22T00:16:20.854488+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15284**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.04% / filled 20/20。**
- 全期間 MARKET基準: n=15284, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+1.04%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.04% | **+1.04%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +1.24% | **+1.17%** |
| MARKET | 20/20 | 100.0% | +1.04% | **+1.04%** |
| LIMIT_BB3S | 9/16 | 56.2% | +0.84% | **+0.47%** |
| LIMIT_6PCT | 3/20 | 15.0% | +0.20% | **+0.03%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | -0.08% | **-0.03%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +4.55% | **+0.45%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +1.33% | **+0.40%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.22% | **+0.19%** |
| MARKET_LONG | 20/20 | 100.0% | +0.18% | **+0.18%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +0.18% | **+0.08%** |

## 2. $100 Live Portfolio

- 残高: **$120.44** / 初期 $100.00 (+20.44%)
- 確定トレード: 216件 (TP 79 / SL 132 / EXP 5)
- 最新: PIEVERSE/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.44
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,178.54** / 初期 $100.00 (+1078.54%)
- 確定: 5775件 (Win 1718 / Loss 1856 / Flat 2201) / skip 6070件
- 成長率目線: 平均log +0.000427 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SYN/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $1,178.54

## 4. Robust Adaptive DryRun ($100)

- 残高: **$248.78** / 初期 $100.00 (+148.78%)
- 確定: 3323件 (Win 918 / Loss 768 / Flat 1637) / skip 5372件
- 成長率目線: 平均log +0.000274 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0431 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SYN/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $248.78

## 5. Causal Adaptive DryRun ($100)

- 残高: **$122.78** / 初期 $100.00 (+22.78%)
- 確定: 3057件 (Win 899 / Loss 1195 / Flat 963) / pending 2件 / skip 3695件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000228 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: SYN/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $122.78

## 6. Latest Market Context

- 更新: 2026-09-22T00:16:09.729960+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.22% price=86395.7
- Funnel: target 1055 → liquid 178 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| FORM/USDT:USDT | +27.61% | $8,679,690.13 |
| ALCH/USDT:USDT | +25.08% | $2,209,945.29 |
| EVAA/USDT:USDT | +17.24% | $1,983,758.07 |
| PTB/USDT:USDT | +16.19% | $1,201,366.76 |
| TAO/USDT:USDT | +11.29% | $132,456,374.27 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PTB/USDT:USDT | below_1h_threshold | +3.41% | +3.63% |
| ALCH/USDT:USDT | below_1h_threshold | +2.19% | +2.41% |
| EVAA/USDT:USDT | below_1h_threshold | +1.72% | +1.94% |
| UNI/USDT:USDT | below_1h_threshold | +1.68% | +1.89% |
| KAS/USDT:USDT | below_1h_threshold | +1.46% | +1.67% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
