# Decision Report

- generated_at: 2026-06-02T00:27:10.681645+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5379**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.00% / filled 20/20。**
- 全期間 MARKET基準: n=5379, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+1.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.00% | **+1.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.00% | **+1.00%** |
| ASK | 20/20 | 100.0% | +0.99% | **+0.99%** |
| LIMIT_3PCT | 14/20 | 70.0% | +0.46% | **+0.32%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_6PCT | 6/20 | 30.0% | +0.91% | **+0.27%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +1.14% | **+0.40%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.29% | **+0.25%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +1.10% | **+0.22%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | -0.40% | **-0.06%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | -0.33% | **-0.20%** |

## 2. $100 Live Portfolio

- 残高: **$97.11** / 初期 $100.00 (-2.89%)
- 確定トレード: 83件 (TP 24 / SL 56 / EXP 3)
- 最新: SKYAI/USDT:USDT SL_HIT PnL -4.00% 残高後 $97.11
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$131.86** / 初期 $100.00 (+31.86%)
- 確定: 896件 (Win 208 / Loss 269 / Flat 419) / skip 1044件
- 成長率目線: 平均log +0.000309 / 幾何平均 +0.031% per trade / maxDD +7.25%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $131.86

## 4. Latest Market Context

- 更新: 2026-06-02T00:27:07.529571+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.32% price=71164.6
- Funnel: target 773 → liquid 144 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 79.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +65.23% | $7,633,928.94 |
| MYX/USDT:USDT | +15.48% | $6,633,763.42 |
| UB/USDT:USDT | +12.72% | $2,404,452.28 |
| WLD/USDT:USDT | +12.13% | $138,591,926.37 |
| PLAY/USDT:USDT | +10.35% | $7,478,163.75 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LAB/USDT:USDT | below_1h_threshold | +4.75% | +5.07% |
| STG/USDT:USDT | below_1h_threshold | +4.20% | +4.52% |
| H/USDT:USDT | below_1h_threshold | +4.04% | +4.36% |
| PORTAL/USDT:USDT | below_1h_threshold | +2.88% | +3.20% |
| MYX/USDT:USDT | below_1h_threshold | +2.49% | +2.81% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
