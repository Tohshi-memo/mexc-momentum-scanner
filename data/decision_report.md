# Decision Report

- generated_at: 2026-06-11T15:06:13.479012+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6366**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6366, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-0.39%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.39% | **-0.39%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 3/20 | 15.0% | +3.70% | **+0.56%** |
| LIMIT_10PCT | 2/20 | 10.0% | +5.45% | **+0.55%** |
| LIMIT_9PCT | 2/20 | 10.0% | +4.59% | **+0.46%** |
| LIMIT_7PCT | 3/20 | 15.0% | +0.54% | **+0.08%** |
| LIMIT_6PCT | 5/20 | 25.0% | -0.47% | **-0.12%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +0.79% | **+0.79%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +1.38% | **+0.76%** |
| ASK_LONG | 20/20 | 100.0% | +0.76% | **+0.76%** |
| LIMIT_7PCT_LONG | 6/20 | 30.0% | +2.49% | **+0.75%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +0.95% | **+0.66%** |

## 2. $100 Live Portfolio

- 残高: **$95.18** / 初期 $100.00 (-4.82%)
- 確定トレード: 14件 (TP 1 / SL 12 / EXP 1)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $95.18
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$152.66** / 初期 $100.00 (+52.66%)
- 確定: 1286件 (Win 329 / Loss 406 / Flat 551) / skip 1641件
- 成長率目線: 平均log +0.000329 / 幾何平均 +0.033% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ESPORTS/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $152.66

## 4. Latest Market Context

- 更新: 2026-06-11T15:06:10.034154+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.15% price=62605.0
- Funnel: target 782 → liquid 154 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VELVET/USDT:USDT | +106.45% | $86,665,674.47 |
| H/USDT:USDT | +88.94% | $29,403,443.24 |
| AIO/USDT:USDT | +66.23% | $9,080,699.43 |
| BEAT/USDT:USDT | +62.93% | $235,779,911.20 |
| COLLECT/USDT:USDT | +52.36% | $2,406,267.60 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SPACE/USDT:USDT | below_1h_threshold | +2.97% | +3.12% |
| LAB/USDT:USDT | below_1h_threshold | +1.81% | +1.97% |
| ID/USDT:USDT | below_1h_threshold | +1.79% | +1.94% |
| AMCSTOCK/USDT:USDT | below_1h_threshold | +1.64% | +1.79% |
| COLLECT/USDT:USDT | below_1h_threshold | +1.19% | +1.34% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
