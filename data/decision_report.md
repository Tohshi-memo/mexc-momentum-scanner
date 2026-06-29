# Decision Report

- generated_at: 2026-06-29T14:19:07.713458+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7819**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.16% / filled 20/20。**
- 全期間 MARKET基準: n=7819, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+1.16%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.16% | **+1.16%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.35% | **+1.35%** |
| MARKET | 20/20 | 100.0% | +1.16% | **+1.16%** |
| LIMIT_6PCT | 6/20 | 30.0% | +2.94% | **+0.88%** |
| LIMIT_2PCT | 15/20 | 75.0% | +0.68% | **+0.51%** |
| LIMIT_7PCT | 4/20 | 20.0% | +2.40% | **+0.48%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +4.15% | **+0.62%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +1.49% | **+0.60%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +2.82% | **+0.56%** |
| LIMIT_BB3S_LONG | 7/10 | 70.0% | +0.53% | **+0.37%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +0.50% | **+0.20%** |

## 2. $100 Live Portfolio

- 残高: **$102.14** / 初期 $100.00 (+2.14%)
- 確定トレード: 42件 (TP 15 / SL 26 / EXP 1)
- 最新: G/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.14
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$263.87** / 初期 $100.00 (+163.87%)
- 確定: 2323件 (Win 708 / Loss 774 / Flat 841) / skip 2057件
- 成長率目線: 平均log +0.000418 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `LIMIT_6PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: GUA/USDT:USDT `LIMIT_6PCT` SL_HIT account +0.24% 残高後 $263.87

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.45** / 初期 $100.00 (+6.45%)
- 確定: 457件 (Win 120 / Loss 119 / Flat 218) / skip 773件
- 成長率目線: 平均log +0.000137 / 幾何平均 +0.014% per trade / maxDD +3.03%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0341 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: GWEI/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $106.45

## 5. Latest Market Context

- 更新: 2026-06-29T14:18:59.549149+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.80% price=59080.7
- Funnel: target 810 → liquid 148 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TAC/USDT:USDT | +152.15% | $30,722,434.44 |
| GWEI/USDT:USDT | +36.11% | $2,743,878.93 |
| RAVE/USDT:USDT | +35.43% | $44,833,310.90 |
| G/USDT:USDT | +25.87% | $2,789,881.45 |
| UB/USDT:USDT | +24.45% | $2,575,125.80 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TAC/USDT:USDT | below_1h_threshold | +3.16% | +3.96% |
| O/USDT:USDT | below_1h_threshold | +1.62% | +2.42% |
| SYN/USDT:USDT | below_1h_threshold | +1.62% | +2.42% |
| SLX/USDT:USDT | below_1h_threshold | +1.27% | +2.07% |
| RAVE/USDT:USDT | below_1h_threshold | +1.15% | +1.96% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
