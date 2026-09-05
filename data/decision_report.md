# Decision Report

- generated_at: 2026-09-05T18:01:08.968238+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13765**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13765, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.25%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.25% | **-1.25%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 3/20 | 15.0% | +6.30% | **+0.95%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +0.68% | **+0.24%** |
| LIMIT_7PCT | 4/20 | 20.0% | -0.60% | **-0.12%** |
| LIMIT_9PCT | 3/20 | 15.0% | -1.14% | **-0.17%** |
| LIMIT_ATR | 15/20 | 75.0% | -0.26% | **-0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.80% | **+1.80%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +2.01% | **+1.41%** |
| LIMIT_2PCT_LONG | 10/20 | 50.0% | +1.55% | **+0.78%** |
| LIMIT_3PCT_LONG | 8/20 | 40.0% | +0.81% | **+0.32%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.22% | **+0.22%** |

## 2. $100 Live Portfolio

- 残高: **$121.04** / 初期 $100.00 (+21.04%)
- 確定トレード: 205件 (TP 77 / SL 123 / EXP 5)
- 最新: BONER/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.04
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$855.61** / 初期 $100.00 (+755.61%)
- 確定: 5071件 (Win 1521 / Loss 1653 / Flat 1897) / skip 5255件
- 成長率目線: 平均log +0.000423 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MAGMA/USDT:USDT `LIMIT_3PCT_LONG` EXPIRED account +0.00% 残高後 $855.61

## 4. Robust Adaptive DryRun ($100)

- 残高: **$189.65** / 初期 $100.00 (+89.65%)
- 確定: 2510件 (Win 700 / Loss 591 / Flat 1219) / skip 4666件
- 成長率目線: 平均log +0.000255 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0556 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MAGMA/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $189.65

## 5. Causal Adaptive DryRun ($100)

- 残高: **$119.95** / 初期 $100.00 (+19.95%)
- 確定: 2384件 (Win 708 / Loss 904 / Flat 772) / pending 4件 / skip 2850件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000290 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: 4/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.26% 残高後 $119.95

## 6. Latest Market Context

- 更新: 2026-09-05T18:00:59.932156+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.00% price=80030.7
- Funnel: target 1050 → liquid 126 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| 4/USDT:USDT | +20.27% | $24,574,756.60 |
| MAGMA/USDT:USDT | +18.72% | $2,162,892.89 |
| NIULAI/USDT:USDT | +14.09% | $2,630,251.23 |
| USELESS/USDT:USDT | +12.14% | $20,203,511.10 |
| BASECAT/USDT:USDT | +11.29% | $2,024,744.31 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| INTUSTOCK/USDT:USDT | below_1h_threshold | +0.52% | +0.51% |
| UNI/USDT:USDT | below_1h_threshold | +0.39% | +0.39% |
| CRV/USDT:USDT | below_1h_threshold | +0.35% | +0.35% |
| BASECAT/USDT:USDT | below_1h_threshold | +0.32% | +0.32% |
| BULLA/USDT:USDT | below_1h_threshold | +0.22% | +0.22% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
