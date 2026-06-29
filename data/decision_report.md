# Decision Report

- generated_at: 2026-06-29T01:25:35.044247+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7780**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +3.09% / filled 20/20。**
- 全期間 MARKET基準: n=7780, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+3.09%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +3.09% | **+3.09%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +3.09% | **+3.09%** |
| ASK | 20/20 | 100.0% | +3.08% | **+3.08%** |
| LIMIT_BB3S | 6/15 | 40.0% | +3.14% | **+1.26%** |
| LIMIT_1PCT | 14/20 | 70.0% | +1.71% | **+1.19%** |
| LIMIT_2PCT | 11/20 | 55.0% | +2.07% | **+1.14%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +5.70% | **+0.85%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +0.89% | **+0.40%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | -0.29% | **-0.14%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | -2.07% | **-0.31%** |

## 2. $100 Live Portfolio

- 残高: **$102.65** / 初期 $100.00 (+2.65%)
- 確定トレード: 41件 (TP 15 / SL 25 / EXP 1)
- 最新: M/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.65
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$258.80** / 初期 $100.00 (+158.80%)
- 確定: 2284件 (Win 694 / Loss 762 / Flat 828) / skip 2057件
- 成長率目線: 平均log +0.000416 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SYN/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $258.80

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.45** / 初期 $100.00 (+6.45%)
- 確定: 456件 (Win 120 / Loss 119 / Flat 217) / skip 735件
- 成長率目線: 平均log +0.000137 / 幾何平均 +0.014% per trade / maxDD +3.03%
- 次の候補: `LIMIT_7PCT` (selected_by_robust_growth_score) / robust_score +0.0219 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SYN/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $106.45

## 5. Latest Market Context

- 更新: 2026-06-29T01:25:30.407279+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.49% price=59343.8
- Funnel: target 805 → liquid 127 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SYN/USDT:USDT | +16.70% | $8,712,772.69 |
| NES/USDT:USDT | +13.44% | $3,014,289.42 |
| BAS/USDT:USDT | +12.27% | $4,833,404.24 |
| G/USDT:USDT | +10.80% | $1,179,505.84 |
| BEAT/USDT:USDT | +9.80% | $31,147,077.21 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CELO/USDT:USDT | below_1h_threshold | +3.13% | +3.62% |
| G/USDT:USDT | below_1h_threshold | +1.87% | +2.36% |
| SYN/USDT:USDT | below_1h_threshold | +1.68% | +2.17% |
| BEAT/USDT:USDT | below_1h_threshold | +1.66% | +2.15% |
| VELVET/USDT:USDT | below_1h_threshold | +0.97% | +1.46% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
