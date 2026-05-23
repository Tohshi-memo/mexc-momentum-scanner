# Decision Report

- generated_at: 2026-05-23T07:49:11.486283+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4761**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.50% / filled 20/20。**
- 全期間 MARKET基準: n=4761, expectancy=-0.08%
- 直近20件 MARKET基準: n=20, expectancy=+1.50%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.50% | **+1.50%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.50% | **+1.50%** |
| ASK | 20/20 | 100.0% | +1.45% | **+1.45%** |
| LIMIT_1PCT | 18/20 | 90.0% | +1.05% | **+0.95%** |
| LIMIT_ATR | 10/20 | 50.0% | +0.93% | **+0.46%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +5.11% | **+1.02%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +2.48% | **+0.62%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | -0.62% | **-0.09%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | -0.24% | **-0.17%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | -0.50% | **-0.20%** |

## 2. $100 Live Portfolio

- 残高: **$96.20** / 初期 $100.00 (-3.80%)
- 確定トレード: 61件 (TP 16 / SL 42 / EXP 3)
- 最新: PLAY/USDT:USDT TP_HIT PnL +8.00% 残高後 $96.20
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$122.13** / 初期 $100.00 (+22.13%)
- 確定: 607件 (Win 150 / Loss 193 / Flat 264) / skip 715件
- 成長率目線: 平均log +0.000329 / 幾何平均 +0.033% per trade / maxDD +4.21%
- 次の候補: `LIMIT_10PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: GMTTOKEN/USDT:USDT `LIMIT_10PCT_LONG` EXPIRED account +0.00% 残高後 $122.13

## 4. Latest Market Context

- 更新: 2026-05-23T07:49:08.236379+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.40% price=75068.9
- Funnel: target 764 → liquid 132 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 82.1 >= 65=1, 4h RSI 77.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BSB/USDT:USDT | +115.63% | $64,795,953.60 |
| GMTTOKEN/USDT:USDT | +29.66% | $1,240,474.52 |
| IN/USDT:USDT | +17.21% | $1,849,307.80 |
| BEAT/USDT:USDT | +13.92% | $63,924,043.06 |
| TAG/USDT:USDT | +10.30% | $1,425,659.43 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| H/USDT:USDT | below_1h_threshold | +2.69% | +3.08% |
| BILL/USDT:USDT | below_1h_threshold | +1.92% | +2.32% |
| TAG/USDT:USDT | below_1h_threshold | +1.27% | +1.67% |
| FUTUSTOCK/USDT:USDT | below_1h_threshold | +1.01% | +1.40% |
| SKYAI/USDT:USDT | below_1h_threshold | +0.62% | +1.02% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
