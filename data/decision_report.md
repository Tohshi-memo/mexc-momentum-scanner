# Decision Report

- generated_at: 2026-07-28T09:16:17.082878+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9687**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9687, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 4/20 | 20.0% | +4.10% | **+0.82%** |
| LIMIT_8PCT | 3/20 | 15.0% | +5.14% | **+0.77%** |
| LIMIT_9PCT | 2/20 | 10.0% | +6.29% | **+0.63%** |
| LIMIT_6PCT | 6/20 | 30.0% | +1.92% | **+0.58%** |
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 20/20 | 100.0% | +1.57% | **+1.57%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +1.42% | **+0.92%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +0.78% | **+0.62%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +2.48% | **+0.62%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +1.04% | **+0.36%** |

## 2. $100 Live Portfolio

- 残高: **$106.92** / 初期 $100.00 (+6.92%)
- 確定トレード: 148件 (TP 51 / SL 92 / EXP 5)
- 最新: BANK/USDT:USDT TP_HIT PnL +8.00% 残高後 $106.92
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$465.73** / 初期 $100.00 (+365.73%)
- 確定: 3457件 (Win 1091 / Loss 1122 / Flat 1244) / skip 2791件
- 成長率目線: 平均log +0.000445 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: DEXE/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account -0.08% 残高後 $465.73

## 4. Robust Adaptive DryRun ($100)

- 残高: **$137.24** / 初期 $100.00 (+37.24%)
- 確定: 1225件 (Win 338 / Loss 275 / Flat 612) / skip 1873件
- 成長率目線: 平均log +0.000258 / 幾何平均 +0.026% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0440 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: COTI/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $137.24

## 5. Causal Adaptive DryRun ($100)

- 残高: **$107.71** / 初期 $100.00 (+7.71%)
- 確定: 707件 (Win 228 / Loss 272 / Flat 207) / pending 4件 / skip 447件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000160 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: DEXE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $107.71

## 6. Latest Market Context

- 更新: 2026-07-28T09:16:10.142198+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=63410.8
- Funnel: target 898 → liquid 175 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| COTI/USDT:USDT | +42.54% | $16,445,506.14 |
| DEXE/USDT:USDT | +18.44% | $15,594,596.50 |
| ON/USDT:USDT | +17.69% | $16,502,732.62 |
| SOONNETWORK/USDT:USDT | +13.52% | $1,707,123.25 |
| BULLA/USDT:USDT | +12.72% | $1,568,363.98 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| JIMOTHY/USDT:USDT | below_1h_threshold | +2.84% | +2.82% |
| ESPORTS/USDT:USDT | below_1h_threshold | +2.36% | +2.35% |
| O/USDT:USDT | below_1h_threshold | +1.47% | +1.45% |
| BULLA/USDT:USDT | below_1h_threshold | +1.23% | +1.22% |
| INFQSTOCK/USDT:USDT | below_1h_threshold | +0.98% | +0.97% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
