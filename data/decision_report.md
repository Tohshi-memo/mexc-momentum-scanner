# Decision Report

- generated_at: 2026-09-02T20:36:28.454810+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13380**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13380, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-1.19%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.19% | **-1.19%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_9PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_FIB1272 | 4/20 | 20.0% | +3.53% | **+0.71%** |
| LIMIT_7PCT | 2/20 | 10.0% | -0.60% | **-0.06%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +2.67% | **+1.74%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +3.56% | **+1.25%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +2.11% | **+1.06%** |
| LIMIT_BB3S_LONG | 2/3 | 66.7% | +1.46% | **+0.98%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.14% | **+0.97%** |

## 2. $100 Live Portfolio

- 残高: **$120.80** / 初期 $100.00 (+20.80%)
- 確定トレード: 198件 (TP 74 / SL 119 / EXP 5)
- 最新: FONE/USDT:USDT TP_HIT PnL +8.00% 残高後 $120.80
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$883.50** / 初期 $100.00 (+783.50%)
- 確定: 4991件 (Win 1514 / Loss 1635 / Flat 1842) / skip 4950件
- 成長率目線: 平均log +0.000437 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CASHCAT/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.81% 残高後 $883.50

## 4. Robust Adaptive DryRun ($100)

- 残高: **$184.71** / 初期 $100.00 (+84.71%)
- 確定: 2359件 (Win 666 / Loss 569 / Flat 1124) / skip 4432件
- 成長率目線: 平均log +0.000260 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1451 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CASHCAT/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $184.71

## 5. Causal Adaptive DryRun ($100)

- 残高: **$114.58** / 初期 $100.00 (+14.58%)
- 確定: 2094件 (Win 611 / Loss 820 / Flat 663) / pending 2件 / skip 2755件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000535 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: AKE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $114.58

## 6. Latest Market Context

- 更新: 2026-09-02T20:36:15.566881+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.18% price=77440.6
- Funnel: target 1044 → liquid 160 → pre 50 → checked 50 → surge 2 → strict 2
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AKE/USDT:USDT | +79.42% | $45,173,810.10 |
| SNOWSTOCK/USDT:USDT | +19.84% | $1,183,924.29 |
| BONER/USDT:USDT | +18.82% | $3,052,110.41 |
| MARSCOIN/USDT:USDT | +16.39% | $3,166,380.24 |
| BULLA/USDT:USDT | +15.80% | $2,709,076.46 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CASHCAT/USDT:USDT | below_1h_threshold | +4.12% | +3.94% |
| FONE/USDT:USDT | below_1h_threshold | +3.92% | +3.74% |
| USELESS/USDT:USDT | below_1h_threshold | +2.36% | +2.17% |
| SKYAI/USDT:USDT | below_1h_threshold | +2.20% | +2.02% |
| EGLD/USDT:USDT | below_1h_threshold | +2.15% | +1.96% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
