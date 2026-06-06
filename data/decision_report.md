# Decision Report

- generated_at: 2026-06-06T12:52:27.778011+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5829**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.80% / filled 20/20。**
- 全期間 MARKET基準: n=5829, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.80%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |
| LIMIT_7PCT | 6/20 | 30.0% | +2.54% | **+0.76%** |
| ASK | 20/20 | 100.0% | +0.75% | **+0.75%** |
| LIMIT_FIB1272 | 4/20 | 20.0% | +3.29% | **+0.66%** |
| LIMIT_10PCT | 2/20 | 10.0% | +5.45% | **+0.55%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +2.63% | **+1.18%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.84% | **+0.76%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +0.90% | **+0.72%** |
| LIMIT_FIB1272_LONG | 4/20 | 20.0% | +3.58% | **+0.72%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +1.50% | **+0.60%** |

## 2. $100 Live Portfolio

- 残高: **$100.00** / 初期 $100.00 (+0.00%)
- 確定トレード: 0件 (TP 0 / SL 0 / EXP 0)

## 3. Safe Adaptive DryRun ($100)

- 残高: **$130.54** / 初期 $100.00 (+30.54%)
- 確定: 1014件 (Win 239 / Loss 313 / Flat 462) / skip 1376件
- 成長率目線: 平均log +0.000263 / 幾何平均 +0.026% per trade / maxDD +7.25%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ALLO/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $130.54

## 4. Latest Market Context

- 更新: 2026-06-06T12:52:22.042962+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.38% price=61004.5
- Funnel: target 771 → liquid 150 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ALLO/USDT:USDT | +102.66% | $55,239,929.61 |
| VELVET/USDT:USDT | +53.88% | $3,413,299.53 |
| BLUAI/USDT:USDT | +43.13% | $3,907,621.14 |
| CLO/USDT:USDT | +30.91% | $2,613,798.90 |
| HEI/USDT:USDT | +26.32% | $3,145,877.80 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| H/USDT:USDT | below_1h_threshold | +4.59% | +4.21% |
| HEI/USDT:USDT | below_1h_threshold | +3.43% | +3.05% |
| BEAT/USDT:USDT | below_1h_threshold | +3.09% | +2.71% |
| CLO/USDT:USDT | below_1h_threshold | +2.94% | +2.56% |
| VELVET/USDT:USDT | below_1h_threshold | +2.92% | +2.54% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
