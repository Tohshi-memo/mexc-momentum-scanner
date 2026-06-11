# Decision Report

- generated_at: 2026-06-11T16:03:00.140954+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6374**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6374, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-0.11%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.11% | **-0.11%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 2/20 | 10.0% | +3.70% | **+0.37%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +0.21% | **+0.09%** |
| LIMIT_2PCT | 15/20 | 75.0% | +0.08% | **+0.06%** |
| ASK | 20/20 | 100.0% | +0.03% | **+0.03%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +1.75% | **+1.14%** |
| MARKET_LONG | 20/20 | 100.0% | +0.51% | **+0.51%** |
| LIMIT_7PCT_LONG | 5/20 | 25.0% | +1.97% | **+0.49%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +0.63% | **+0.44%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +0.57% | **+0.43%** |

## 2. $100 Live Portfolio

- 残高: **$95.18** / 初期 $100.00 (-4.82%)
- 確定トレード: 14件 (TP 1 / SL 12 / EXP 1)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $95.18
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$153.42** / 初期 $100.00 (+53.42%)
- 確定: 1291件 (Win 332 / Loss 408 / Flat 551) / skip 1644件
- 成長率目線: 平均log +0.000332 / 幾何平均 +0.033% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AIO/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $153.42

## 4. Latest Market Context

- 更新: 2026-06-11T16:02:57.472191+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.03% price=62702.2
- Funnel: target 782 → liquid 152 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HIGH/USDT:USDT | +2.15% | $1,218,654.36 |
| AIO/USDT:USDT | +1.59% | $9,538,150.92 |
| LAB/USDT:USDT | +1.26% | $23,352,953.93 |
| SKYAI/USDT:USDT | +0.99% | $9,468,057.61 |
| ALLO/USDT:USDT | +0.82% | $13,322,049.52 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| HIGH/USDT:USDT | below_1h_threshold | +2.16% | +2.19% |
| AIO/USDT:USDT | below_1h_threshold | +1.59% | +1.63% |
| LAB/USDT:USDT | below_1h_threshold | +1.27% | +1.30% |
| SKYAI/USDT:USDT | below_1h_threshold | +1.02% | +1.05% |
| ALLO/USDT:USDT | below_1h_threshold | +0.93% | +0.97% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
