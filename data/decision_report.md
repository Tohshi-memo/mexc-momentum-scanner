# Decision Report

- generated_at: 2026-06-06T12:35:43.147960+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5826**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.80% / filled 20/20。**
- 全期間 MARKET基準: n=5826, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.80%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 18/20 | 90.0% | +1.45% | **+1.30%** |
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |
| LIMIT_7PCT | 6/20 | 30.0% | +2.54% | **+0.76%** |
| ASK | 20/20 | 100.0% | +0.74% | **+0.74%** |
| LIMIT_BB3S | 5/13 | 38.5% | +1.78% | **+0.69%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +2.88% | **+1.44%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +1.53% | **+0.84%** |
| LIMIT_FIB1272_LONG | 4/20 | 20.0% | +3.58% | **+0.72%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +1.36% | **+0.68%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +2.48% | **+0.62%** |

## 2. $100 Live Portfolio

- 残高: **$100.00** / 初期 $100.00 (+0.00%)
- 確定トレード: 0件 (TP 0 / SL 0 / EXP 0)

## 3. Safe Adaptive DryRun ($100)

- 残高: **$130.54** / 初期 $100.00 (+30.54%)
- 確定: 1014件 (Win 239 / Loss 313 / Flat 462) / skip 1373件
- 成長率目線: 平均log +0.000263 / 幾何平均 +0.026% per trade / maxDD +7.25%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ALLO/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $130.54

## 4. Latest Market Context

- 更新: 2026-06-06T12:35:40.352940+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.07% price=60814.1
- Funnel: target 771 → liquid 149 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ALLO/USDT:USDT | +107.39% | $53,425,480.32 |
| VELVET/USDT:USDT | +50.82% | $3,294,902.57 |
| BLUAI/USDT:USDT | +47.91% | $3,702,821.07 |
| CLO/USDT:USDT | +31.48% | $2,594,426.08 |
| HEI/USDT:USDT | +27.31% | $3,072,175.71 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| HEI/USDT:USDT | below_1h_threshold | +4.33% | +4.27% |
| CLO/USDT:USDT | below_1h_threshold | +2.99% | +2.92% |
| ALLO/USDT:USDT | below_1h_threshold | +2.10% | +2.03% |
| BEAT/USDT:USDT | below_1h_threshold | +1.59% | +1.52% |
| H/USDT:USDT | below_1h_threshold | +1.51% | +1.45% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
