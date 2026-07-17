# Decision Report

- generated_at: 2026-07-17T18:31:17.277946+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8875**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=8875, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.60%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.60% | **-1.60%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 3/20 | 15.0% | +8.00% | **+1.20%** |
| LIMIT_7PCT | 4/20 | 20.0% | +5.40% | **+1.08%** |
| LIMIT_8PCT | 3/20 | 15.0% | +6.57% | **+0.99%** |
| LIMIT_6PCT | 6/20 | 30.0% | +1.92% | **+0.58%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | +1.28% | **+0.58%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.60% | **+1.60%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +1.59% | **+1.12%** |
| LIMIT_2PCT_LONG | 11/20 | 55.0% | +1.86% | **+1.02%** |
| LIMIT_6PCT_LONG | 5/20 | 25.0% | +3.95% | **+0.99%** |
| LIMIT_3PCT_LONG | 8/20 | 40.0% | +1.90% | **+0.76%** |

## 2. $100 Live Portfolio

- 残高: **$112.93** / 初期 $100.00 (+12.93%)
- 確定トレード: 112件 (TP 43 / SL 65 / EXP 4)
- 最新: BSB/USDT:USDT TP_HIT PnL +8.00% 残高後 $112.93
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$358.39** / 初期 $100.00 (+258.39%)
- 確定: 2990件 (Win 931 / Loss 952 / Flat 1107) / skip 2446件
- 成長率目線: 平均log +0.000427 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CASHCAT/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $358.39

## 4. Robust Adaptive DryRun ($100)

- 残高: **$110.02** / 初期 $100.00 (+10.02%)
- 確定: 837件 (Win 198 / Loss 172 / Flat 467) / skip 1449件
- 成長率目線: 平均log +0.000114 / 幾何平均 +0.011% per trade / maxDD +3.89%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0650 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CASHCAT/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $110.02

## 5. Causal Adaptive DryRun ($100)

- 残高: **$99.15** / 初期 $100.00 (-0.85%)
- 確定: 136件 (Win 43 / Loss 76 / Flat 17) / pending 5件 / skip 209件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000350 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: SNXX/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $99.15

## 6. Latest Market Context

- 更新: 2026-07-17T18:31:10.704765+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.06% price=63972.2
- Funnel: target 885 → liquid 174 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 65.8 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +17.75% | $11,765,051.84 |
| CASHCAT/USDT:USDT | +14.69% | $1,245,997.94 |
| VVV/USDT:USDT | +7.78% | $2,116,208.22 |
| AKE/USDT:USDT | +7.60% | $37,953,879.42 |
| BANK/USDT:USDT | +5.46% | $19,947,297.32 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| KIOXIASTOCK/USDT:USDT | below_1h_threshold | +2.43% | +2.49% |
| BULLA/USDT:USDT | below_1h_threshold | +2.38% | +2.45% |
| NBISSTOCK/USDT:USDT | below_1h_threshold | +2.36% | +2.42% |
| ZHIPUSTOCK/USDT:USDT | below_1h_threshold | +2.17% | +2.23% |
| GALA/USDT:USDT | below_1h_threshold | +1.83% | +1.89% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
