# Decision Report

- generated_at: 2026-05-06T18:57:28.158873+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3495**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.56% / filled 20/20。**
- 全期間 MARKET基準: n=3495, expectancy=-0.15%
- 直近20件 MARKET基準: n=20, expectancy=+0.56%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.56% | **+0.56%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 5/14 | 35.7% | +3.04% | **+1.09%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.86% | **+0.77%** |
| LIMIT_3PCT | 15/20 | 75.0% | +1.02% | **+0.76%** |
| ASK | 20/20 | 100.0% | +0.60% | **+0.60%** |
| LIMIT_ATR | 13/20 | 65.0% | +0.88% | **+0.57%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/6 | 33.3% | +7.12% | **+2.37%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +3.32% | **+1.49%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +2.50% | **+1.00%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +1.96% | **+0.88%** |
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +2.55% | **+0.76%** |

## 2. $100 Live Portfolio

- 残高: **$101.34** / 初期 $100.00 (+1.34%)
- 確定トレード: 19件 (TP 6 / SL 11 / EXP 2)
- 最新: TAG/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.34
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$98.01** / 初期 $100.00 (-1.99%)
- 確定: 9件 (Win 0 / Loss 4 / Flat 5) / skip 47件
- 成長率目線: 平均log -0.002228 / 幾何平均 -0.223% per trade / maxDD +1.99%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LYN/USDT:USDT `LIMIT_BB3S` SL_HIT account -0.50% 残高後 $98.01

## 4. Latest Market Context

- 更新: 2026-05-06T18:57:25.309674+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.04% price=81367.4
- Funnel: target 766 → liquid 194 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 80.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PLAY/USDT:USDT | +42.06% | $6,900,005.64 |
| TAG/USDT:USDT | +7.97% | $15,295,973.33 |
| ZEREBRO/USDT:USDT | +7.40% | $1,063,270.36 |
| LAB/USDT:USDT | +6.42% | $227,486,868.93 |
| SMCISTOCK/USDT:USDT | +6.04% | $9,391,665.62 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| VVV/USDT:USDT | below_1h_threshold | +4.98% | +5.02% |
| TAG/USDT:USDT | below_1h_threshold | +4.39% | +4.43% |
| SMCISTOCK/USDT:USDT | below_1h_threshold | +3.08% | +3.12% |
| ZRO/USDT:USDT | below_1h_threshold | +3.07% | +3.11% |
| UB/USDT:USDT | below_1h_threshold | +2.62% | +2.67% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
