# Decision Report

- generated_at: 2026-08-11T11:21:23.629970+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11253**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=11253, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-2.80%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.80% | **-2.80%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 11/20 | 55.0% | +1.78% | **+0.98%** |
| LIMIT_7PCT | 4/20 | 20.0% | +4.10% | **+0.82%** |
| LIMIT_6PCT | 5/20 | 25.0% | +1.93% | **+0.48%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +4.25% | **+0.43%** |
| LIMIT_4PCT | 18/20 | 90.0% | +0.22% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +2.91% | **+2.47%** |
| MARKET_LONG | 20/20 | 100.0% | +2.20% | **+2.20%** |
| LIMIT_ATR_LONG | 9/20 | 45.0% | +3.05% | **+1.37%** |
| LIMIT_2PCT_LONG | 9/20 | 45.0% | +2.96% | **+1.33%** |
| LIMIT_3PCT_LONG | 7/20 | 35.0% | +2.75% | **+0.96%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 177件 (TP 68 / SL 104 / EXP 5)
- 最新: EPIC/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.17
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$616.77** / 初期 $100.00 (+516.77%)
- 確定: 3937件 (Win 1230 / Loss 1285 / Flat 1422) / skip 3877件
- 成長率目線: 平均log +0.000462 / 幾何平均 +0.046% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BLUAI/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $616.77

## 4. Robust Adaptive DryRun ($100)

- 残高: **$141.89** / 初期 $100.00 (+41.89%)
- 確定: 1514件 (Win 424 / Loss 361 / Flat 729) / skip 3150件
- 成長率目線: 平均log +0.000231 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0285 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BLUAI/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $141.89

## 5. Causal Adaptive DryRun ($100)

- 残高: **$114.64** / 初期 $100.00 (+14.64%)
- 確定: 1331件 (Win 407 / Loss 525 / Flat 399) / pending 0件 / skip 1392件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000165 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ON/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $114.64

## 6. Latest Market Context

- 更新: 2026-08-11T11:21:14.096188+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.17% price=64312.6
- Funnel: target 963 → liquid 193 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BLUAI/USDT:USDT | +91.02% | $19,701,976.59 |
| VELVET/USDT:USDT | +82.40% | $17,323,525.81 |
| BTR/USDT:USDT | +39.54% | $1,273,527.26 |
| TOAD/USDT:USDT | +29.54% | $1,504,310.55 |
| CYS/USDT:USDT | +25.36% | $25,906,689.30 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LAB/USDT:USDT | below_1h_threshold | +3.99% | +3.82% |
| ON/USDT:USDT | below_1h_threshold | +2.67% | +2.50% |
| COOKIE/USDT:USDT | below_1h_threshold | +2.22% | +2.05% |
| TOAD/USDT:USDT | below_1h_threshold | +2.12% | +1.95% |
| KORU/USDT:USDT | below_1h_threshold | +1.48% | +1.31% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
