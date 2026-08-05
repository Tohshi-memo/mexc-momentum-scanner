# Decision Report

- generated_at: 2026-08-05T03:11:38.787972+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10343**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=10343, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-1.65%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.65% | **-1.65%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 4/20 | 20.0% | +4.78% | **+0.96%** |
| LIMIT_10PCT | 2/20 | 10.0% | +6.73% | **+0.67%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +2.37% | **+0.59%** |
| LIMIT_7PCT | 4/20 | 20.0% | +2.80% | **+0.56%** |
| LIMIT_9PCT | 2/20 | 10.0% | +4.59% | **+0.46%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.80% | **+1.80%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +1.82% | **+1.37%** |
| LIMIT_7PCT_LONG | 6/20 | 30.0% | +3.46% | **+1.04%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +1.37% | **+0.82%** |
| LIMIT_6PCT_LONG | 6/20 | 30.0% | +1.96% | **+0.59%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$586.51** / 初期 $100.00 (+486.51%)
- 確定: 3740件 (Win 1183 / Loss 1223 / Flat 1334) / skip 3164件
- 成長率目線: 平均log +0.000473 / 幾何平均 +0.047% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SKYAI/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.77% 残高後 $586.51

## 4. Robust Adaptive DryRun ($100)

- 残高: **$139.82** / 初期 $100.00 (+39.82%)
- 確定: 1285件 (Win 359 / Loss 299 / Flat 627) / skip 2469件
- 成長率目線: 平均log +0.000261 / 幾何平均 +0.026% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0077 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SKYAI/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $139.82

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.90** / 初期 $100.00 (+17.90%)
- 確定: 1099件 (Win 353 / Loss 424 / Flat 322) / pending 5件 / skip 716件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000302 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: SKYAI/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.26% 残高後 $117.90

## 6. Latest Market Context

- 更新: 2026-08-05T03:11:31.418508+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.05% price=64370.3
- Funnel: target 939 → liquid 181 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HEI/USDT:USDT | +81.44% | $7,497,208.43 |
| CASHCAT/USDT:USDT | +35.52% | $1,155,723.77 |
| MARSCOIN/USDT:USDT | +33.55% | $1,117,161.75 |
| TAKE/USDT:USDT | +32.37% | $1,508,515.00 |
| SKYAI/USDT:USDT | +25.82% | $51,838,679.22 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MARSCOIN/USDT:USDT | below_1h_threshold | +4.13% | +4.09% |
| UNI/USDT:USDT | below_1h_threshold | +1.41% | +1.36% |
| LIT/USDT:USDT | below_1h_threshold | +0.80% | +0.75% |
| ONDO/USDT:USDT | below_1h_threshold | +0.40% | +0.35% |
| SILVER/USDT:USDT | below_1h_threshold | +0.36% | +0.32% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
