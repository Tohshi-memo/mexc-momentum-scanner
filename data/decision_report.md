# Decision Report

- generated_at: 2026-05-13T07:58:09.466348+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4199**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.19% / filled 20/20。**
- 全期間 MARKET基準: n=4199, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=+1.19%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.19% | **+1.19%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT | 14/20 | 70.0% | +1.93% | **+1.35%** |
| ASK | 20/20 | 100.0% | +1.34% | **+1.34%** |
| MARKET | 20/20 | 100.0% | +1.19% | **+1.19%** |
| LIMIT_ATR | 14/20 | 70.0% | +1.26% | **+0.88%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.83% | **+0.74%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 12/20 | 60.0% | +0.73% | **+0.44%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +0.41% | **+0.35%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +0.46% | **+0.32%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +0.22% | **+0.15%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +0.12% | **+0.06%** |

## 2. $100 Live Portfolio

- 残高: **$97.71** / 初期 $100.00 (-2.29%)
- 確定トレード: 37件 (TP 9 / SL 25 / EXP 3)
- 最新: SATO/USDT:USDT SL_HIT PnL -4.00% 残高後 $97.71
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$120.75** / 初期 $100.00 (+20.75%)
- 確定: 335件 (Win 94 / Loss 119 / Flat 122) / skip 425件
- 成長率目線: 平均log +0.000563 / 幾何平均 +0.056% per trade / maxDD +4.21%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: B/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.01% 残高後 $120.75

## 4. Latest Market Context

- 更新: 2026-05-13T07:58:05.705440+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.00% price=80944.2
- Funnel: target 765 → liquid 192 → pre 50 → checked 50 → surge 3 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 75.6 >= 65=1, 4h RSI 89.3 >= 65=1, 4h RSI 67.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| COS/USDT:USDT | +43.64% | $1,204,285.54 |
| SATO/USDT:USDT | +19.06% | $1,291,578.06 |
| LAB/USDT:USDT | +18.15% | $107,426,140.15 |
| INJ/USDT:USDT | +17.90% | $63,093,493.25 |
| TRUTH/USDT:USDT | +14.87% | $2,158,806.24 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TROLLSOL/USDT:USDT | below_1h_threshold | +4.57% | +4.58% |
| INJ/USDT:USDT | below_1h_threshold | +3.83% | +3.83% |
| ESPORTS/USDT:USDT | below_1h_threshold | +3.23% | +3.23% |
| MITO/USDT:USDT | below_1h_threshold | +2.48% | +2.48% |
| STX/USDT:USDT | below_1h_threshold | +2.42% | +2.42% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
