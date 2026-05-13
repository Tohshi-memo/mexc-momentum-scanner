# Decision Report

- generated_at: 2026-05-13T00:23:24.785178+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4171**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.31% / filled 20/20。**
- 全期間 MARKET基準: n=4171, expectancy=-0.12%
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
| ASK | 20/20 | 100.0% | +1.01% | **+1.01%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +3.15% | **+0.95%** |
| LIMIT_1PCT | 17/20 | 85.0% | +0.87% | **+0.74%** |
| LIMIT_10PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +5.70% | **+0.85%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +1.73% | **+0.78%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.54% | **+0.49%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +1.14% | **+0.40%** |

## 2. $100 Live Portfolio

- 残高: **$98.69** / 初期 $100.00 (-1.31%)
- 確定トレード: 35件 (TP 9 / SL 23 / EXP 3)
- 最新: KITE/USDT:USDT SL_HIT PnL -3.91% 残高後 $98.69
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定: 307件 (Win 89 / Loss 107 / Flat 111) / skip 425件
- 成長率目線: 平均log +0.000626 / 幾何平均 +0.063% per trade / maxDD +4.21%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: VIC/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $121.17

## 4. Latest Market Context

- 更新: 2026-05-13T00:23:18.541819+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.16% price=80586.6
- Funnel: target 758 → liquid 184 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 83.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| DYM/USDT:USDT | +13.79% | $2,864,393.45 |
| IRYS/USDT:USDT | +10.64% | $2,202,277.43 |
| AKT/USDT:USDT | +10.38% | $2,686,223.23 |
| LAB/USDT:USDT | +9.55% | $107,081,494.99 |
| VIC/USDT:USDT | +9.55% | $6,657,631.35 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BASED/USDT:USDT | below_1h_threshold | +2.91% | +2.75% |
| IRYS/USDT:USDT | below_1h_threshold | +1.90% | +1.74% |
| CHZ/USDT:USDT | below_1h_threshold | +1.89% | +1.73% |
| JUP/USDT:USDT | below_1h_threshold | +1.81% | +1.66% |
| KITE/USDT:USDT | below_1h_threshold | +1.72% | +1.57% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
