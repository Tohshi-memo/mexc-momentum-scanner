# Decision Report

- generated_at: 2026-05-13T07:23:05.544183+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4195**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.19% / filled 20/20。**
- 全期間 MARKET基準: n=4195, expectancy=-0.11%
- 直近20件 MARKET基準: n=20, expectancy=+1.19%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.19% | **+1.19%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +1.78% | **+1.69%** |
| LIMIT_ATR | 14/20 | 70.0% | +2.16% | **+1.51%** |
| LIMIT_3PCT | 14/20 | 70.0% | +1.93% | **+1.35%** |
| LIMIT_2PCT | 15/20 | 75.0% | +1.73% | **+1.30%** |
| ASK | 20/20 | 100.0% | +1.20% | **+1.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 13/20 | 65.0% | +1.38% | **+0.90%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +0.91% | **+0.46%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +0.94% | **+0.42%** |
| LIMIT_4PCT_LONG | 14/20 | 70.0% | +0.59% | **+0.41%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +0.00% | **+0.00%** |

## 2. $100 Live Portfolio

- 残高: **$97.71** / 初期 $100.00 (-2.29%)
- 確定トレード: 37件 (TP 9 / SL 25 / EXP 3)
- 最新: SATO/USDT:USDT SL_HIT PnL -4.00% 残高後 $97.71
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$120.76** / 初期 $100.00 (+20.76%)
- 確定: 331件 (Win 93 / Loss 117 / Flat 121) / skip 425件
- 成長率目線: 平均log +0.000570 / 幾何平均 +0.057% per trade / maxDD +4.21%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SATO/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $120.76

## 4. Latest Market Context

- 更新: 2026-05-13T07:23:01.566081+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.10% price=80862.9
- Funnel: target 765 → liquid 189 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 88.5 >= 65=1, 4h RSI 91.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| COS/USDT:USDT | +59.28% | $1,033,869.32 |
| IRYS/USDT:USDT | +29.57% | $5,619,687.34 |
| SATO/USDT:USDT | +19.86% | $1,249,741.00 |
| LAB/USDT:USDT | +18.93% | $105,293,341.66 |
| GUA/USDT:USDT | +17.48% | $4,449,525.01 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| INJ/USDT:USDT | below_1h_threshold | +1.53% | +1.64% |
| RIVER/USDT:USDT | below_1h_threshold | +1.31% | +1.41% |
| ESPORTS/USDT:USDT | below_1h_threshold | +1.02% | +1.12% |
| TIA/USDT:USDT | below_1h_threshold | +0.91% | +1.01% |
| STX/USDT:USDT | below_1h_threshold | +0.71% | +0.81% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
