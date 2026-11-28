# Decision Report

- generated_at: 2026-11-28T15:06:22.381726+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **19848**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=19848, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.40% | **-0.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 3/14 | 21.4% | +5.65% | **+1.21%** |
| LIMIT_8PCT | 2/20 | 10.0% | +3.70% | **+0.37%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |
| LIMIT_5PCT | 9/20 | 45.0% | +0.40% | **+0.18%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.67% | **+1.42%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +1.89% | **+1.32%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +6.27% | **+1.25%** |
| LIMIT_FIB1272_LONG | 6/20 | 30.0% | +4.10% | **+1.23%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +1.83% | **+1.19%** |

## 2. $100 Live Portfolio

- 残高: **$122.25** / 初期 $100.00 (+22.25%)
- 確定トレード: 294件 (TP 108 / SL 176 / EXP 10)
- 最新: AKE/USDT:USDT TP_HIT PnL +8.00% 残高後 $122.25
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,992.49** / 初期 $100.00 (+1892.49%)
- 確定: 7674件 (Win 2210 / Loss 2471 / Flat 2993) / skip 8735件
- 成長率目線: 平均log +0.000390 / 幾何平均 +0.039% per trade / maxDD +9.04%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PIEVERSE/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $1,992.49

## 4. Robust Adaptive DryRun ($100)

- 残高: **$460.06** / 初期 $100.00 (+360.06%)
- 確定: 5298件 (Win 1410 / Loss 1141 / Flat 2747) / skip 7961件
- 成長率目線: 平均log +0.000288 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0461 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: EVAA/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $460.06

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 8011件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000187 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-28T15:06:10.536628+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.03% price=59304.4
- Funnel: target 1101 → liquid 127 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 92.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| O/USDT:USDT | +76.16% | $2,139,667.71 |
| EVAA/USDT:USDT | +58.96% | $38,371,357.34 |
| BTW/USDT:USDT | +34.63% | $19,199,345.12 |
| LAB/USDT:USDT | +26.81% | $1,557,906.03 |
| ACE/USDT:USDT | +23.48% | $6,970,415.77 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| IDOL/USDT:USDT | below_1h_threshold | +3.37% | +3.34% |
| LAB/USDT:USDT | below_1h_threshold | +1.77% | +1.74% |
| MUU/USDT:USDT | below_1h_threshold | +0.76% | +0.73% |
| TAG/USDT:USDT | below_1h_threshold | +0.59% | +0.56% |
| SNXX/USDT:USDT | below_1h_threshold | +0.58% | +0.55% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
