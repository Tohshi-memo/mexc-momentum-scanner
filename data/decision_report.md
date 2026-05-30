# Decision Report

- generated_at: 2026-05-30T08:25:10.110973+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5111**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5111, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-0.14%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.14% | **-0.14%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 4/20 | 20.0% | +7.15% | **+1.43%** |
| LIMIT_10PCT | 3/20 | 15.0% | +8.00% | **+1.20%** |
| LIMIT_8PCT | 4/20 | 20.0% | +3.93% | **+0.79%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +1.28% | **+0.45%** |
| LIMIT_7PCT | 4/20 | 20.0% | +0.70% | **+0.14%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/4 | 100.0% | +1.19% | **+1.19%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +1.40% | **+0.84%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +1.19% | **+0.78%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.89% | **+0.75%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +0.69% | **+0.51%** |

## 2. $100 Live Portfolio

- 残高: **$98.10** / 初期 $100.00 (-1.90%)
- 確定トレード: 75件 (TP 22 / SL 50 / EXP 3)
- 最新: ESPORTS/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.10
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$125.53** / 初期 $100.00 (+25.53%)
- 確定: 766件 (Win 178 / Loss 230 / Flat 358) / skip 906件
- 成長率目線: 平均log +0.000297 / 幾何平均 +0.030% per trade / maxDD +4.72%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: EDEN/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $125.53

## 4. Latest Market Context

- 更新: 2026-05-30T08:25:07.825043+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.00% price=73517.8
- Funnel: target 773 → liquid 130 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 88.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HEI/USDT:USDT | +65.24% | $14,946,982.85 |
| VTHO/USDT:USDT | +29.49% | $1,132,029.76 |
| LAB/USDT:USDT | +23.32% | $122,092,264.41 |
| XLM/USDT:USDT | +17.66% | $440,605,222.57 |
| ID/USDT:USDT | +12.95% | $6,739,020.59 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BEAT/USDT:USDT | below_1h_threshold | +2.15% | +2.14% |
| ID/USDT:USDT | below_1h_threshold | +2.07% | +2.07% |
| GUA/USDT:USDT | below_1h_threshold | +2.03% | +2.03% |
| BILL/USDT:USDT | below_1h_threshold | +1.73% | +1.73% |
| PLAY/USDT:USDT | below_1h_threshold | +1.68% | +1.68% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
