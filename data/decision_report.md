# Decision Report

- generated_at: 2026-05-27T01:00:51.068787+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4912**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.54% / filled 20/20。**
- 全期間 MARKET基準: n=4912, expectancy=-0.08%
- 直近20件 MARKET基準: n=20, expectancy=+0.54%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.54% | **+0.54%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.60% | **+0.60%** |
| MARKET | 20/20 | 100.0% | +0.54% | **+0.54%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.80% | **+0.42%** |
| LIMIT_8PCT | 2/20 | 10.0% | +3.70% | **+0.37%** |
| LIMIT_3PCT | 12/20 | 60.0% | +0.51% | **+0.31%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +1.74% | **+1.30%** |
| LIMIT_BB3S_LONG | 4/5 | 80.0% | +1.23% | **+0.98%** |
| LIMIT_ATR_LONG | 15/20 | 75.0% | +1.13% | **+0.85%** |
| LIMIT_FIB1272_LONG | 12/20 | 60.0% | +0.75% | **+0.45%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +0.41% | **+0.39%** |

## 2. $100 Live Portfolio

- 残高: **$97.16** / 初期 $100.00 (-2.84%)
- 確定トレード: 65件 (TP 18 / SL 44 / EXP 3)
- 最新: ESPORTS/USDT:USDT SL_HIT PnL -4.00% 残高後 $97.16
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$129.36** / 初期 $100.00 (+29.36%)
- 確定: 679件 (Win 172 / Loss 216 / Flat 291) / skip 794件
- 成長率目線: 平均log +0.000379 / 幾何平均 +0.038% per trade / maxDD +4.72%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BILL/USDT:USDT `LIMIT_BB3S_LONG` SL_HIT account -0.50% 残高後 $129.36

## 4. Latest Market Context

- 更新: 2026-05-27T01:00:48.936506+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.21% price=76060.3
- Funnel: target 768 → liquid 137 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LUNC/USDT:USDT | +13.07% | $6,806,461.26 |
| REQ/USDT:USDT | +13.03% | $1,084,314.30 |
| MUSTOCK/USDT:USDT | +9.89% | $26,199,957.12 |
| MRVLSTOCK/USDT:USDT | +7.42% | $1,010,321.03 |
| PLAY/USDT:USDT | +6.21% | $7,824,279.72 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| WDCSTOCK/USDT:USDT | below_1h_threshold | +0.46% | +0.25% |
| DRIFT/USDT:USDT | below_1h_threshold | +0.30% | +0.09% |
| FILECOIN/USDT:USDT | below_1h_threshold | +0.29% | +0.08% |
| COSTSTOCK/USDT:USDT | below_1h_threshold | +0.20% | -0.01% |
| CHIP/USDT:USDT | below_1h_threshold | +0.14% | -0.07% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
