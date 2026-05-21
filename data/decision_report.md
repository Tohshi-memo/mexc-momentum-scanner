# Decision Report

- generated_at: 2026-05-21T04:03:52.591205+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4602**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.91% / filled 20/20。**
- 全期間 MARKET基準: n=4602, expectancy=-0.10%
- 直近20件 MARKET基準: n=20, expectancy=+1.91%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.91% | **+1.91%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.91% | **+1.91%** |
| LIMIT_1PCT | 15/20 | 75.0% | +1.96% | **+1.47%** |
| LIMIT_2PCT | 14/20 | 70.0% | +2.04% | **+1.43%** |
| ASK | 20/20 | 100.0% | +1.31% | **+1.31%** |
| LIMIT_3PCT | 13/20 | 65.0% | +1.34% | **+0.87%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 11/20 | 55.0% | +2.52% | **+1.38%** |
| LIMIT_6PCT_LONG | 11/20 | 55.0% | +2.14% | **+1.17%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +1.44% | **+0.93%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +1.78% | **+0.80%** |
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | +1.41% | **+0.77%** |

## 2. $100 Live Portfolio

- 残高: **$96.69** / 初期 $100.00 (-3.31%)
- 確定トレード: 57件 (TP 15 / SL 39 / EXP 3)
- 最新: SATO/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.69
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$121.41** / 初期 $100.00 (+21.41%)
- 確定: 545件 (Win 138 / Loss 185 / Flat 222) / skip 618件
- 成長率目線: 平均log +0.000356 / 幾何平均 +0.036% per trade / maxDD +4.21%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BSB/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $121.41

## 4. Latest Market Context

- 更新: 2026-05-21T04:03:50.256633+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.06% price=78083.8
- Funnel: target 765 → liquid 129 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ROAM/USDT:USDT | +68.75% | $1,395,649.35 |
| EDEN/USDT:USDT | +42.34% | $29,567,498.29 |
| NIL/USDT:USDT | +21.37% | $3,403,255.61 |
| SATO/USDT:USDT | +19.12% | $3,536,561.65 |
| BSB/USDT:USDT | +15.57% | $62,021,992.89 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BSB/USDT:USDT | below_1h_threshold | +3.36% | +3.31% |
| ROAM/USDT:USDT | below_1h_threshold | +2.37% | +2.31% |
| SATO/USDT:USDT | below_1h_threshold | +1.85% | +1.80% |
| NIL/USDT:USDT | below_1h_threshold | +0.96% | +0.90% |
| STRK/USDT:USDT | below_1h_threshold | +0.65% | +0.59% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
