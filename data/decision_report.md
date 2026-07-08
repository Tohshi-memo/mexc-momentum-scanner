# Decision Report

- generated_at: 2026-07-08T04:58:06.705146+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8466**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.89% / filled 20/20。**
- 全期間 MARKET基準: n=8466, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+1.89%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.89% | **+1.89%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.89% | **+1.89%** |
| ASK | 20/20 | 100.0% | +1.81% | **+1.81%** |
| LIMIT_9PCT | 3/20 | 15.0% | +4.59% | **+0.69%** |
| LIMIT_10PCT | 2/20 | 10.0% | +5.45% | **+0.55%** |
| LIMIT_BB3S | 3/19 | 15.8% | +2.64% | **+0.42%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +0.60% | **+0.60%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +2.11% | **+0.32%** |
| MARKET_LONG | 20/20 | 100.0% | +0.05% | **+0.05%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +0.00% | **+0.00%** |
| LIMIT_10PCT_LONG | 5/20 | 25.0% | -0.27% | **-0.07%** |

## 2. $100 Live Portfolio

- 残高: **$103.08** / 初期 $100.00 (+3.08%)
- 確定トレード: 73件 (TP 26 / SL 46 / EXP 1)
- 最新: DRAM/USDT:USDT TP_HIT PnL +5.87% 残高後 $103.08
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$320.19** / 初期 $100.00 (+220.19%)
- 確定: 2671件 (Win 848 / Loss 898 / Flat 925) / skip 2356件
- 成長率目線: 平均log +0.000436 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_10PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CLO/USDT:USDT `LIMIT_10PCT_LONG` EXPIRED account +0.00% 残高後 $320.19

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.48** / 初期 $100.00 (+5.48%)
- 確定: 641件 (Win 152 / Loss 158 / Flat 331) / skip 1236件
- 成長率目線: 平均log +0.000083 / 幾何平均 +0.008% per trade / maxDD +3.57%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: EVAA/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $105.48

## 5. Latest Market Context

- 更新: 2026-07-08T04:57:56.495477+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=62725.9
- Funnel: target 847 → liquid 177 → pre 50 → checked 50 → surge 4 → strict 1
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 95.4 >= 65=1, 4h RSI 86.3 >= 65=1, 4h RSI 90.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| EVAA/USDT:USDT | +48.37% | $57,426,032.90 |
| EDGE/USDT:USDT | +19.94% | $13,621,930.56 |
| SYN/USDT:USDT | +16.29% | $4,338,072.54 |
| NES/USDT:USDT | +14.14% | $1,058,768.31 |
| CLO/USDT:USDT | +9.57% | $1,109,029.65 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SLX/USDT:USDT | below_1h_threshold | +3.36% | +3.39% |
| H/USDT:USDT | below_1h_threshold | +1.52% | +1.54% |
| UNI/USDT:USDT | below_1h_threshold | +1.46% | +1.49% |
| NES/USDT:USDT | below_1h_threshold | +0.70% | +0.72% |
| BACSTOCK/USDT:USDT | below_1h_threshold | +0.54% | +0.56% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
