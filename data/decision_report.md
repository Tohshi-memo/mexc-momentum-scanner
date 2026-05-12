# Decision Report

- generated_at: 2026-05-12T22:03:18.523809+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4167**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.30% / filled 20/20。**
- 全期間 MARKET基準: n=4167, expectancy=-0.13%
- 直近20件 MARKET基準: n=20, expectancy=+0.30%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.30% | **+0.30%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 6/20 | 30.0% | +2.63% | **+0.79%** |
| LIMIT_BB3S | 9/18 | 50.0% | +1.11% | **+0.56%** |
| MARKET | 20/20 | 100.0% | +0.30% | **+0.30%** |
| LIMIT_10PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_9PCT | 2/20 | 10.0% | +0.29% | **+0.03%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +2.08% | **+0.83%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +4.55% | **+0.45%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.52% | **+0.44%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +0.55% | **+0.42%** |

## 2. $100 Live Portfolio

- 残高: **$98.69** / 初期 $100.00 (-1.31%)
- 確定トレード: 35件 (TP 9 / SL 23 / EXP 3)
- 最新: KITE/USDT:USDT SL_HIT PnL -3.91% 残高後 $98.69
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$121.79** / 初期 $100.00 (+21.79%)
- 確定: 303件 (Win 88 / Loss 104 / Flat 111) / skip 425件
- 成長率目線: 平均log +0.000651 / 幾何平均 +0.065% per trade / maxDD +4.21%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: NAORIS/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $121.79

## 4. Latest Market Context

- 更新: 2026-05-12T22:03:15.266343+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.18% price=80697.3
- Funnel: target 757 → liquid 184 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TRUMPOFFICIAL/USDT:USDT | +11.41% | $21,429,834.75 |
| LAB/USDT:USDT | +10.93% | $114,702,470.88 |
| EDU/USDT:USDT | +8.11% | $4,279,946.87 |
| BILL/USDT:USDT | +7.83% | $20,683,298.46 |
| AKT/USDT:USDT | +7.73% | $2,401,484.74 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TRUTH/USDT:USDT | below_1h_threshold | +3.17% | +2.98% |
| BILL/USDT:USDT | below_1h_threshold | +1.87% | +1.69% |
| TROLLSOL/USDT:USDT | below_1h_threshold | +1.82% | +1.64% |
| ZEC/USDT:USDT | below_1h_threshold | +1.35% | +1.17% |
| SATO/USDT:USDT | below_1h_threshold | +0.99% | +0.81% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
