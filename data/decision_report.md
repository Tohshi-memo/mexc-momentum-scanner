# Decision Report

- generated_at: 2026-09-19T18:51:31.448884+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15081**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=15081, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.31%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.31% | **-0.31%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 8/20 | 40.0% | +2.77% | **+1.11%** |
| LIMIT_2PCT | 18/20 | 90.0% | +1.01% | **+0.91%** |
| LIMIT_ATR | 16/20 | 80.0% | +1.09% | **+0.87%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.74% | **+0.70%** |
| LIMIT_4PCT | 12/20 | 60.0% | +1.04% | **+0.62%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +2.51% | **+1.00%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +1.50% | **+0.83%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +1.17% | **+0.76%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +0.97% | **+0.72%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +1.11% | **+0.45%** |

## 2. $100 Live Portfolio

- 残高: **$120.56** / 初期 $100.00 (+20.56%)
- 確定トレード: 215件 (TP 79 / SL 131 / EXP 5)
- 最新: BULLA/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.56
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,195.40** / 初期 $100.00 (+1095.40%)
- 確定: 5640件 (Win 1691 / Loss 1829 / Flat 2120) / skip 6002件
- 成長率目線: 平均log +0.000440 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AR/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $1,195.40

## 4. Robust Adaptive DryRun ($100)

- 残高: **$243.60** / 初期 $100.00 (+143.60%)
- 確定: 3196件 (Win 886 / Loss 760 / Flat 1550) / skip 5296件
- 成長率目線: 平均log +0.000279 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0244 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ONE/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $243.60

## 5. Causal Adaptive DryRun ($100)

- 残高: **$122.01** / 初期 $100.00 (+22.01%)
- 確定: 2974件 (Win 880 / Loss 1176 / Flat 918) / pending 0件 / skip 3583件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000416 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ENA/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $122.01

## 6. Latest Market Context

- 更新: 2026-09-19T18:51:18.960508+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.03% price=81400.1
- Funnel: target 1050 → liquid 147 → pre 50 → checked 50 → surge 4 → strict 0
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 88.5 >= 65=1, 4h RSI 66.9 >= 65=1, 4h RSI 81.6 >= 65=1, 4h RSI 95.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ONE/USDT:USDT | +34.80% | $29,572,029.32 |
| OFC/USDT:USDT | +34.52% | $1,428,435.80 |
| PEPE/USDT:USDT | +9.73% | $154,706,103.89 |
| CATE/USDT:USDT | +7.31% | $1,435,203.42 |
| FILECOIN/USDT:USDT | +7.23% | $12,164,294.00 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MYX/USDT:USDT | below_1h_threshold | +4.05% | +4.08% |
| EVAA/USDT:USDT | below_1h_threshold | +2.59% | +2.61% |
| XTZ/USDT:USDT | below_1h_threshold | +2.13% | +2.16% |
| AKE/USDT:USDT | below_1h_threshold | +2.12% | +2.15% |
| STX/USDT:USDT | below_1h_threshold | +1.45% | +1.48% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
