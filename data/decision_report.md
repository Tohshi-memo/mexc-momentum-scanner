# Decision Report

- generated_at: 2026-09-02T23:36:36.352929+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13400**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13400, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-2.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.20% | **-2.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 15/20 | 75.0% | +1.98% | **+1.49%** |
| LIMIT_6PCT | 10/20 | 50.0% | +1.98% | **+0.99%** |
| LIMIT_BB3S | 7/17 | 41.2% | +1.50% | **+0.62%** |
| LIMIT_10PCT | 4/20 | 20.0% | +2.00% | **+0.40%** |
| LIMIT_8PCT | 6/20 | 30.0% | +1.29% | **+0.39%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +3.00% | **+1.20%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +2.73% | **+1.09%** |
| LIMIT_9PCT_LONG | 7/20 | 35.0% | +2.60% | **+0.91%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +2.47% | **+0.87%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +0.99% | **+0.49%** |

## 2. $100 Live Portfolio

- 残高: **$120.80** / 初期 $100.00 (+20.80%)
- 確定トレード: 198件 (TP 74 / SL 119 / EXP 5)
- 最新: FONE/USDT:USDT TP_HIT PnL +8.00% 残高後 $120.80
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$870.32** / 初期 $100.00 (+770.32%)
- 確定: 4994件 (Win 1514 / Loss 1638 / Flat 1842) / skip 4967件
- 成長率目線: 平均log +0.000433 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BTW/USDT:USDT `LIMIT_BB3S_LONG` SL_HIT account -0.50% 残高後 $870.32

## 4. Robust Adaptive DryRun ($100)

- 残高: **$184.60** / 初期 $100.00 (+84.60%)
- 確定: 2372件 (Win 671 / Loss 576 / Flat 1125) / skip 4439件
- 成長率目線: 平均log +0.000258 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_7PCT` (selected_by_robust_growth_score) / robust_score +0.0422 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BULLA/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $184.60

## 5. Causal Adaptive DryRun ($100)

- 残高: **$114.26** / 初期 $100.00 (+14.26%)
- 確定: 2109件 (Win 615 / Loss 828 / Flat 666) / pending 6件 / skip 2761件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000315 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: PONS/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $114.26

## 6. Latest Market Context

- 更新: 2026-09-02T23:36:20.931484+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.14% price=77106.0
- Funnel: target 1044 → liquid 160 → pre 50 → checked 50 → surge 3 → strict 3
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AKE/USDT:USDT | +59.56% | $72,502,029.66 |
| SNOWSTOCK/USDT:USDT | +21.72% | $1,388,049.47 |
| PONS/USDT:USDT | +17.73% | $3,442,336.89 |
| EGLD/USDT:USDT | +17.18% | $8,499,443.10 |
| CASHCAT/USDT:USDT | +12.93% | $1,919,282.73 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CASHCAT/USDT:USDT | below_1h_threshold | +3.61% | +3.47% |
| BONER/USDT:USDT | below_1h_threshold | +2.71% | +2.57% |
| LIT/USDT:USDT | below_1h_threshold | +2.57% | +2.43% |
| USELESS/USDT:USDT | below_1h_threshold | +1.47% | +1.33% |
| ETHFI/USDT:USDT | below_1h_threshold | +1.41% | +1.27% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
