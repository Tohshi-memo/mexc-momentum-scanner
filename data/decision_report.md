# Decision Report

- generated_at: 2026-09-20T02:51:31.148398+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15129**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=15129, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.15%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.15% | **+0.15%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 8/20 | 40.0% | +2.65% | **+1.06%** |
| LIMIT_5PCT | 9/20 | 45.0% | +1.74% | **+0.78%** |
| LIMIT_7PCT | 4/20 | 20.0% | +2.80% | **+0.56%** |
| LIMIT_ATR | 13/20 | 65.0% | +0.67% | **+0.44%** |
| LIMIT_8PCT | 2/20 | 10.0% | +3.70% | **+0.37%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +1.94% | **+1.65%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +1.52% | **+0.99%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +0.93% | **+0.89%** |
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +3.67% | **+0.73%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +1.07% | **+0.64%** |

## 2. $100 Live Portfolio

- 残高: **$120.56** / 初期 $100.00 (+20.56%)
- 確定トレード: 215件 (TP 79 / SL 131 / EXP 5)
- 最新: BULLA/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.56
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,211.64** / 初期 $100.00 (+1111.64%)
- 確定: 5657件 (Win 1698 / Loss 1831 / Flat 2128) / skip 6033件
- 成長率目線: 平均log +0.000441 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ONE/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.77% 残高後 $1,211.64

## 4. Robust Adaptive DryRun ($100)

- 残高: **$247.30** / 初期 $100.00 (+147.30%)
- 確定: 3242件 (Win 900 / Loss 762 / Flat 1580) / skip 5298件
- 成長率目線: 平均log +0.000279 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0553 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ONE/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $247.30

## 5. Causal Adaptive DryRun ($100)

- 残高: **$121.37** / 初期 $100.00 (+21.37%)
- 確定: 2978件 (Win 880 / Loss 1179 / Flat 919) / pending 0件 / skip 3625件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000263 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CATE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $121.37

## 6. Latest Market Context

- 更新: 2026-09-20T02:51:17.034182+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.59% price=80590.6
- Funnel: target 1050 → liquid 142 → pre 50 → checked 50 → surge 3 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 97.6 >= 65=1, 4h RSI 80.1 >= 65=1, 4h RSI 86.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CELR/USDT:USDT | +94.61% | $2,718,677.11 |
| OFC/USDT:USDT | +63.09% | $2,099,858.05 |
| ONE/USDT:USDT | +30.31% | $48,553,203.59 |
| G/USDT:USDT | +23.39% | $11,433,052.94 |
| BANK/USDT:USDT | +21.31% | $2,937,903.68 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| EVAA/USDT:USDT | below_1h_threshold | +4.02% | +4.60% |
| BANK/USDT:USDT | below_1h_threshold | +3.72% | +4.31% |
| OFC/USDT:USDT | below_1h_threshold | +3.40% | +3.98% |
| ZIL/USDT:USDT | below_1h_threshold | +2.57% | +3.15% |
| PIEVERSE/USDT:USDT | below_1h_threshold | +2.51% | +3.10% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
