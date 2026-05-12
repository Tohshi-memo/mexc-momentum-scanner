# Decision Report

- generated_at: 2026-05-12T22:07:55.074392+00:00
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

- 更新: 2026-05-12T22:07:51.734455+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.20% price=80710.3
- Funnel: target 757 → liquid 186 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LAB/USDT:USDT | +11.50% | $115,044,275.86 |
| TRUMPOFFICIAL/USDT:USDT | +10.64% | $22,332,755.90 |
| AKT/USDT:USDT | +7.96% | $2,427,064.30 |
| EDU/USDT:USDT | +7.92% | $4,281,423.25 |
| KITE/USDT:USDT | +7.69% | $2,305,742.31 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AIGENSYN/USDT:USDT | below_1h_threshold | +4.08% | +3.88% |
| TROLLSOL/USDT:USDT | below_1h_threshold | +3.05% | +2.86% |
| BANANAS31/USDT:USDT | below_1h_threshold | +2.94% | +2.74% |
| TRUTH/USDT:USDT | below_1h_threshold | +2.15% | +1.95% |
| TIA/USDT:USDT | below_1h_threshold | +1.71% | +1.51% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
