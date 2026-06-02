# Decision Report

- generated_at: 2026-06-02T11:41:38.665789+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5447**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.80% / filled 20/20。**
- 全期間 MARKET基準: n=5447, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=+0.80%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.89% | **+0.89%** |
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |
| LIMIT_4PCT | 12/20 | 60.0% | +1.00% | **+0.60%** |
| LIMIT_5PCT | 4/20 | 20.0% | +1.48% | **+0.30%** |
| LIMIT_ATR | 12/20 | 60.0% | +0.35% | **+0.21%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 5/20 | 25.0% | +0.89% | **+0.22%** |
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +0.55% | **+0.16%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | -0.14% | **-0.07%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | -0.50% | **-0.08%** |
| ASK_LONG | 20/20 | 100.0% | -0.20% | **-0.20%** |

## 2. $100 Live Portfolio

- 残高: **$97.10** / 初期 $100.00 (-2.90%)
- 確定トレード: 86件 (TP 25 / SL 58 / EXP 3)
- 最新: LIT/USDT:USDT TP_HIT PnL +8.00% 残高後 $97.10
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$132.98** / 初期 $100.00 (+32.98%)
- 確定: 959件 (Win 225 / Loss 290 / Flat 444) / skip 1049件
- 成長率目線: 平均log +0.000297 / 幾何平均 +0.030% per trade / maxDD +7.25%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MYX/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $132.98

## 4. Latest Market Context

- 更新: 2026-06-02T11:41:36.086443+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.20% price=69480.1
- Funnel: target 773 → liquid 152 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 90.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| US/USDT:USDT | +42.02% | $3,266,225.12 |
| EPIC/USDT:USDT | +38.79% | $2,663,735.32 |
| ESPORTS/USDT:USDT | +25.95% | $12,899,946.79 |
| USELESS/USDT:USDT | +25.31% | $2,384,658.75 |
| LAB/USDT:USDT | +24.41% | $189,020,476.79 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PIEVERSE/USDT:USDT | below_1h_threshold | +4.43% | +4.63% |
| MYX/USDT:USDT | below_1h_threshold | +4.01% | +4.21% |
| H/USDT:USDT | below_1h_threshold | +3.99% | +4.19% |
| NBISSTOCK/USDT:USDT | below_1h_threshold | +3.46% | +3.66% |
| JTO/USDT:USDT | below_1h_threshold | +2.54% | +2.74% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
