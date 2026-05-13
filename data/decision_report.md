# Decision Report

- generated_at: 2026-05-13T03:48:16.511309+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4182**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.61% / filled 20/20。**
- 全期間 MARKET基準: n=4182, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=+0.61%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.61% | **+0.61%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +1.57% | **+1.49%** |
| LIMIT_2PCT | 15/20 | 75.0% | +1.34% | **+1.01%** |
| LIMIT_ATR | 15/20 | 75.0% | +1.33% | **+1.00%** |
| LIMIT_3PCT | 12/20 | 60.0% | +1.18% | **+0.71%** |
| MARKET | 20/20 | 100.0% | +0.61% | **+0.61%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +3.40% | **+0.51%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +1.23% | **+0.43%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +0.12% | **+0.09%** |
| LIMIT_6PCT_LONG | 7/20 | 35.0% | +0.05% | **+0.02%** |
| LIMIT_8PCT_LONG | 5/20 | 25.0% | +0.00% | **+0.00%** |

## 2. $100 Live Portfolio

- 残高: **$98.69** / 初期 $100.00 (-1.31%)
- 確定トレード: 35件 (TP 9 / SL 23 / EXP 3)
- 最新: KITE/USDT:USDT SL_HIT PnL -3.91% 残高後 $98.69
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$119.82** / 初期 $100.00 (+19.82%)
- 確定: 318件 (Win 91 / Loss 113 / Flat 114) / skip 425件
- 成長率目線: 平均log +0.000569 / 幾何平均 +0.057% per trade / maxDD +4.21%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: VIC/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.12% 残高後 $119.82

## 4. Latest Market Context

- 更新: 2026-05-13T03:48:10.095607+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.16% price=81147.5
- Funnel: target 763 → liquid 185 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=46, below_relative_strength=1, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 85.2 >= 65=1, 4h RSI 91.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| IRYS/USDT:USDT | +29.74% | $3,283,708.56 |
| LAB/USDT:USDT | +17.71% | $104,532,395.02 |
| PEAQ/USDT:USDT | +17.55% | $2,400,456.12 |
| SATO/USDT:USDT | +17.18% | $1,075,314.47 |
| TIA/USDT:USDT | +14.07% | $29,138,552.70 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SATO/USDT:USDT | below_relative_strength | +5.11% | +4.95% |
| TURBO/USDT:USDT | below_1h_threshold | +2.89% | +2.73% |
| IRYS/USDT:USDT | below_1h_threshold | +2.81% | +2.65% |
| VELO/USDT:USDT | below_1h_threshold | +2.36% | +2.20% |
| INX/USDT:USDT | below_1h_threshold | +1.99% | +1.83% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
