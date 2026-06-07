# Decision Report

- generated_at: 2026-06-07T23:13:54.931372+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6006**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6006, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=-0.33%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.33% | **-0.33%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 3/16 | 18.8% | +2.45% | **+0.46%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.95% | **+0.29%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +1.03% | **+0.26%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.04% | **+0.03%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/4 | 100.0% | +3.16% | **+3.16%** |
| LIMIT_3PCT_LONG | 16/20 | 80.0% | +2.59% | **+2.07%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +1.56% | **+1.33%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +0.88% | **+0.57%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +1.11% | **+0.56%** |

## 2. $100 Live Portfolio

- 残高: **$99.00** / 初期 $100.00 (-1.00%)
- 確定トレード: 5件 (TP 1 / SL 4 / EXP 0)
- 最新: BSB/USDT:USDT SL_HIT PnL -4.00% 残高後 $99.00
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$154.64** / 初期 $100.00 (+54.64%)
- 確定: 1123件 (Win 275 / Loss 339 / Flat 509) / skip 1444件
- 成長率目線: 平均log +0.000388 / 幾何平均 +0.039% per trade / maxDD +7.25%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BTW/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.77% 残高後 $154.64

## 4. Latest Market Context

- 更新: 2026-06-07T23:13:52.288246+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.10% price=62896.9
- Funnel: target 769 → liquid 133 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BTW/USDT:USDT | +36.01% | $15,169,188.63 |
| BANK/USDT:USDT | +27.05% | $4,067,304.19 |
| BEAT/USDT:USDT | +25.29% | $78,050,380.24 |
| PIPPIN/USDT:USDT | +23.63% | $4,536,947.59 |
| BLESS/USDT:USDT | +17.00% | $8,489,226.10 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BTW/USDT:USDT | below_1h_threshold | +2.11% | +2.01% |
| GUA/USDT:USDT | below_1h_threshold | +1.91% | +1.82% |
| PIPPIN/USDT:USDT | below_1h_threshold | +1.30% | +1.20% |
| BABY/USDT:USDT | below_1h_threshold | +1.23% | +1.13% |
| BEAT/USDT:USDT | below_1h_threshold | +1.05% | +0.95% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
