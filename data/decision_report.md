# Decision Report

- generated_at: 2026-05-21T03:13:56.581244+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4597**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.81% / filled 20/20。**
- 全期間 MARKET基準: n=4597, expectancy=-0.10%
- 直近20件 MARKET基準: n=20, expectancy=+0.81%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.81% | **+0.81%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.81% | **+0.81%** |
| LIMIT_7PCT | 3/20 | 15.0% | +4.54% | **+0.68%** |
| LIMIT_2PCT | 16/20 | 80.0% | +0.79% | **+0.63%** |
| LIMIT_6PCT | 3/20 | 15.0% | +3.92% | **+0.59%** |
| LIMIT_1PCT | 17/20 | 85.0% | +0.68% | **+0.57%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 12/20 | 60.0% | +2.03% | **+1.22%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +0.95% | **+0.57%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +1.06% | **+0.53%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +1.09% | **+0.43%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +0.67% | **+0.37%** |

## 2. $100 Live Portfolio

- 残高: **$96.69** / 初期 $100.00 (-3.31%)
- 確定トレード: 57件 (TP 15 / SL 39 / EXP 3)
- 最新: SATO/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.69
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$121.41** / 初期 $100.00 (+21.41%)
- 確定: 545件 (Win 138 / Loss 185 / Flat 222) / skip 613件
- 成長率目線: 平均log +0.000356 / 幾何平均 +0.036% per trade / maxDD +4.21%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BSB/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $121.41

## 4. Latest Market Context

- 更新: 2026-05-21T03:13:54.547808+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.04% price=77947.8
- Funnel: target 763 → liquid 127 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ROAM/USDT:USDT | +57.27% | $1,280,846.33 |
| EDEN/USDT:USDT | +43.58% | $29,797,072.61 |
| BSB/USDT:USDT | +19.26% | $61,581,710.80 |
| NIL/USDT:USDT | +18.22% | $3,461,925.38 |
| JTO/USDT:USDT | +16.85% | $3,232,807.94 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| DASH/USDT:USDT | below_1h_threshold | +2.51% | +2.47% |
| SKYAI/USDT:USDT | below_1h_threshold | +1.60% | +1.56% |
| JTO/USDT:USDT | below_1h_threshold | +1.14% | +1.10% |
| STRK/USDT:USDT | below_1h_threshold | +1.12% | +1.08% |
| NEAR/USDT:USDT | below_1h_threshold | +0.87% | +0.83% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
