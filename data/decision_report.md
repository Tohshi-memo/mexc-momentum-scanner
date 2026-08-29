# Decision Report

- generated_at: 2026-08-29T10:36:27.972875+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12926**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=12926, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.39%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.39% | **-0.39%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 5/20 | 25.0% | +1.93% | **+0.48%** |
| LIMIT_5PCT | 5/20 | 25.0% | +1.37% | **+0.34%** |
| LIMIT_8PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_7PCT | 3/20 | 15.0% | +0.54% | **+0.08%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | -0.79% | **-0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.66% | **+1.41%** |
| MARKET_LONG | 20/20 | 100.0% | +1.19% | **+1.19%** |
| LIMIT_BB3S_LONG | 2/3 | 66.7% | +0.88% | **+0.58%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +3.40% | **+0.51%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +1.33% | **+0.40%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 194件 (TP 73 / SL 116 / EXP 5)
- 最新: SKR/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$726.74** / 初期 $100.00 (+626.74%)
- 確定: 4696件 (Win 1422 / Loss 1542 / Flat 1732) / skip 4791件
- 成長率目線: 平均log +0.000422 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HNT/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $726.74

## 4. Robust Adaptive DryRun ($100)

- 残高: **$159.18** / 初期 $100.00 (+59.18%)
- 確定: 2011件 (Win 549 / Loss 485 / Flat 977) / skip 4326件
- 成長率目線: 平均log +0.000231 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0524 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: HNT/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $159.18

## 5. Causal Adaptive DryRun ($100)

- 残高: **$115.89** / 初期 $100.00 (+15.89%)
- 確定: 2021件 (Win 593 / Loss 782 / Flat 646) / pending 3件 / skip 2372件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000290 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: HNT/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $115.89

## 6. Latest Market Context

- 更新: 2026-08-29T10:36:16.339966+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.02% price=77633.7
- Funnel: target 1023 → liquid 143 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 80.9 >= 65=1, 4h RSI 89.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TOAD/USDT:USDT | +100.72% | $1,790,553.51 |
| HNT/USDT:USDT | +95.03% | $5,144,231.57 |
| 4/USDT:USDT | +45.02% | $1,650,674.41 |
| O/USDT:USDT | +20.05% | $1,295,572.17 |
| ONG/USDT:USDT | +13.76% | $4,254,944.26 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LONGXIA/USDT:USDT | below_1h_threshold | +3.97% | +3.95% |
| PROM/USDT:USDT | below_1h_threshold | +2.62% | +2.60% |
| VELVET/USDT:USDT | below_1h_threshold | +2.41% | +2.39% |
| TUT/USDT:USDT | below_1h_threshold | +1.56% | +1.54% |
| ICP/USDT:USDT | below_1h_threshold | +1.14% | +1.12% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
