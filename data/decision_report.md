# Decision Report

- generated_at: 2026-05-10T22:07:37.394499+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3994**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3994, expectancy=-0.13%
- 直近20件 MARKET基準: n=20, expectancy=+0.10%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.10% | **+0.10%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 7/20 | 35.0% | +2.54% | **+0.89%** |
| LIMIT_7PCT | 2/20 | 10.0% | +5.40% | **+0.54%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.95% | **+0.29%** |
| ASK | 20/20 | 100.0% | +0.10% | **+0.10%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 16/20 | 80.0% | +2.67% | **+2.13%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.43% | **+1.00%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +1.76% | **+0.97%** |
| LIMIT_BB3S_LONG | 6/7 | 85.7% | +0.99% | **+0.85%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.86% | **+0.77%** |

## 2. $100 Live Portfolio

- 残高: **$98.21** / 初期 $100.00 (-1.79%)
- 確定トレード: 30件 (TP 7 / SL 20 / EXP 3)
- 最新: SATO/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.21
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$109.48** / 初期 $100.00 (+9.48%)
- 確定: 204件 (Win 51 / Loss 68 / Flat 85) / skip 351件
- 成長率目線: 平均log +0.000444 / 幾何平均 +0.044% per trade / maxDD +4.09%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: US/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.00% 残高後 $109.48

## 4. Latest Market Context

- 更新: 2026-05-10T22:07:34.434741+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.59% price=81148.8
- Funnel: target 769 → liquid 173 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| US/USDT:USDT | +50.33% | $4,779,084.31 |
| ALCH/USDT:USDT | +20.38% | $3,335,862.73 |
| TROLLSOL/USDT:USDT | +17.58% | $4,522,437.95 |
| B/USDT:USDT | +14.61% | $2,378,916.82 |
| SUI/USDT:USDT | +10.59% | $741,904,427.90 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| US/USDT:USDT | below_1h_threshold | +2.26% | +1.67% |
| IP/USDT:USDT | below_1h_threshold | +2.16% | +1.58% |
| FHE/USDT:USDT | below_1h_threshold | +1.76% | +1.17% |
| SKYAI/USDT:USDT | below_1h_threshold | +1.65% | +1.06% |
| NIL/USDT:USDT | below_1h_threshold | +1.57% | +0.98% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
