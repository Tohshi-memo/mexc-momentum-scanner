# Decision Report

- generated_at: 2026-06-08T06:50:21.432806+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6039**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.60% / filled 20/20。**
- 全期間 MARKET基準: n=6039, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=+1.60%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.60% | **+1.60%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.60% | **+1.60%** |
| ASK | 20/20 | 100.0% | +1.17% | **+1.17%** |
| LIMIT_1PCT | 17/20 | 85.0% | +0.89% | **+0.76%** |
| LIMIT_5PCT | 4/20 | 20.0% | +0.95% | **+0.19%** |
| LIMIT_3PCT | 11/20 | 55.0% | +0.20% | **+0.11%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 7/20 | 35.0% | +2.34% | **+0.82%** |
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +3.56% | **+0.71%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +1.33% | **+0.60%** |
| LIMIT_5PCT_LONG | 14/20 | 70.0% | +0.35% | **+0.24%** |
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +0.32% | **+0.24%** |

## 2. $100 Live Portfolio

- 残高: **$97.59** / 初期 $100.00 (-2.41%)
- 確定トレード: 9件 (TP 1 / SL 7 / EXP 1)
- 最新: SKYAI/USDT:USDT SL_HIT PnL -4.00% 残高後 $97.59
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$151.21** / 初期 $100.00 (+51.21%)
- 確定: 1144件 (Win 280 / Loss 350 / Flat 514) / skip 1456件
- 成長率目線: 平均log +0.000361 / 幾何平均 +0.036% per trade / maxDD +7.25%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: GUA/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $151.21

## 4. Latest Market Context

- 更新: 2026-06-08T06:50:17.445236+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.34% price=62951.7
- Funnel: target 773 → liquid 142 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 83.2 >= 65=1, 4h RSI 67.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BEAT/USDT:USDT | +43.58% | $106,300,765.00 |
| ALLO/USDT:USDT | +29.63% | $38,098,770.09 |
| PIPPIN/USDT:USDT | +28.80% | $9,134,158.01 |
| ESPORTS/USDT:USDT | +22.09% | $7,129,607.74 |
| VELVET/USDT:USDT | +18.11% | $3,538,457.29 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BLESS/USDT:USDT | below_1h_threshold | +4.18% | +3.84% |
| NEAR/USDT:USDT | below_1h_threshold | +3.33% | +2.99% |
| BANK/USDT:USDT | below_1h_threshold | +3.32% | +2.98% |
| SAHARA/USDT:USDT | below_1h_threshold | +2.69% | +2.35% |
| KAS/USDT:USDT | below_1h_threshold | +2.52% | +2.18% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
