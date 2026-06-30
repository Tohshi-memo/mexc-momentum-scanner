# Decision Report

- generated_at: 2026-06-30T01:42:45.823558+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7844**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.45% / filled 20/20。**
- 全期間 MARKET基準: n=7844, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=+0.45%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.45% | **+0.45%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT | 13/20 | 65.0% | +0.89% | **+0.58%** |
| MARKET | 20/20 | 100.0% | +0.45% | **+0.45%** |
| LIMIT_2PCT | 15/20 | 75.0% | +0.48% | **+0.36%** |
| ASK | 20/20 | 100.0% | +0.36% | **+0.36%** |
| LIMIT_1PCT | 17/20 | 85.0% | +0.42% | **+0.35%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 9/9 | 100.0% | +0.52% | **+0.52%** |
| LIMIT_ATR_LONG | 16/20 | 80.0% | +0.48% | **+0.38%** |
| MARKET_LONG | 20/20 | 100.0% | +0.27% | **+0.27%** |
| ASK_LONG | 20/20 | 100.0% | +0.24% | **+0.24%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +1.50% | **+0.15%** |

## 2. $100 Live Portfolio

- 残高: **$101.62** / 初期 $100.00 (+1.62%)
- 確定トレード: 46件 (TP 16 / SL 29 / EXP 1)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.62
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$261.74** / 初期 $100.00 (+161.74%)
- 確定: 2348件 (Win 714 / Loss 783 / Flat 851) / skip 2057件
- 成長率目線: 平均log +0.000410 / 幾何平均 +0.041% per trade / maxDD +8.13%
- 次の候補: `LIMIT_6PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: H/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $261.74

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.45** / 初期 $100.00 (+6.45%)
- 確定: 457件 (Win 120 / Loss 119 / Flat 218) / skip 798件
- 成長率目線: 平均log +0.000137 / 幾何平均 +0.014% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: GWEI/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $106.45

## 5. Latest Market Context

- 更新: 2026-06-30T01:42:38.192849+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.00% price=59806.2
- Funnel: target 811 → liquid 152 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 66.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ANSEM/USDT:USDT | +27.98% | $1,036,540.20 |
| AIGENSYN/USDT:USDT | +26.90% | $3,707,144.86 |
| SYN/USDT:USDT | +20.41% | $22,709,029.13 |
| H/USDT:USDT | +19.01% | $7,313,868.93 |
| BAS/USDT:USDT | +18.28% | $3,116,978.20 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SYN/USDT:USDT | below_1h_threshold | +4.16% | +4.16% |
| GWEI/USDT:USDT | below_1h_threshold | +4.08% | +4.08% |
| SLX/USDT:USDT | below_1h_threshold | +3.43% | +3.43% |
| KORU/USDT:USDT | below_1h_threshold | +2.35% | +2.35% |
| BEAT/USDT:USDT | below_1h_threshold | +2.19% | +2.19% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
