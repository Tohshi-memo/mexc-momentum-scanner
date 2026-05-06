# Decision Report

- generated_at: 2026-05-06T20:47:34.644428+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3498**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3498, expectancy=-0.15%
- 直近20件 MARKET基準: n=20, expectancy=-0.03%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.03% | **-0.03%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 4/13 | 30.8% | +1.81% | **+0.56%** |
| LIMIT_7PCT | 2/20 | 10.0% | +5.40% | **+0.54%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.98% | **+0.29%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| ASK | 20/20 | 100.0% | +0.01% | **+0.01%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/7 | 42.9% | +7.41% | **+3.18%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +1.08% | **+1.03%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +1.11% | **+0.94%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +1.36% | **+0.82%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +1.48% | **+0.67%** |

## 2. $100 Live Portfolio

- 残高: **$101.34** / 初期 $100.00 (+1.34%)
- 確定トレード: 19件 (TP 6 / SL 11 / EXP 2)
- 最新: TAG/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.34
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$98.01** / 初期 $100.00 (-1.99%)
- 確定: 9件 (Win 0 / Loss 4 / Flat 5) / skip 50件
- 成長率目線: 平均log -0.002228 / 幾何平均 -0.223% per trade / maxDD +1.99%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LYN/USDT:USDT `LIMIT_BB3S` SL_HIT account -0.50% 残高後 $98.01

## 4. Latest Market Context

- 更新: 2026-05-06T20:47:31.578430+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.13% price=81310.3
- Funnel: target 765 → liquid 196 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 86.1 >= 65=1, 4h RSI 68.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PLAY/USDT:USDT | +53.52% | $11,252,481.94 |
| ARMSTOCK/USDT:USDT | +10.10% | $6,959,868.58 |
| ZEREBRO/USDT:USDT | +9.75% | $1,149,734.74 |
| SMCISTOCK/USDT:USDT | +8.27% | $9,759,681.70 |
| DOGS/USDT:USDT | +7.09% | $6,666,274.44 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ZEREBRO/USDT:USDT | below_1h_threshold | +4.28% | +4.41% |
| UB/USDT:USDT | below_1h_threshold | +2.39% | +2.52% |
| PANWSTOCK/USDT:USDT | below_1h_threshold | +2.20% | +2.33% |
| BILL/USDT:USDT | below_1h_threshold | +2.07% | +2.20% |
| PLAY/USDT:USDT | below_1h_threshold | +1.97% | +2.10% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
