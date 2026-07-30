# Decision Report

- generated_at: 2026-07-30T19:36:19.821850+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9917**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9917, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-2.98%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.98% | **-2.98%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 2/20 | 10.0% | +5.40% | **+0.54%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_5PCT | 5/20 | 25.0% | +1.03% | **+0.26%** |
| LIMIT_4PCT | 16/20 | 80.0% | -0.22% | **-0.18%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | -0.65% | **-0.29%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +3.62% | **+2.90%** |
| MARKET_LONG | 20/20 | 100.0% | +2.78% | **+2.78%** |
| LIMIT_BB3S_LONG | 3/3 | 100.0% | +2.43% | **+2.43%** |
| LIMIT_2PCT_LONG | 11/20 | 55.0% | +3.74% | **+2.06%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +3.54% | **+1.95%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$497.17** / 初期 $100.00 (+397.17%)
- 確定: 3521件 (Win 1114 / Loss 1147 / Flat 1260) / skip 2957件
- 成長率目線: 平均log +0.000455 / 幾何平均 +0.046% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ROBO/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $497.17

## 4. Robust Adaptive DryRun ($100)

- 残高: **$136.91** / 初期 $100.00 (+36.91%)
- 確定: 1243件 (Win 344 / Loss 283 / Flat 616) / skip 2085件
- 成長率目線: 平均log +0.000253 / 幾何平均 +0.025% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0684 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: KOMA/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $136.91

## 5. Causal Adaptive DryRun ($100)

- 残高: **$110.80** / 初期 $100.00 (+10.80%)
- 確定: 803件 (Win 262 / Loss 318 / Flat 223) / pending 2件 / skip 593件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000108 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: AGT/USDT:USDT `MARKET` EXPIRED account +0.16% 残高後 $110.80

## 6. Latest Market Context

- 更新: 2026-07-30T19:36:13.048092+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.28% price=64851.9
- Funnel: target 920 → liquid 178 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ROBO/USDT:USDT | +16.18% | $2,564,766.31 |
| CAP/USDT:USDT | +15.27% | $3,938,413.57 |
| MMT/USDT:USDT | +14.88% | $5,783,464.32 |
| EVAA/USDT:USDT | +10.20% | $2,969,336.47 |
| KOMA/USDT:USDT | +5.06% | $5,618,110.35 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ROBO/USDT:USDT | below_1h_threshold | +2.80% | +2.52% |
| KOMA/USDT:USDT | below_1h_threshold | +2.61% | +2.32% |
| EIGEN/USDT:USDT | below_1h_threshold | +2.44% | +2.15% |
| FET/USDT:USDT | below_1h_threshold | +1.26% | +0.98% |
| PENGU/USDT:USDT | below_1h_threshold | +1.17% | +0.89% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
