# Decision Report

- generated_at: 2026-09-05T16:06:14.860781+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13746**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13746, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.78%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.78% | **-0.78%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 3/20 | 15.0% | +2.27% | **+0.34%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.96% | **+0.29%** |
| LIMIT_8PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.13% | **+0.04%** |
| LIMIT_ATR | 15/20 | 75.0% | -0.02% | **-0.02%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +2.48% | **+1.49%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.83% | **+1.28%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +2.00% | **+1.00%** |
| LIMIT_FIB1272_LONG | 6/20 | 30.0% | +2.95% | **+0.88%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +1.51% | **+0.83%** |

## 2. $100 Live Portfolio

- 残高: **$120.80** / 初期 $100.00 (+20.80%)
- 確定トレード: 204件 (TP 76 / SL 123 / EXP 5)
- 最新: CP/USDT:USDT TP_HIT PnL +8.00% 残高後 $120.80
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$848.84** / 初期 $100.00 (+748.84%)
- 確定: 5052件 (Win 1519 / Loss 1651 / Flat 1882) / skip 5255件
- 成長率目線: 平均log +0.000423 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BULLA/USDT:USDT `LIMIT_6PCT` SL_HIT account -0.50% 残高後 $848.84

## 4. Robust Adaptive DryRun ($100)

- 残高: **$189.03** / 初期 $100.00 (+89.03%)
- 確定: 2491件 (Win 697 / Loss 588 / Flat 1206) / skip 4666件
- 成長率目線: 平均log +0.000256 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0844 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BULLA/USDT:USDT `LIMIT_6PCT` SL_HIT account -0.35% 残高後 $189.03

## 5. Causal Adaptive DryRun ($100)

- 残高: **$119.12** / 初期 $100.00 (+19.12%)
- 確定: 2370件 (Win 704 / Loss 902 / Flat 764) / pending 4件 / skip 2844件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000183 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BULLA/USDT:USDT `LIMIT_7PCT` SL_HIT account -0.17% 残高後 $119.12

## 6. Latest Market Context

- 更新: 2026-09-05T16:06:07.144186+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.04% price=79793.5
- Funnel: target 1050 → liquid 131 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| USELESS/USDT:USDT | +3.84% | $18,932,883.63 |
| EDGE/USDT:USDT | +3.15% | $1,188,011.84 |
| BULLA/USDT:USDT | +1.63% | $19,062,057.94 |
| CP/USDT:USDT | +1.30% | $1,033,317.77 |
| NIULAI/USDT:USDT | +1.23% | $1,964,578.74 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| USELESS/USDT:USDT | below_1h_threshold | +3.85% | +3.81% |
| EDGE/USDT:USDT | below_1h_threshold | +3.15% | +3.11% |
| BULLA/USDT:USDT | below_1h_threshold | +1.57% | +1.53% |
| CP/USDT:USDT | below_1h_threshold | +1.31% | +1.27% |
| NIULAI/USDT:USDT | below_1h_threshold | +1.24% | +1.20% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
