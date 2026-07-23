# Decision Report

- generated_at: 2026-07-23T18:11:18.168465+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9383**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9383, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.57%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.57% | **-0.57%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 10/17 | 58.8% | +1.41% | **+0.83%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | +1.59% | **+0.72%** |
| LIMIT_8PCT | 3/20 | 15.0% | +2.57% | **+0.39%** |
| LIMIT_5PCT | 10/20 | 50.0% | +0.67% | **+0.33%** |
| LIMIT_10PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/3 | 100.0% | +2.90% | **+2.90%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +2.21% | **+1.77%** |
| MARKET_LONG | 20/20 | 100.0% | +1.60% | **+1.60%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +2.03% | **+1.32%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +1.87% | **+1.12%** |

## 2. $100 Live Portfolio

- 残高: **$103.79** / 初期 $100.00 (+3.79%)
- 確定トレード: 136件 (TP 45 / SL 86 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -2.63% 残高後 $103.79
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$425.48** / 初期 $100.00 (+325.48%)
- 確定: 3322件 (Win 1048 / Loss 1076 / Flat 1198) / skip 2622件
- 成長率目線: 平均log +0.000436 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: B/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.13% 残高後 $425.48

## 4. Robust Adaptive DryRun ($100)

- 残高: **$130.36** / 初期 $100.00 (+30.36%)
- 確定: 1162件 (Win 312 / Loss 254 / Flat 596) / skip 1632件
- 成長率目線: 平均log +0.000228 / 幾何平均 +0.023% per trade / maxDD +3.89%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0429 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BROCCOLIF3B/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $130.36

## 5. Causal Adaptive DryRun ($100)

- 残高: **$100.85** / 初期 $100.00 (+0.85%)
- 確定: 449件 (Win 149 / Loss 182 / Flat 118) / pending 5件 / skip 402件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000152 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: B/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $100.85

## 6. Latest Market Context

- 更新: 2026-07-23T18:11:12.889601+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.13% price=64742.4
- Funnel: target 897 → liquid 176 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AKE/USDT:USDT | +19.53% | $17,003,121.67 |
| ANTHROPIC/USDT:USDT | +8.01% | $16,457,883.77 |
| B/USDT:USDT | +7.33% | $3,712,878.18 |
| BILL/USDT:USDT | +6.99% | $2,352,854.10 |
| UB/USDT:USDT | +6.78% | $2,199,440.14 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| B/USDT:USDT | below_1h_threshold | +2.01% | +1.87% |
| PROM/USDT:USDT | below_1h_threshold | +1.79% | +1.65% |
| NIGHT/USDT:USDT | below_1h_threshold | +1.58% | +1.44% |
| EVAA/USDT:USDT | below_1h_threshold | +1.46% | +1.33% |
| BILL/USDT:USDT | below_1h_threshold | +1.28% | +1.15% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
