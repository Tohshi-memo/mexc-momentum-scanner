# Decision Report

- generated_at: 2026-06-02T23:43:31.319596+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5502**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.92% / filled 20/20。**
- 全期間 MARKET基準: n=5502, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=+0.92%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.92% | **+0.92%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.98% | **+0.98%** |
| MARKET | 20/20 | 100.0% | +0.92% | **+0.92%** |
| LIMIT_6PCT | 5/20 | 25.0% | +1.97% | **+0.49%** |
| LIMIT_9PCT | 2/20 | 10.0% | +4.67% | **+0.47%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.48% | **+0.43%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +3.40% | **+0.51%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +0.87% | **+0.43%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +1.14% | **+0.40%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.05% | **+0.04%** |
| ASK_LONG | 20/20 | 100.0% | -0.00% | **-0.00%** |

## 2. $100 Live Portfolio

- 残高: **$96.61** / 初期 $100.00 (-3.39%)
- 確定トレード: 90件 (TP 26 / SL 61 / EXP 3)
- 最新: VVV/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.61
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$130.39** / 初期 $100.00 (+30.39%)
- 確定: 977件 (Win 229 / Loss 300 / Flat 448) / skip 1086件
- 成長率目線: 平均log +0.000272 / 幾何平均 +0.027% per trade / maxDD +7.25%
- 次の候補: `LIMIT_6PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: US/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $130.39

## 4. Latest Market Context

- 更新: 2026-06-02T23:43:28.051179+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.40% price=66623.0
- Funnel: target 770 → liquid 153 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 87.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| US/USDT:USDT | +33.59% | $7,550,612.16 |
| PORTAL/USDT:USDT | +32.91% | $12,885,674.06 |
| ESPORTS/USDT:USDT | +18.51% | $8,293,617.35 |
| LIT/USDT:USDT | +16.35% | $6,759,268.22 |
| BBSTOCK/USDT:USDT | +15.19% | $1,781,348.68 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| GENIUS/USDT:USDT | below_1h_threshold | +1.77% | +1.36% |
| PORTAL/USDT:USDT | below_1h_threshold | +1.28% | +0.88% |
| ZEC/USDT:USDT | below_1h_threshold | +1.22% | +0.81% |
| EPIC/USDT:USDT | below_1h_threshold | +1.10% | +0.69% |
| MYX/USDT:USDT | below_1h_threshold | +1.01% | +0.61% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
