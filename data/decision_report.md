# Decision Report

- generated_at: 2026-09-01T12:41:23.909123+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13250**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13250, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.70%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.70% | **-0.70%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 6/20 | 30.0% | +3.00% | **+0.90%** |
| LIMIT_7PCT | 4/20 | 20.0% | +4.24% | **+0.85%** |
| LIMIT_5PCT | 9/20 | 45.0% | +1.80% | **+0.81%** |
| LIMIT_8PCT | 2/20 | 10.0% | +5.85% | **+0.59%** |
| LIMIT_FIB1272 | 4/20 | 20.0% | +2.90% | **+0.58%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +2.94% | **+1.17%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +1.51% | **+0.76%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +0.99% | **+0.74%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +1.61% | **+0.73%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +0.69% | **+0.65%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 196件 (TP 73 / SL 118 / EXP 5)
- 最新: BTR/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$781.91** / 初期 $100.00 (+681.91%)
- 確定: 4885件 (Win 1486 / Loss 1613 / Flat 1786) / skip 4926件
- 成長率目線: 平均log +0.000421 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_6PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MARSCOIN/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $781.91

## 4. Robust Adaptive DryRun ($100)

- 残高: **$173.47** / 初期 $100.00 (+73.47%)
- 確定: 2229件 (Win 622 / Loss 539 / Flat 1068) / skip 4432件
- 成長率目線: 平均log +0.000247 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0654 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $173.47

## 5. Causal Adaptive DryRun ($100)

- 残高: **$115.28** / 初期 $100.00 (+15.28%)
- 確定: 2087件 (Win 610 / Loss 815 / Flat 662) / pending 0件 / skip 2634件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000198 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: PONS/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $115.28

## 6. Latest Market Context

- 更新: 2026-09-01T12:41:14.547072+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.41% price=77736.0
- Funnel: target 1037 → liquid 156 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| MARSCOIN/USDT:USDT | +74.71% | $1,984,214.22 |
| USELESS/USDT:USDT | +31.99% | $29,927,350.46 |
| ARB/USDT:USDT | +25.02% | $91,606,963.20 |
| ONG/USDT:USDT | +17.29% | $6,372,987.53 |
| CRV/USDT:USDT | +16.31% | $9,384,177.46 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ACE/USDT:USDT | below_1h_threshold | +2.67% | +3.08% |
| PONS/USDT:USDT | below_1h_threshold | +1.45% | +1.86% |
| SOXS/USDT:USDT | below_1h_threshold | +1.29% | +1.70% |
| SHEINSTOCK/USDT:USDT | below_1h_threshold | +0.48% | +0.89% |
| STX/USDT:USDT | below_1h_threshold | +0.47% | +0.88% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
