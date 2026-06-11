# Decision Report

- generated_at: 2026-06-11T15:37:22.330553+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6372**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6372, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=+0.09%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.09% | **+0.09%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 2/20 | 10.0% | +3.70% | **+0.37%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| ASK | 20/20 | 100.0% | +0.23% | **+0.23%** |
| LIMIT_ATR | 13/20 | 65.0% | +0.25% | **+0.16%** |
| LIMIT_3PCT | 14/20 | 70.0% | +0.22% | **+0.15%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +1.52% | **+0.99%** |
| LIMIT_7PCT_LONG | 6/20 | 30.0% | +2.97% | **+0.89%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +1.16% | **+0.52%** |
| MARKET_LONG | 20/20 | 100.0% | +0.51% | **+0.51%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +0.57% | **+0.43%** |

## 2. $100 Live Portfolio

- 残高: **$95.18** / 初期 $100.00 (-4.82%)
- 確定トレード: 14件 (TP 1 / SL 12 / EXP 1)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $95.18
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$152.65** / 初期 $100.00 (+52.65%)
- 確定: 1290件 (Win 331 / Loss 408 / Flat 551) / skip 1643件
- 成長率目線: 平均log +0.000328 / 幾何平均 +0.033% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HMSTR/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $152.65

## 4. Latest Market Context

- 更新: 2026-06-11T15:37:18.846590+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.16% price=62798.9
- Funnel: target 782 → liquid 155 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=1, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| H/USDT:USDT | +101.97% | $30,622,362.51 |
| VELVET/USDT:USDT | +95.99% | $90,339,154.43 |
| AIO/USDT:USDT | +72.97% | $9,250,357.99 |
| BEAT/USDT:USDT | +59.77% | $241,256,134.52 |
| COLLECT/USDT:USDT | +49.57% | $2,453,149.44 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| H/USDT:USDT | below_relative_strength | +5.04% | +4.89% |
| LAB/USDT:USDT | below_1h_threshold | +4.92% | +4.76% |
| ESPORTS/USDT:USDT | below_1h_threshold | +4.29% | +4.14% |
| SPACE/USDT:USDT | below_1h_threshold | +3.64% | +3.49% |
| SOXL/USDT:USDT | below_1h_threshold | +3.43% | +3.27% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
