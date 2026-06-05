# Decision Report

- generated_at: 2026-06-05T09:56:07.067467+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5707**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.53% / filled 20/20。**
- 全期間 MARKET基準: n=5707, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.53%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.53% | **+0.53%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 6/20 | 30.0% | +2.81% | **+0.84%** |
| ASK | 20/20 | 100.0% | +0.68% | **+0.68%** |
| LIMIT_2PCT | 16/20 | 80.0% | +0.77% | **+0.62%** |
| MARKET | 20/20 | 100.0% | +0.53% | **+0.53%** |
| LIMIT_6PCT | 5/20 | 25.0% | +1.89% | **+0.47%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +0.92% | **+0.60%** |
| LIMIT_FIB1618_LONG | 6/20 | 30.0% | +1.17% | **+0.35%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +0.10% | **+0.06%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | -0.18% | **-0.04%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | -0.89% | **-0.09%** |

## 2. $100 Live Portfolio

- 残高: **$99.03** / 初期 $100.00 (-0.97%)
- 確定トレード: 100件 (TP 31 / SL 66 / EXP 3)
- 最新: OPG/USDT:USDT TP_HIT PnL +8.00% 残高後 $99.03
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$131.20** / 初期 $100.00 (+31.20%)
- 確定: 1009件 (Win 239 / Loss 312 / Flat 458) / skip 1259件
- 成長率目線: 平均log +0.000269 / 幾何平均 +0.027% per trade / maxDD +7.25%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ZEST/USDT:USDT `LIMIT_3PCT_LONG` EXPIRED account +0.00% 残高後 $131.20

## 4. Latest Market Context

- 更新: 2026-06-05T09:56:03.796898+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.68% price=62855.3
- Funnel: target 773 → liquid 161 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=46, below_relative_strength=1, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 71.5 >= 65=1, 4h RSI 72.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BTW/USDT:USDT | +78.79% | $22,484,981.66 |
| OPN/USDT:USDT | +31.50% | $40,625,602.88 |
| BABY/USDT:USDT | +28.72% | $2,833,738.81 |
| CLO/USDT:USDT | +15.63% | $1,043,447.86 |
| BEAT/USDT:USDT | +13.79% | $27,734,322.60 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SKYAI/USDT:USDT | below_relative_strength | +5.13% | +4.45% |
| BIANRENSHENG/USDT:USDT | below_1h_threshold | +4.99% | +4.31% |
| BTW/USDT:USDT | below_1h_threshold | +3.40% | +2.71% |
| EPIC/USDT:USDT | below_1h_threshold | +3.20% | +2.52% |
| MONAD/USDT:USDT | below_1h_threshold | +3.19% | +2.51% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
