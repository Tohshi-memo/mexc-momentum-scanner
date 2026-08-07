# Decision Report

- generated_at: 2026-08-07T12:16:20.714698+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10709**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=10709, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.07%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.07% | **-0.07%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 6/20 | 30.0% | +3.92% | **+1.18%** |
| LIMIT_7PCT | 4/20 | 20.0% | +5.40% | **+1.08%** |
| LIMIT_ATR | 9/20 | 45.0% | +1.71% | **+0.77%** |
| LIMIT_5PCT | 8/20 | 40.0% | +1.83% | **+0.73%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.40% | **+0.38%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +1.96% | **+1.27%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +1.40% | **+0.98%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +1.65% | **+0.58%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.40% | **+0.36%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +0.37% | **+0.17%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 176件 (TP 67 / SL 104 / EXP 5)
- 最新: AAOISTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$595.60** / 初期 $100.00 (+495.60%)
- 確定: 3798件 (Win 1203 / Loss 1250 / Flat 1345) / skip 3472件
- 成長率目線: 平均log +0.000470 / 幾何平均 +0.047% per trade / maxDD +8.13%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HEI/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $595.60

## 4. Robust Adaptive DryRun ($100)

- 残高: **$144.49** / 初期 $100.00 (+44.49%)
- 確定: 1456件 (Win 407 / Loss 342 / Flat 707) / skip 2664件
- 成長率目線: 平均log +0.000253 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SKYAI/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $144.49

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.47** / 初期 $100.00 (+17.47%)
- 確定: 1164件 (Win 374 / Loss 457 / Flat 333) / pending 3件 / skip 1017件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000390 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: KGEN/USDT:USDT `MARKET` TP_HIT account +0.34% 残高後 $117.47

## 6. Latest Market Context

- 更新: 2026-08-07T12:16:11.562886+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.30% price=65189.1
- Funnel: target 961 → liquid 192 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SKYAI/USDT:USDT | +38.56% | $73,816,029.20 |
| CATE/USDT:USDT | +34.53% | $4,318,337.78 |
| KGEN/USDT:USDT | +33.74% | $1,912,808.75 |
| TUT/USDT:USDT | +33.14% | $1,021,045.73 |
| BICO/USDT:USDT | +26.34% | $29,071,656.06 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SKYAI/USDT:USDT | below_1h_threshold | +3.12% | +2.82% |
| CATE/USDT:USDT | below_1h_threshold | +3.01% | +2.71% |
| TUT/USDT:USDT | below_1h_threshold | +1.70% | +1.40% |
| STG/USDT:USDT | below_1h_threshold | +1.67% | +1.37% |
| BTW/USDT:USDT | below_1h_threshold | +1.29% | +0.99% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
