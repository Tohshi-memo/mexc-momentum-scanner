# Decision Report

- generated_at: 2026-05-21T00:13:46.637706+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4584**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4584, expectancy=-0.10%
- 直近20件 MARKET基準: n=20, expectancy=-1.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.00% | **-1.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618 | 3/20 | 15.0% | -0.00% | **-0.00%** |
| LIMIT_5PCT | 10/20 | 50.0% | -0.82% | **-0.41%** |
| LIMIT_6PCT | 8/20 | 40.0% | -1.03% | **-0.41%** |
| LIMIT_7PCT | 7/20 | 35.0% | -1.31% | **-0.46%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | -1.22% | **-0.49%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 5/8 | 62.5% | +6.22% | **+3.89%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +3.49% | **+1.92%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +1.86% | **+1.77%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.22% | **+0.92%** |
| MARKET_LONG | 20/20 | 100.0% | +0.80% | **+0.80%** |

## 2. $100 Live Portfolio

- 残高: **$96.69** / 初期 $100.00 (-3.31%)
- 確定トレード: 57件 (TP 15 / SL 39 / EXP 3)
- 最新: SATO/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.69
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$123.25** / 初期 $100.00 (+23.25%)
- 確定: 542件 (Win 138 / Loss 182 / Flat 222) / skip 603件
- 成長率目線: 平均log +0.000386 / 幾何平均 +0.039% per trade / maxDD +4.21%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BSB/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $123.25

## 4. Latest Market Context

- 更新: 2026-05-21T00:13:44.613091+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.16% price=77635.2
- Funnel: target 759 → liquid 129 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| EDEN/USDT:USDT | +41.75% | $27,793,855.00 |
| NIL/USDT:USDT | +22.23% | $2,943,447.13 |
| FIDA/USDT:USDT | +17.52% | $11,572,695.82 |
| BEAT/USDT:USDT | +12.12% | $1,910,048.27 |
| JTO/USDT:USDT | +10.25% | $2,740,394.13 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NIL/USDT:USDT | below_1h_threshold | +2.33% | +2.17% |
| EDEN/USDT:USDT | below_1h_threshold | +2.01% | +1.85% |
| BEAT/USDT:USDT | below_1h_threshold | +1.35% | +1.19% |
| XMR/USDT:USDT | below_1h_threshold | +1.31% | +1.15% |
| SPACE/USDT:USDT | below_1h_threshold | +1.11% | +0.95% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
