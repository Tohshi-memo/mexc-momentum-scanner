# Decision Report

- generated_at: 2026-07-27T10:16:10.495684+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9623**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9623, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.40% | **-0.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 10/20 | 50.0% | +3.28% | **+1.64%** |
| LIMIT_4PCT | 14/20 | 70.0% | +2.00% | **+1.40%** |
| LIMIT_6PCT | 6/20 | 30.0% | +3.96% | **+1.19%** |
| LIMIT_ATR | 13/20 | 65.0% | +1.18% | **+0.77%** |
| LIMIT_2PCT | 17/20 | 85.0% | +0.84% | **+0.71%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 15/20 | 75.0% | +2.15% | **+1.61%** |
| LIMIT_3PCT_LONG | 16/20 | 80.0% | +1.90% | **+1.52%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +2.56% | **+1.28%** |
| LIMIT_BB3S_LONG | 10/12 | 83.3% | +1.45% | **+1.21%** |
| LIMIT_4PCT_LONG | 14/20 | 70.0% | +1.14% | **+0.80%** |

## 2. $100 Live Portfolio

- 残高: **$106.92** / 初期 $100.00 (+6.92%)
- 確定トレード: 145件 (TP 50 / SL 90 / EXP 5)
- 最新: ON/USDT:USDT SL_HIT PnL -4.00% 残高後 $106.92
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$454.92** / 初期 $100.00 (+354.92%)
- 確定: 3414件 (Win 1082 / Loss 1112 / Flat 1220) / skip 2770件
- 成長率目線: 平均log +0.000444 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ON/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.00% 残高後 $454.92

## 4. Robust Adaptive DryRun ($100)

- 残高: **$137.24** / 初期 $100.00 (+37.24%)
- 確定: 1223件 (Win 338 / Loss 275 / Flat 610) / skip 1811件
- 成長率目線: 平均log +0.000259 / 幾何平均 +0.026% per trade / maxDD +3.89%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0017 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: PRL/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $137.24

## 5. Causal Adaptive DryRun ($100)

- 残高: **$108.45** / 初期 $100.00 (+8.45%)
- 確定: 646件 (Win 214 / Loss 245 / Flat 187) / pending 2件 / skip 445件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000302 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: DIA/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +0.34% 残高後 $108.45

## 6. Latest Market Context

- 更新: 2026-07-27T10:16:03.580773+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.01% price=65228.3
- Funnel: target 901 → liquid 155 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AKE/USDT:USDT | +46.54% | $39,266,240.56 |
| ON/USDT:USDT | +39.46% | $4,428,537.60 |
| DIA/USDT:USDT | +36.59% | $10,541,515.65 |
| BTW/USDT:USDT | +31.49% | $2,932,686.94 |
| NIL/USDT:USDT | +23.88% | $2,318,845.97 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ZAMA/USDT:USDT | below_1h_threshold | +1.70% | +1.72% |
| BTW/USDT:USDT | below_1h_threshold | +1.41% | +1.43% |
| PUMPFUN/USDT:USDT | below_1h_threshold | +0.93% | +0.95% |
| SPCXSTOCK/USDT:USDT | below_1h_threshold | +0.92% | +0.94% |
| KORU/USDT:USDT | below_1h_threshold | +0.87% | +0.88% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
