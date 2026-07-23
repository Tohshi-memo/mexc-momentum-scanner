# Decision Report

- generated_at: 2026-07-23T19:11:10.812153+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9386**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9386, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.50%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.50% | **-1.50%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 3/20 | 15.0% | +2.57% | **+0.39%** |
| LIMIT_BB3S | 9/16 | 56.2% | +0.68% | **+0.38%** |
| LIMIT_5PCT | 10/20 | 50.0% | +0.67% | **+0.33%** |
| LIMIT_FIB1272 | 10/20 | 50.0% | +0.63% | **+0.32%** |
| LIMIT_10PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/4 | 100.0% | +2.89% | **+2.89%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +2.64% | **+1.98%** |
| MARKET_LONG | 20/20 | 100.0% | +1.92% | **+1.92%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +2.55% | **+1.53%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +2.43% | **+1.33%** |

## 2. $100 Live Portfolio

- 残高: **$103.79** / 初期 $100.00 (+3.79%)
- 確定トレード: 136件 (TP 45 / SL 86 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -2.63% 残高後 $103.79
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$425.48** / 初期 $100.00 (+325.48%)
- 確定: 3322件 (Win 1048 / Loss 1076 / Flat 1198) / skip 2625件
- 成長率目線: 平均log +0.000436 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: B/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.13% 残高後 $425.48

## 4. Robust Adaptive DryRun ($100)

- 残高: **$130.36** / 初期 $100.00 (+30.36%)
- 確定: 1162件 (Win 312 / Loss 254 / Flat 596) / skip 1635件
- 成長率目線: 平均log +0.000228 / 幾何平均 +0.023% per trade / maxDD +3.89%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0342 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BROCCOLIF3B/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $130.36

## 5. Causal Adaptive DryRun ($100)

- 残高: **$100.85** / 初期 $100.00 (+0.85%)
- 確定: 451件 (Win 149 / Loss 182 / Flat 120) / pending 5件 / skip 402件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000149 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BILL/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $100.85

## 6. Latest Market Context

- 更新: 2026-07-23T19:11:04.067021+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.01% price=64834.5
- Funnel: target 897 → liquid 177 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BILL/USDT:USDT | +11.13% | $2,795,946.00 |
| ON/USDT:USDT | +10.39% | $6,742,072.38 |
| UB/USDT:USDT | +9.18% | $2,307,604.29 |
| PROM/USDT:USDT | +8.65% | $1,637,483.09 |
| B/USDT:USDT | +8.39% | $3,906,441.89 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LMTSTOCK/USDT:USDT | below_1h_threshold | +1.95% | +1.97% |
| ACE/USDT:USDT | below_1h_threshold | +1.71% | +1.72% |
| BILL/USDT:USDT | below_1h_threshold | +1.44% | +1.45% |
| O/USDT:USDT | below_1h_threshold | +1.18% | +1.19% |
| MSTRSTOCK/USDT:USDT | below_1h_threshold | +1.00% | +1.01% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
