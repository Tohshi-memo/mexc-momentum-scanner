# Decision Report

- generated_at: 2026-10-19T01:11:14.120224+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **16968**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.00% / filled 20/20。**
- 全期間 MARKET基準: n=16968, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+2.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.00% | **+2.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.00% | **+2.00%** |
| LIMIT_2PCT | 15/20 | 75.0% | +1.75% | **+1.31%** |
| LIMIT_3PCT | 13/20 | 65.0% | +1.56% | **+1.01%** |
| LIMIT_BB3S | 3/20 | 15.0% | +5.62% | **+0.84%** |
| LIMIT_1PCT | 16/20 | 80.0% | +0.95% | **+0.76%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT_LONG | 14/20 | 70.0% | +1.32% | **+0.93%** |
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +2.55% | **+0.76%** |
| LIMIT_ATR_LONG | 15/20 | 75.0% | +1.00% | **+0.75%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +4.15% | **+0.62%** |
| LIMIT_4PCT_LONG | 15/20 | 75.0% | +0.80% | **+0.60%** |

## 2. $100 Live Portfolio

- 残高: **$121.60** / 初期 $100.00 (+21.60%)
- 確定トレード: 245件 (TP 91 / SL 147 / EXP 7)
- 最新: ICNT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.60
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,273.17** / 初期 $100.00 (+1173.17%)
- 確定: 6414件 (Win 1866 / Loss 2052 / Flat 2496) / skip 7115件
- 成長率目線: 平均log +0.000397 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `MARKET` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AGT/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.50% 残高後 $1,273.17

## 4. Robust Adaptive DryRun ($100)

- 残高: **$276.84** / 初期 $100.00 (+176.84%)
- 確定: 3733件 (Win 1034 / Loss 881 / Flat 1818) / skip 6646件
- 成長率目線: 平均log +0.000273 / 幾何平均 +0.027% per trade / maxDD +4.13%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score -0.0096 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: APR/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $276.84

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5127件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000379 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-19T01:11:02.013454+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.15% price=82395.6
- Funnel: target 1084 → liquid 143 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| APR/USDT:USDT | +16.07% | $1,834,552.46 |
| ZEREBRO/USDT:USDT | +11.45% | $1,190,066.66 |
| SNXX/USDT:USDT | +10.95% | $8,291,889.10 |
| KORU/USDT:USDT | +10.87% | $26,853,585.33 |
| SOXL/USDT:USDT | +9.72% | $19,453,949.86 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SOXL/USDT:USDT | below_1h_threshold | +3.82% | +3.67% |
| KORU/USDT:USDT | below_1h_threshold | +3.46% | +3.31% |
| APR/USDT:USDT | below_1h_threshold | +3.37% | +3.22% |
| SNXX/USDT:USDT | below_1h_threshold | +3.20% | +3.05% |
| ARIA/USDT:USDT | below_1h_threshold | +3.14% | +2.98% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
