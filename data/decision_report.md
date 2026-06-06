# Decision Report

- generated_at: 2026-06-06T12:30:05.923576+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5825**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5825, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 6/20 | 30.0% | +2.54% | **+0.76%** |
| LIMIT_FIB1272 | 4/20 | 20.0% | +3.58% | **+0.72%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.78% | **+0.70%** |
| LIMIT_10PCT | 2/20 | 10.0% | +5.45% | **+0.55%** |
| LIMIT_9PCT | 2/20 | 10.0% | +4.59% | **+0.46%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +3.64% | **+1.64%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +2.08% | **+1.04%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +1.96% | **+0.88%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +2.29% | **+0.80%** |
| LIMIT_FIB1272_LONG | 4/20 | 20.0% | +3.58% | **+0.72%** |

## 2. $100 Live Portfolio

- 残高: **$100.00** / 初期 $100.00 (+0.00%)
- 確定トレード: 0件 (TP 0 / SL 0 / EXP 0)

## 3. Safe Adaptive DryRun ($100)

- 残高: **$130.54** / 初期 $100.00 (+30.54%)
- 確定: 1014件 (Win 239 / Loss 313 / Flat 462) / skip 1372件
- 成長率目線: 平均log +0.000263 / 幾何平均 +0.026% per trade / maxDD +7.25%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ALLO/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $130.54

## 4. Latest Market Context

- 更新: 2026-06-06T12:30:03.093999+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.12% price=60702.7
- Funnel: target 771 → liquid 148 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ALLO/USDT:USDT | +107.18% | $51,946,728.40 |
| BLUAI/USDT:USDT | +52.05% | $3,636,183.63 |
| VELVET/USDT:USDT | +50.22% | $3,284,002.31 |
| CLO/USDT:USDT | +28.66% | $2,579,160.42 |
| HEI/USDT:USDT | +22.79% | $3,022,201.21 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ALLO/USDT:USDT | below_1h_threshold | +1.80% | +1.92% |
| CLO/USDT:USDT | below_1h_threshold | +1.22% | +1.34% |
| BEAT/USDT:USDT | below_1h_threshold | +0.99% | +1.11% |
| SKYAI/USDT:USDT | below_1h_threshold | +0.89% | +1.00% |
| HEI/USDT:USDT | below_1h_threshold | +0.63% | +0.75% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
