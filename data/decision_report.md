# Decision Report

- generated_at: 2026-07-28T03:01:17.523848+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9671**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9671, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-1.63%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.63% | **-1.63%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 6/19 | 31.6% | +4.48% | **+1.41%** |
| LIMIT_10PCT | 2/20 | 10.0% | +6.73% | **+0.67%** |
| LIMIT_6PCT | 8/20 | 40.0% | +1.18% | **+0.47%** |
| LIMIT_9PCT | 2/20 | 10.0% | +4.59% | **+0.46%** |
| LIMIT_8PCT | 4/20 | 20.0% | +1.78% | **+0.36%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +3.78% | **+1.32%** |
| LIMIT_ATR_LONG | 10/20 | 50.0% | +2.28% | **+1.14%** |
| MARKET_LONG | 20/20 | 100.0% | +1.01% | **+1.01%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +2.90% | **+1.01%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +5.70% | **+0.85%** |

## 2. $100 Live Portfolio

- 残高: **$106.92** / 初期 $100.00 (+6.92%)
- 確定トレード: 148件 (TP 51 / SL 92 / EXP 5)
- 最新: BANK/USDT:USDT TP_HIT PnL +8.00% 残高後 $106.92
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$466.17** / 初期 $100.00 (+366.17%)
- 確定: 3441件 (Win 1089 / Loss 1118 / Flat 1234) / skip 2791件
- 成長率目線: 平均log +0.000447 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ON/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $466.17

## 4. Robust Adaptive DryRun ($100)

- 残高: **$137.24** / 初期 $100.00 (+37.24%)
- 確定: 1225件 (Win 338 / Loss 275 / Flat 612) / skip 1857件
- 成長率目線: 平均log +0.000258 / 幾何平均 +0.026% per trade / maxDD +3.89%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: COTI/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $137.24

## 5. Causal Adaptive DryRun ($100)

- 残高: **$108.50** / 初期 $100.00 (+8.50%)
- 確定: 691件 (Win 224 / Loss 262 / Flat 205) / pending 3件 / skip 447件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000172 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ON/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.26% 残高後 $108.50

## 6. Latest Market Context

- 更新: 2026-07-28T03:01:10.850818+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.06% price=63186.1
- Funnel: target 902 → liquid 174 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| COTI/USDT:USDT | +74.92% | $10,567,557.20 |
| ON/USDT:USDT | +15.92% | $12,704,415.48 |
| RIF/USDT:USDT | +15.80% | $7,351,746.30 |
| SOONNETWORK/USDT:USDT | +14.23% | $1,350,016.27 |
| DEXE/USDT:USDT | +10.17% | $13,791,924.59 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CXMTSTOCK/USDT:USDT | below_1h_threshold | +2.60% | +2.54% |
| ON/USDT:USDT | below_1h_threshold | +1.57% | +1.51% |
| SOXS/USDT:USDT | below_1h_threshold | +1.44% | +1.38% |
| JIMOTHY/USDT:USDT | below_1h_threshold | +1.12% | +1.06% |
| AEON1/USDT:USDT | below_1h_threshold | +0.99% | +0.93% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
