# Decision Report

- generated_at: 2026-06-09T05:33:29.515718+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6115**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.40% / filled 20/20。**
- 全期間 MARKET基準: n=6115, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.40% | **+0.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 3/20 | 15.0% | +5.72% | **+0.86%** |
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_2PCT | 16/20 | 80.0% | +0.73% | **+0.58%** |
| LIMIT_ATR | 12/20 | 60.0% | +0.94% | **+0.57%** |
| MARKET | 20/20 | 100.0% | +0.40% | **+0.40%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +0.99% | **+0.99%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +1.24% | **+0.56%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +0.84% | **+0.55%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +0.68% | **+0.41%** |

## 2. $100 Live Portfolio

- 残高: **$97.11** / 初期 $100.00 (-2.89%)
- 確定トレード: 10件 (TP 1 / SL 8 / EXP 1)
- 最新: ESPORTS/USDT:USDT SL_HIT PnL -4.00% 残高後 $97.11
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$152.70** / 初期 $100.00 (+52.70%)
- 確定: 1155件 (Win 286 / Loss 355 / Flat 514) / skip 1521件
- 成長率目線: 平均log +0.000367 / 幾何平均 +0.037% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ESPORTS/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $152.70

## 4. Latest Market Context

- 更新: 2026-06-09T05:33:26.520184+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.28% price=63392.2
- Funnel: target 774 → liquid 154 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 73.2 >= 65=1, 4h RSI 65.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +42.90% | $24,511,532.44 |
| ZEST/USDT:USDT | +29.44% | $1,082,967.67 |
| SLX/USDT:USDT | +16.01% | $1,341,035.55 |
| CTR/USDT:USDT | +15.41% | $1,159,910.89 |
| POWER/USDT:USDT | +14.35% | $1,232,077.18 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CTR/USDT:USDT | below_1h_threshold | +4.28% | +4.00% |
| EPIC/USDT:USDT | below_1h_threshold | +4.19% | +3.91% |
| BANK/USDT:USDT | below_1h_threshold | +4.06% | +3.78% |
| PIPPIN/USDT:USDT | below_1h_threshold | +3.70% | +3.42% |
| POWER/USDT:USDT | below_1h_threshold | +1.48% | +1.20% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
