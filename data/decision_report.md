# Decision Report

- generated_at: 2026-07-15T08:16:15.697727+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8729**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=8729, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.76%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.76% | **-0.76%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 8/20 | 40.0% | +3.05% | **+1.22%** |
| LIMIT_8PCT | 7/20 | 35.0% | +3.34% | **+1.17%** |
| LIMIT_9PCT | 4/20 | 20.0% | +5.00% | **+1.00%** |
| LIMIT_6PCT | 8/20 | 40.0% | +1.94% | **+0.78%** |
| LIMIT_10PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 8/12 | 66.7% | +3.99% | **+2.66%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +3.64% | **+2.00%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +2.40% | **+1.80%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +2.47% | **+1.73%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +1.73% | **+1.39%** |

## 2. $100 Live Portfolio

- 残高: **$102.71** / 初期 $100.00 (+2.71%)
- 確定トレード: 97件 (TP 33 / SL 62 / EXP 2)
- 最新: DODO/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.71
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$341.54** / 初期 $100.00 (+241.54%)
- 確定: 2877件 (Win 900 / Loss 934 / Flat 1043) / skip 2413件
- 成長率目線: 平均log +0.000427 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: US/USDT:USDT `LIMIT_BB3S_LONG` EXPIRED account +0.00% 残高後 $341.54

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.47** / 初期 $100.00 (+5.47%)
- 確定: 698件 (Win 162 / Loss 164 / Flat 372) / skip 1442件
- 成長率目線: 平均log +0.000076 / 幾何平均 +0.008% per trade / maxDD +3.89%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0759 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AKE/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $105.47

## 5. Causal Adaptive DryRun ($100)

- 残高: **$98.75** / 初期 $100.00 (-1.25%)
- 確定: 60件 (Win 19 / Loss 39 / Flat 2) / pending 0件 / skip 141件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000263 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: AEHRSTOCK/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $98.75

## 6. Latest Market Context

- 更新: 2026-07-15T08:16:06.818021+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.05% price=64566.8
- Funnel: target 866 → liquid 177 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=1, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AKE/USDT:USDT | +166.99% | $8,970,965.41 |
| US/USDT:USDT | +31.37% | $3,716,713.98 |
| DODO/USDT:USDT | +30.99% | $9,212,832.96 |
| AEHRSTOCK/USDT:USDT | +30.41% | $3,288,371.93 |
| MAGMA/USDT:USDT | +20.75% | $2,715,821.15 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| B3/USDT:USDT | below_relative_strength | +5.04% | +4.98% |
| XEC/USDT:USDT | below_1h_threshold | +1.48% | +1.42% |
| BEAT/USDT:USDT | below_1h_threshold | +1.38% | +1.32% |
| KAITO/USDT:USDT | below_1h_threshold | +1.32% | +1.27% |
| LIT/USDT:USDT | below_1h_threshold | +1.01% | +0.96% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
