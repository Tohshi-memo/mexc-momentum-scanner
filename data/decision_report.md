# Decision Report

- generated_at: 2026-09-13T10:21:28.294019+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14413**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.76% / filled 20/20。**
- 全期間 MARKET基準: n=14413, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.76%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.76% | **+0.76%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.76% | **+0.76%** |
| LIMIT_BB3S | 3/19 | 15.8% | +2.15% | **+0.34%** |
| LIMIT_6PCT | 6/20 | 30.0% | +0.94% | **+0.28%** |
| LIMIT_5PCT | 8/20 | 40.0% | +0.67% | **+0.27%** |
| LIMIT_ATR | 12/20 | 60.0% | +0.40% | **+0.24%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +3.13% | **+1.41%** |
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +1.52% | **+1.14%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +2.01% | **+1.10%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +0.87% | **+0.70%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +3.37% | **+0.67%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 211件 (TP 78 / SL 128 / EXP 5)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,080.43** / 初期 $100.00 (+980.43%)
- 確定: 5431件 (Win 1635 / Loss 1760 / Flat 2036) / skip 5543件
- 成長率目線: 平均log +0.000438 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: VTHO/USDT:USDT `LIMIT_BB3S_LONG` EXPIRED account +0.00% 残高後 $1,080.43

## 4. Robust Adaptive DryRun ($100)

- 残高: **$223.31** / 初期 $100.00 (+123.31%)
- 確定: 2931件 (Win 815 / Loss 698 / Flat 1418) / skip 4893件
- 成長率目線: 平均log +0.000274 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_8PCT` (selected_by_robust_growth_score) / robust_score +0.0374 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: LSK/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $223.31

## 5. Causal Adaptive DryRun ($100)

- 残高: **$126.83** / 初期 $100.00 (+26.83%)
- 確定: 2853件 (Win 849 / Loss 1103 / Flat 901) / pending 3件 / skip 3033件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000246 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BTW/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $126.83

## 6. Latest Market Context

- 更新: 2026-09-13T10:21:13.935497+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.03% price=76740.1
- Funnel: target 1068 → liquid 131 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 75.4 >= 65=1, 4h RSI 96.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LSK/USDT:USDT | +314.48% | $92,580,803.77 |
| STEEM/USDT:USDT | +70.22% | $1,567,983.14 |
| ARK/USDT:USDT | +40.28% | $1,372,677.18 |
| VTHO/USDT:USDT | +34.85% | $3,233,681.23 |
| POWR/USDT:USDT | +30.93% | $2,576,088.75 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LONGXIA/USDT:USDT | below_1h_threshold | +2.75% | +2.79% |
| THETA/USDT:USDT | below_1h_threshold | +2.25% | +2.29% |
| ARK/USDT:USDT | below_1h_threshold | +1.73% | +1.77% |
| POWR/USDT:USDT | below_1h_threshold | +1.38% | +1.41% |
| ABNBSTOCK/USDT:USDT | below_1h_threshold | +1.26% | +1.30% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
