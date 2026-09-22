# Decision Report

- generated_at: 2026-09-22T08:51:30.366135+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15309**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=15309, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.21%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.21% | **-0.21%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 9/17 | 52.9% | +3.35% | **+1.77%** |
| LIMIT_7PCT | 3/20 | 15.0% | +4.54% | **+0.68%** |
| LIMIT_6PCT | 3/20 | 15.0% | +3.92% | **+0.59%** |
| LIMIT_5PCT | 3/20 | 15.0% | +3.30% | **+0.50%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | +0.50% | **+0.23%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/3 | 66.7% | +5.29% | **+3.53%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.23% | **+1.05%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +3.27% | **+0.65%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +2.00% | **+0.60%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +0.71% | **+0.46%** |

## 2. $100 Live Portfolio

- 残高: **$120.44** / 初期 $100.00 (+20.44%)
- 確定トレード: 216件 (TP 79 / SL 132 / EXP 5)
- 最新: PIEVERSE/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.44
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,175.15** / 初期 $100.00 (+1075.15%)
- 確定: 5800件 (Win 1724 / Loss 1868 / Flat 2208) / skip 6070件
- 成長率目線: 平均log +0.000425 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: S/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $1,175.15

## 4. Robust Adaptive DryRun ($100)

- 残高: **$248.25** / 初期 $100.00 (+148.25%)
- 確定: 3348件 (Win 924 / Loss 779 / Flat 1645) / skip 5372件
- 成長率目線: 平均log +0.000272 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: S/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $248.25

## 5. Causal Adaptive DryRun ($100)

- 残高: **$122.65** / 初期 $100.00 (+22.65%)
- 確定: 3081件 (Win 905 / Loss 1206 / Flat 970) / pending 5件 / skip 3695件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000131 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: S/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $122.65

## 6. Latest Market Context

- 更新: 2026-09-22T08:51:20.263653+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.99% price=86167.6
- Funnel: target 1056 → liquid 189 → pre 50 → checked 50 → surge 3 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 67.7 >= 65=1, 4h RSI 67.1 >= 65=1, 4h RSI 87.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AGT/USDT:USDT | +53.14% | $1,173,252.04 |
| 4STOCK/USDT:USDT | +45.84% | $1,974,608.37 |
| KERNEL/USDT:USDT | +34.66% | $4,077,314.42 |
| MUBARAK/USDT:USDT | +22.75% | $3,089,901.09 |
| GRASS/USDT:USDT | +22.60% | $3,248,454.83 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| WIF/USDT:USDT | below_1h_threshold | +4.99% | +4.00% |
| USELESS/USDT:USDT | below_1h_threshold | +4.55% | +3.56% |
| AERO/USDT:USDT | below_1h_threshold | +4.34% | +3.35% |
| SYN/USDT:USDT | below_1h_threshold | +3.81% | +2.82% |
| FET/USDT:USDT | below_1h_threshold | +3.71% | +2.72% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
