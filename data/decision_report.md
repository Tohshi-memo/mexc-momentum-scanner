# Decision Report

- generated_at: 2026-05-12T23:57:58.921487+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4169**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.31% / filled 20/20。**
- 全期間 MARKET基準: n=4169, expectancy=-0.13%
- 直近20件 MARKET基準: n=20, expectancy=+1.31%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.31% | **+1.31%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.31% | **+1.31%** |
| ASK | 20/20 | 100.0% | +0.95% | **+0.95%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +2.63% | **+0.79%** |
| LIMIT_BB3S | 9/19 | 47.4% | +1.11% | **+0.53%** |
| LIMIT_3PCT | 10/20 | 50.0% | +0.81% | **+0.41%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +1.73% | **+0.78%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +4.55% | **+0.45%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +1.14% | **+0.40%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | -0.15% | **-0.07%** |

## 2. $100 Live Portfolio

- 残高: **$98.69** / 初期 $100.00 (-1.31%)
- 確定トレード: 35件 (TP 9 / SL 23 / EXP 3)
- 最新: KITE/USDT:USDT SL_HIT PnL -3.91% 残高後 $98.69
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$120.58** / 初期 $100.00 (+20.58%)
- 確定: 305件 (Win 88 / Loss 106 / Flat 111) / skip 425件
- 成長率目線: 平均log +0.000613 / 幾何平均 +0.061% per trade / maxDD +4.21%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: TRUMPOFFICIAL/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $120.58

## 4. Latest Market Context

- 更新: 2026-05-12T23:57:55.462976+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.19% price=80460.9
- Funnel: target 758 → liquid 184 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 83.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VIC/USDT:USDT | +12.66% | $6,363,704.94 |
| AKT/USDT:USDT | +11.22% | $2,568,216.77 |
| LAB/USDT:USDT | +9.98% | $112,845,518.39 |
| IRYS/USDT:USDT | +8.91% | $2,184,433.50 |
| PEAQ/USDT:USDT | +8.23% | $2,109,018.69 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TROLLSOL/USDT:USDT | below_1h_threshold | +3.25% | +3.44% |
| UB/USDT:USDT | below_1h_threshold | +2.85% | +3.04% |
| BASED/USDT:USDT | below_1h_threshold | +2.10% | +2.29% |
| CHIP/USDT:USDT | below_1h_threshold | +1.87% | +2.06% |
| DYM/USDT:USDT | below_1h_threshold | +1.64% | +1.83% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
