# Decision Report

- generated_at: 2026-08-28T23:21:27.564490+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12892**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=12892, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.03%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.03% | **+0.03%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 9/18 | 50.0% | +2.49% | **+1.25%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | +1.90% | **+0.86%** |
| LIMIT_8PCT | 2/20 | 10.0% | +5.85% | **+0.59%** |
| LIMIT_7PCT | 4/20 | 20.0% | +2.80% | **+0.56%** |
| LIMIT_6PCT | 5/20 | 25.0% | +1.89% | **+0.47%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +1.97% | **+1.97%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +2.58% | **+1.16%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +1.56% | **+1.09%** |
| LIMIT_7PCT_LONG | 6/20 | 30.0% | +3.46% | **+1.04%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +1.07% | **+1.02%** |

## 2. $100 Live Portfolio

- 残高: **$121.04** / 初期 $100.00 (+21.04%)
- 確定トレード: 193件 (TP 73 / SL 115 / EXP 5)
- 最新: AKE/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.04
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$708.89** / 初期 $100.00 (+608.89%)
- 確定: 4677件 (Win 1414 / Loss 1534 / Flat 1729) / skip 4776件
- 成長率目線: 平均log +0.000419 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MOVR/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $708.89

## 4. Robust Adaptive DryRun ($100)

- 残高: **$156.51** / 初期 $100.00 (+56.51%)
- 確定: 2003件 (Win 544 / Loss 483 / Flat 976) / skip 4300件
- 成長率目線: 平均log +0.000224 / 幾何平均 +0.022% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AKE/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $156.51

## 5. Causal Adaptive DryRun ($100)

- 残高: **$114.58** / 初期 $100.00 (+14.58%)
- 確定: 1992件 (Win 581 / Loss 765 / Flat 646) / pending 0件 / skip 2371件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000304 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: AKE/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $114.58

## 6. Latest Market Context

- 更新: 2026-08-28T23:21:16.448357+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.08% price=77663.7
- Funnel: target 1023 → liquid 151 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AKE/USDT:USDT | +39.21% | $15,432,254.34 |
| MAGMA/USDT:USDT | +14.70% | $8,870,084.98 |
| DEXE/USDT:USDT | +10.93% | $5,384,317.38 |
| TURBO/USDT:USDT | +10.70% | $1,754,849.53 |
| UAI/USDT:USDT | +5.29% | $1,353,382.91 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AKE/USDT:USDT | below_1h_threshold | +3.31% | +3.38% |
| SKYAI/USDT:USDT | below_1h_threshold | +2.36% | +2.43% |
| MAGMA/USDT:USDT | below_1h_threshold | +1.98% | +2.06% |
| UAI/USDT:USDT | below_1h_threshold | +1.25% | +1.32% |
| PYTH/USDT:USDT | below_1h_threshold | +1.04% | +1.12% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
